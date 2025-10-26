#      ______    _            _                    ________          _                         _                   
#    .' ____ \  / |_         (_)                  |_   __  |        / |_                      / |_                 
#    | (___ \_|`| |-'_ .--.  __   _ .--.   .--./)   | |_ \_| _   __`| |-'_ .--.  ,--.   .---.`| |-' .--.   _ .--.  
#     _.____`.  | | [ `/'`\][  | [ `.-. | / /'`\;   |  _| _ [ \ [  ]| | [ `/'`\]`'_\ : / /'`\]| | / .'`\ \[ `/'`\] 
#    | \____) | | |, | |     | |  | | | | \ \._//  _| |__/ | > '  < | |, | |    // | |,| \__. | |,| \__. | | |     
#     \______.' \__/[___]   [___][___||__].',__`  |________|[__]`\_]\__/[___]   \'-;__/'.___.'\__/ '.__.' [___]    
#                                        ( ( __))                                                                  

# ───────────────────────────────────────────────────────────────
# Third-party libraries
from floss.main import main as floss_call
import lief

# ───────────────────────────────────────────────────────────────
# Standard library
import io
import logging
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List

###################################################################################################

# ================= Runner =================
def _run_cmd(cmd: list[str]) -> subprocess.CompletedProcess:
    """
    Run a subprocess command and return the completed process.
    """
    logging.debug("Executing command: %s", " ".join(cmd))
    process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
    if process.returncode != 0:
        logging.warning("Command exited with code %d: %s", process.returncode, " ".join(cmd))
        if process.stderr:
            logging.debug("Stderr from command: %s", process.stderr.strip()[:1000])
    else:
        logging.debug("Command succeeded: %s", " ".join(cmd))
    return process

def _detect_file_type(file_path: Path) -> str:
    """
    Detect basic file type via heuristics
    """
    # lief detector
    if lief is not None:
        try:
            binobj = lief.parse(str(file_path))
            if binobj is None:
                logging.debug("lief.parse returned None for %s", file_path)
            else:
                fmt = binobj.format
                try:
                    # lief.EXE_FORMATS.PE
                    if fmt == lief.EXE_FORMATS.PE:
                        return "pe"
                    # lief.EXE_FORMATS.ELF
                    if fmt == lief.EXE_FORMATS.ELF:
                        return "elf"
                except Exception:
                    # string comparison
                    if str(fmt).upper().find("PE") != -1:
                        return "pe"
                    if str(fmt).upper().find("ELF") != -1:
                        return "elf"
        except Exception as e:
            logging.debug("lief.parse failed: %s", e)

    # mime-type detector
    try:
        p = _run_cmd(["file", "-b", "--mime-type", str(file_path)])
        if p.returncode == 0 and p.stdout:
            mime = p.stdout.strip().lower()
            logging.debug("file mime-type for %s -> %s", file_path, mime)
            if "x-dosexec" in mime or "pe" in mime or "application/x-msdownload" in mime:
                return "pe"
            if "elf" in mime or "application/x-executable" in mime:
                return "elf"
            # other binary mime types
            if mime.startswith("application/"):
                return "sc"
    except FileNotFoundError:
        logging.debug("'file' command not found, cannot fallback to it.")

    # Heuristic (small binary or no recognizable header)
    try:
        data = file_path.read_bytes()[:64]
        # ELF magic
        if data.startswith(b"\x7fELF"):
            return "elf"
        # PE header "MZ" at start
        if data.startswith(b"MZ"):
            return "pe"
        # otherwise if binary-like content, mark as shellcode candidate
        if any(b < 9 or (11 <= b <= 31) for b in data):
            # some non-printables present
            return "sc"
    except Exception:
        pass

    return "unknown"

###################################################################################################

# ================= Native =================
def strings_native(file_path: Path, min_len: int) -> List[Dict[str, Any]]:
    """
    Extract printable strings from a file using the system 'strings' command.
    """
    logging.info("Running 'strings' on %s (min_len=%d).", file_path, min_len)
    try:
        # Run GNU strings with offsets (-t x) and min length
        p = _run_cmd(["strings", "-a", "-n", str(min_len), "-t", "x", str(file_path)])
    except FileNotFoundError:
        logging.warning("'strings' not found on PATH, falling back to Python implementation.")
        return strings_python(file_path, min_len, source="strings_python")

    out: list[dict[str, Any]] = []
    for line in p.stdout.splitlines():
        # Split line into offset and string
        parts = line.strip().split(None, 1)
        if len(parts) == 2:
            off, s = parts[0].rstrip(":"), parts[1].strip()
        else:
            off, s = None, parts[0] if parts else ""
        
        # Store only strings of at least min_len
        if len(s) >= min_len:
            out.append({"string": s, "source": "strings", "offset": off})
    logging.info("Extracted %d strings via 'strings' from %s", len(out), file_path)
    return out

