# utilities.py
import hashlib
import os
import math
import mimetypes
from datetime import datetime
from typing import Optional, Tuple, Dict, Any, List

# Optional imports are handled gracefully (we don't fail hard if a lib isn't installed)
def _try_import(module_name: str):
    try:
        return __import__(module_name)
    except Exception:
        return None

_magic = _try_import("magic")      # from python-magic
_pefile = _try_import("pefile")    # from pefile
_lief = _try_import("lief")        # from lief
_ssdeep = _try_import("ssdeep")    # from ssdeep


# ================= Hashing =================
def compute_hashes_from_bytes(b: bytes) -> Tuple[str, str, str, int]:
    """Return (sha256, md5, sha1, size)."""
    return (
        hashlib.sha256(b).hexdigest(),
        hashlib.md5(b).hexdigest(),
        hashlib.sha1(b).hexdigest(),
        len(b),
    )

def compute_ssdeep_from_bytes(b: bytes) -> Optional[str]:
    """Return ssdeep fuzzy hash if ssdeep is available, else None."""
    if _ssdeep:
        try:
            return _ssdeep.hash(b)
        except Exception:
            return None
    return None


# ================= MIME / extension =================
def guess_mime_magic(b: bytes) -> Optional[str]:
    """
    Use libmagic to detect file type (e.g., 'PE32 executable (GUI) Intel 80386, for MS Windows').
    Falls back to None if python-magic is not installed.
    """
    if _magic:
        try:
            ms = _magic.Magic(mime=False)
            return ms.from_buffer(b)
        except Exception:
            return None
    return None

def guess_ext_from_name(filename: str) -> Optional[str]:
    ext = os.path.splitext(filename)[1].lower() or None
    return ext

def guess_mime_from_name(filename: str) -> Optional[str]:
    mime, _ = mimetypes.guess_type(filename)
    return mime


# ================= Entropy =================
def shannon_entropy(b: bytes) -> float:
    """Compute Shannon entropy (0..8 for byte values)."""
    if not b:
        return 0.0
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


# ================= Format identification =================
def is_pe(buf: bytes) -> bool:
    return len(buf) >= 2 and buf[:2] == b"MZ"

def _looks_like_elf(buf: bytes) -> bool:
    return len(buf) >= 4 and buf[:4] == b"\x7fELF"

def _looks_like_macho(buf: bytes) -> bool:
    if len(buf) < 4:
        return False
    magic = int.from_bytes(buf[0:4], "big")
    # Common Mach-O magics (fat + thin)
    return magic in (0xFEEDFACE, 0xFEEDFACF, 0xCEFAEDFE, 0xCFFAEDFE, 0xCAFEBABE)


# ================= PE metadata (pefile) =================
def extract_pe_metadata(b: bytes) -> Optional[Dict[str, Any]]:
    """
    Rich PE extraction via pefile: imphash, timestamp, sections, imports, etc.
    Returns None if pefile is not available or parsing fails.
    """
    if not _pefile:
        return None
    try:
        pe = _pefile.PE(data=b)

        # Type: PE32 / PE32+
        pe_type = None
        try:
            magic = pe.OPTIONAL_HEADER.Magic
            pe_type = "PE32+" if magic == 0x20B else ("PE32" if magic == 0x10B else f"0x{magic:04x}")
        except Exception:
            pass

        # COFF / header basics
        tstamp = None
        tstamp_iso = None
        machine = None
        characteristics = None
        num_sections = None

        try:
            tstamp = pe.FILE_HEADER.TimeDateStamp
            tstamp_iso = datetime.utcfromtimestamp(tstamp).strftime("%Y-%m-%d %H:%M:%S UTC")
            machine = f"0x{pe.FILE_HEADER.Machine:04x}"
            characteristics = f"0x{pe.FILE_HEADER.Characteristics:04x}"
            num_sections = pe.FILE_HEADER.NumberOfSections
        except Exception:
            pass

        # imphash
        imp_hash = None
        try:
            imp_hash = pe.get_imphash()
        except Exception:
            pass

        # Sections
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

        # Imports
        imports: Dict[str, List[str]] = {}
        try:
            if hasattr(pe, "DIRECTORY_ENTRY_IMPORT"):
                for entry in pe.DIRECTORY_ENTRY_IMPORT:
                    dll = entry.dll.decode(errors="ignore") if entry.dll else "UNKNOWN.dll"
                    funcs = []
                    for imp in entry.imports:
                        name = imp.name.decode(errors="ignore") if imp.name else f"ord_{imp.ordinal}"
                        funcs.append(name)
                    imports[dll] = funcs
        except Exception:
            pass

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
        return None


# ================= ELF / Mach-O metadata (LIEF) =================
def extract_lief_metadata(b: bytes) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    """
    Return (elf_dict, macho_dict) using LIEF if available; otherwise (None, None).
    """
    if not _lief:
        return None, None
    try:
        bin_obj = _lief.parse(list(b))
        if bin_obj is None:
            return None, None

        fmt = bin_obj.format.name if hasattr(bin_obj, "format") else "UNKNOWN"
        # ELF
        if fmt == "ELF":
            libraries = []
            try:
                libraries = list(bin_obj.libraries)
            except Exception:
                pass
            return {
                "class_type": bin_obj.header.file_type.name if hasattr(bin_obj, "header") else None,
                "machine": bin_obj.header.machine_type.name if hasattr(bin_obj, "header") else None,
                "entrypoint": int(bin_obj.entrypoint) if hasattr(bin_obj, "entrypoint") else None,  
                "libraries": libraries or None,
            }, None

        # Mach-O
        if fmt == "MACHO":
            libraries = []
            try:
                libraries = [str(cmd.name) for cmd in bin_obj.libraries]
            except Exception:
                pass
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

        return None, None
    except Exception:
        return None, None


# ================= Unified extractor =================
def full_metadata_from_bytes(filename: str, b: bytes) -> Dict[str, Any]:
    """
    Produce a unified metadata dict using external libraries where possible.
    - file_kind: PE / ELF / MACHO / UNKNOWN
    - mime_magic via libmagic if available
    - hashes: sha256, md5, sha1, ssdeep
    - entropy
    - PE / ELF / Mach-O sub-objects
    - external_providers: empty map ready for enrichment
    """
    sha256, md5, sha1, size = compute_hashes_from_bytes(b)
    ssdeep_hash = compute_ssdeep_from_bytes(b)
    mime_magic = guess_mime_magic(b)
    ext = guess_ext_from_name(filename)
    entropy = shannon_entropy(b)

    file_kind = "UNKNOWN"
    pe_meta = None
    elf_meta = None
    macho_meta = None

    if is_pe(b):
        file_kind = "PE"
        pe_meta = extract_pe_metadata(b)
    else:
        # Try LIEF to decide ELF/Mach-O
        elf_meta, macho_meta = extract_lief_metadata(b)
        if elf_meta:
            file_kind = "ELF"
        elif macho_meta:
            file_kind = "MACHO"

    meta: Dict[str, Any] = {
        "filename": filename,
        "size_bytes": size,
        "md5": md5,
        "sha1": sha1,
        "sha256": sha256,
        "ssdeep": ssdeep_hash,
        "mime_magic": mime_magic,
        "ext": ext,
        "entropy": entropy,
        "file_kind": file_kind,
        "pe": pe_meta,
        "elf": elf_meta,
        "macho": macho_meta,
        "external_providers": {}
    }
    return meta
