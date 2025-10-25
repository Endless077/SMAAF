#     ____    ____        _                __         _          
#    |_   \  /   _|      / |_             |  ]       / |_        
#      |   \/   |  .---.`| |-',--.    .--.| |  ,--. `| |-',--.   
#      | |\  /| | / /__\\| | `'_\ : / /'`\' | `'_\ : | | `'_\ :  
#     _| |_\/_| |_| \__.,| |,// | |,| \__/  | // | |,| |,// | |, 
#    |_____||_____|'.__.'\__/\'-;__/ '.__.;__]\'-;__/\__/\'-;__/ 
#                                                                                                  

# ───────────────────────────────────────────────────────────────
# Standard library
import hashlib
import math
import mimetypes
import os
import re
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

###################################################################################################

# Explicit Hard Import
def _try_import(module_name: str):
    try:
        return __import__(module_name)
    except Exception:
        return None

_lief = _try_import("lief")        # from lief
_magic = _try_import("magic")      # from python-magic
_pefile = _try_import("pefile")    # from pefile
_ssdeep = _try_import("ssdeep")    # from ssdeep

###################################################################################################

# ================= ELF / Mach-O metadata (LIEF) =================
def extract_lief_metadata(b: bytes) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    """
    Parse ELF/Mach-O using LIEF; returns (elf_dict, macho_dict).
    """
    # Check if lief is installed
    if not _lief:
        return None, None
    try:
        # LIEF expects a sequence of ints; list(b) avoids file I/O but copies memory
        bin_obj = _lief.parse(list(b))
        if bin_obj is None:
            return None, None

        # Probe binary format (ELF/MACHO/Unknown)
        fmt = bin_obj.format.name if hasattr(bin_obj, "format") else "Unknown"
        
        # --- ELF path ---
        if fmt == "ELF":
            # Collect DT_NEEDED entries; be robust to parser quirks
            libraries = []
            try:
                libraries = list(bin_obj.libraries)
            except Exception:
                pass
            # Extract core header info; guard with hasattr for stability across LIEF versions
            return {
                "class_type": bin_obj.header.file_type.name if hasattr(bin_obj, "header") else None,
                "machine": bin_obj.header.machine_type.name if hasattr(bin_obj, "header") else None,
                "entrypoint": int(bin_obj.entrypoint) if hasattr(bin_obj, "entrypoint") else None,  
                "libraries": libraries or None,
            }, None

        # --- Mach-O path ---
        if fmt == "MACHO":
            # Gather linked libraries from load commands
            libraries = []
            try:
                libraries = [str(cmd.name) for cmd in bin_obj.libraries]
            except Exception:
                pass
            # CPU type can be missing on some slices; keep it optional
            cpu = None
            try:
                cpu = bin_obj.header.cpu_type.name
            except Exception:
                pass
            return None, {
                "filetype": bin_obj.header.file_type.name if hasattr(bin_obj, "header") else None,
                "cpu_type": cpu,
                "entrypoint": int(bin_obj.entrypoint) if hasattr(bin_obj, "entrypoint") else None,
                "libraries": libraries or None,
            }

        # Unknown format (no metadata)
        return None, None
    
    except Exception:
        # Any LIEF parsing failure returns silent None to keep pipeline resilient
        return None, None