###################################################################################################

# ================= Python =================
def strings_python(file_path: Path, min_len: int, source="strings_python") -> List[Dict[str, Any]]:
    """
    Extract printable ASCII strings from a file in pure Python.
    """
    logging.info("Extracting ASCII strings (Python) from %s (min_len=%d).", file_path, min_len)
    data = file_path.read_bytes()
    logging.debug("Read %d bytes from %s", len(data), file_path)

    acc = bytearray()
    start = None
    out: list[dict[str, Any]] = []

    # Iterate through file bytes
    for i, b in enumerate(data):
        # ASCII printable range
        if 32 <= b <= 126:
            if start is None:
                start = i
            acc.append(b)
        else:
            if len(acc) >= min_len:
                out.append({
                    "string": acc.decode("ascii", "ignore"),
                    "source": source,
                    "offset": hex(start) if start is not None else None
                })
            acc.clear()
            start = None

    # Handle trailing string if file ends with printable chars
    if len(acc) >= min_len:
        out.append({
            "string": acc.decode("ascii", "ignore"),
            "source": source,
            "offset": hex(start) if start is not None else None
        })
    
    logging.info("Extracted %d strings via Python from %s", len(out), file_path)
    return out

###################################################################################################

# ================= Floss (FLARE Obfuscated String Solver)=================
def floss(file_path: Path, min_len: int) -> List[Dict[str, Any]]:
    """
    Run FLOSS (flare-floss) via its Python API instead of subprocess.
    """
    logging.info("Running FLOSS via Python API on %s (min_len=%d).", file_path, min_len)

    # Filte type detection
    file_type = _detect_file_type(file_path)

    # Decide arguments based on type
    if file_type == "pe":
        args_list = [[str(file_path)]]
    elif file_type in ("sc", "unknown"):
        # Try shellcode formats (both 64 and 32 bit)
        args_list = [
            [str(file_path), "--format", "sc64"],
            [str(file_path), "--format", "sc32"]
        ]
    else:
        logging.info("Skipping FLOSS: unsupported file type '%s'.", file_type)
        return []
    
    # Floss Strings Extraction
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    strings: list[dict[str, Any]] = []

    try:
        for args in args_list:
            try:
                floss_call(args)
            except SystemExit:
                pass
            except Exception as e:
                logging.debug("FLOSS exception for args %s: %s", args, e)
                continue

            output = sys.stdout.getvalue()
            sys.stdout = io.StringIO()

            if not output.strip():
                continue

            for line in output.splitlines():
                s = line.strip()
                if not s:
                    continue
                addr = None
                if (m := re.match(r"^(0x[a-fA-F0-9]+|\d+):\s*(.+)$", s)):
                    addr, s = m.group(1), m.group(2).strip()
                if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
                    s = s[1:-1]
                if len(s) >= min_len:
                    strings.append({"string": s, "source": "floss", "offset": addr})

            if strings:
                logging.info("FLOSS extracted %d strings from %s (mode: %s)",
                             len(strings), file_path, " ".join(args))
                break

    finally:
        sys.stdout = old_stdout

    if not strings:
        logging.info("FLOSS produced no decoded strings for %s", file_path)

    return strings

###################################################################################################

def rabin2(file_path: Path, min_len: int) -> List[Dict[str, Any]]:
    """
    Extract strings using radare2's rabin2 -zz.
    """
    logging.info("Running rabin2 on %s (min_len=%d).", file_path, min_len)
    try:
        p = _run_cmd(["rabin2", "-zz", str(file_path)])
    except FileNotFoundError:
        logging.warning("'rabin2' not found on PATH — skipping rabin2 extraction.")
        return []

    output: list[dict[str, Any]] = []
    for line in p.stdout.splitlines():
        s = line.strip()
        if len(s) >= min_len:
            output.append({"string": s, "source": "rabin2", "offset": None})

    logging.info("Extracted %d strings via rabin2 from %s", len(output), file_path)
    return output

###################################################################################################

def dedupe(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Deduplicate strings while preserving first-seen order.
    """
    logging.info("Deduplicating %d string records.", len(records))
    seen: dict[str, dict] = {}
    order: list[str] = []
    duplicates = 0

    for r in records:
        key = r["string"]
        if key in seen:
            duplicates += 1
            
            # Prefer record with an offset if previous had none
            if not seen[key].get("offset") and r.get("offset"):
                seen[key] = r
        else:
            seen[key] = r
            order.append(key)

    result = [seen[k] for k in order]
    logging.info("Deduplication complete: %d -> %d (removed %d duplicates).", len(records), len(result), duplicates)
    return result

###################################################################################################