# ================= PE metadata (pefile) =================
def extract_pe_metadata(b: bytes) -> Optional[Dict[str, Any]]:
    """
    Parse PE headers/sections/imports via pefile.
    """
    # Check if pefile is installed
    if not _pefile:
        return None
    
    try:
        # Parse from in-memory bytes
        pe = _pefile.PE(data=b)

        # Determine PE type from Optional Header magic
        pe_type = None
        try:
            magic = pe.OPTIONAL_HEADER.Magic
            pe_type = "PE32+" if magic == 0x20B else ("PE32" if magic == 0x10B else f"0x{magic:04x}")
        except Exception:
            pass

        # Extract core COFF header info, keep ISO timestamp for readability
        tstamp = None
        tstamp_iso = None
        machine = None
        characteristics = None
        num_sections = None
        try:
            tstamp = pe.FILE_HEADER.TimeDateStamp
            tstamp_iso = datetime.fromtimestamp(tstamp, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
            machine = f"0x{pe.FILE_HEADER.Machine:04x}"
            characteristics = f"0x{pe.FILE_HEADER.Characteristics:04x}"
            num_sections = pe.FILE_HEADER.NumberOfSections
        except Exception:
            pass

        # Compute import hash (useful for clustering)
        imp_hash = None
        try:
            imp_hash = pe.get_imphash()
        except Exception:
            pass

        # Collect section info + entropy for packing/obfuscation hints
        sections: List[Dict[str, Any]] = []
        try:
            for s in pe.sections:
                sections.append({
                    "name": s.Name.decode(errors="ignore").rstrip("\x00"),
                    "virtual_size": s.Misc_VirtualSize,
                    "virtual_address": s.VirtualAddress,
                    "size_of_raw_data": s.SizeOfRawData,
                    "characteristics": f"0x{s.Characteristics:08x}",
                    "entropy": round(s.get_entropy(), 4) if hasattr(s, "get_entropy") else None,
                })
        except Exception:
            pass

        # Build import table map: DLL -> list of functions (names or ordinals)
        imports: Dict[str, List[str]] = {}
        try:
            if hasattr(pe, "DIRECTORY_ENTRY_IMPORT"):
                for entry in pe.DIRECTORY_ENTRY_IMPORT:
                    dll = entry.dll.decode(errors="ignore") if entry.dll else "Unknown.dll"
                    funcs = []
                    for imp in entry.imports:
                        name = imp.name.decode(errors="ignore") if imp.name else f"ord_{imp.ordinal}"
                        funcs.append(name)
                    imports[dll] = funcs
        except Exception:
            pass

        # Return normalized PE metadata dictionary
        return {
            "pe_type": pe_type,
            "imphash": imp_hash,
            "timestamp_unix": tstamp,
            "timestamp_iso": tstamp_iso,
            "machine": machine,
            "number_of_sections": num_sections,
            "characteristics": characteristics,
            "sections": sections or None,
            "imports": imports or None,
        }
    
    except Exception:
        # Any parsing error returns None to keep pipeline moving
        return None
    
# ================= Entropy =================
def shannon_entropy(b: bytes) -> float:
    """
    Shannon entropy over raw bytes (rounded for compactness).
    """
    if not b:
        return 0.0
    
    # Frequency histogram (0..255)
    freq = [0] * 256
    for x in b:
        freq[x] += 1
    entropy = 0.0
    length = len(b)
    for c in freq:
        if c:
            p = c / length
            entropy -= p * math.log2(p)
    return round(entropy, 4)

# ================= Hashing =================
def classify_hash(s: str) -> str | None:
    """
    Identify hash type by hex-length; returns 'md5'/'sha1'/'sha256' or None.
    """
    s = s.lower()
    if not re.fullmatch(r"[0-9a-f]+", s):
        return None
    
    # Length -> algorithm
    hash_map = {
        32: "md5",
        40: "sha1",
        64: "sha256",
    }
    return hash_map.get(len(s))

def hashes(b: bytes) -> Tuple[str, str, str, int]:
    """
    Compute common hashes and size once to avoid repeated passes.
    """
    return (
        hashlib.md5(b).hexdigest(),
        hashlib.sha1(b).hexdigest(),
        hashlib.sha256(b).hexdigest(),
        len(b),
    )

def ssdeep(b: bytes) -> Optional[str]:
    """
    Compute ssdeep (fuzzy hash) if library is available.
    """
    if _ssdeep:
        try:
            return _ssdeep.hash(b)
        except Exception:
            return None
    return None

# ================= MIME / extension =================
def guess_mime_magic(b: bytes) -> Optional[str]:
    """
    Best-effort magic-based type (human-readable), may raise on some platforms.
    """
    if _magic:
        try:
            ms = _magic.Magic(mime=False)
            return ms.from_buffer(b)
        except Exception:
            return None
    return None

def guess_ext_from_name(filename: str) -> Optional[str]:
    """
    Guess extension from filename (lowercased, includes leading dot).
    """
    ext = os.path.splitext(filename)[1].lower() or None
    return ext

def guess_mime_from_name(filename: str) -> Optional[str]:
    """
    Guess MIME from filename via mimetypes DB.
    """
    mime, _ = mimetypes.guess_type(filename)
    return mime

###################################################################################################

# ================= Unified extractor =================
def metadata_extractor(filename: str, b: bytes) -> Dict[str, Any]:
    """
    Metadata Extractor using file's bytes (a unified extractor).
    """
    # Extract and compute inexpensive generic features first
    entropy = shannon_entropy(b)
    mime_magic = guess_mime_magic(b)
    ext = guess_ext_from_name(filename)
    
    # Calculate the hasches from bytes
    md5, sha1, sha256, size = hashes(b)

    # Fuzzy hash (optional)
    ssdeep_hash = ssdeep(b)

    # Probe file kind via signatures before heavy parsing
    file_kind = "Unknown"
    elf_meta = None
    macho_meta = None
    pe_meta = None
    
    # Quick PE check: 'MZ' magic at offset 0
    if not(len(b) >= 2 and b[:2] == b"MZ"):
        # ELF/Mach-O via LIEF
        elf_meta, macho_meta = extract_lief_metadata(b)
        if elf_meta:
            file_kind = "ELF"
        elif macho_meta:
            file_kind = "MACHO"
    else:
        # PE via pefile
        file_kind = "PE"
        pe_meta = extract_pe_metadata(b)

    # Assemble unified metadata object
    metadata: Dict[str, Any] = {
        "filename": filename,
        "size_bytes": size,
        "ext": ext,
        "entropy": entropy,
        "mime_magic": mime_magic,
        "file_kind": file_kind,
        "elf": elf_meta,
        "macho": macho_meta,
        "pe": pe_meta,
        "md5": md5,
        "sha1": sha1,
        "sha256": sha256,
        "ssdeep": ssdeep_hash,
        "external_providers": {}
    }
    return metadata

###################################################################################################
