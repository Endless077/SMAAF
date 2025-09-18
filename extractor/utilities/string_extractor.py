#      ______    _            _                    ________          _                         _                   
#    .' ____ \  / |_         (_)                  |_   __  |        / |_                      / |_                 
#    | (___ \_|`| |-'_ .--.  __   _ .--.   .--./)   | |_ \_| _   __`| |-'_ .--.  ,--.   .---.`| |-' .--.   _ .--.  
#     _.____`.  | | [ `/'`\][  | [ `.-. | / /'`\;   |  _| _ [ \ [  ]| | [ `/'`\]`'_\ : / /'`\]| | / .'`\ \[ `/'`\] 
#    | \____) | | |, | |     | |  | | | | \ \._//  _| |__/ | > '  < | |, | |    // | |,| \__. | |,| \__. | | |     
#     \______.' \__/[___]   [___][___||__].',__`  |________|[__]`\_]\__/[___]   \'-;__/'.___.'\__/ '.__.' [___]    
#                                        ( ( __))                                                                  

import re
import io
import sys
import logging
import subprocess
from pathlib import Path
from typing import List, Dict, Any

from floss.main import main as floss_call

###################################################################################################

# ================= Runner =================
def _run_cmd(cmd: list[str]) -> subprocess.CompletedProcess:
    """Run a subprocess command and return the completed process."""
    logging.debug("Executing command: %s", " ".join(cmd))
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
    if p.returncode != 0:
        logging.warning("Command exited with code %d: %s", p.returncode, " ".join(cmd))
        if p.stderr:
            logging.debug("Stderr from command: %s", p.stderr.strip()[:1000])
    else:
        logging.debug("Command succeeded: %s", " ".join(cmd))
    return p

###################################################################################################

# ================= Native =================
def strings_native(file_path: Path, min_len: int) -> List[Dict[str, Any]]:
    """Extract printable strings from a file using the system 'strings' command."""
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
    """Extract printable ASCII strings from a file in pure Python."""
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
    """Run FLOSS (flare-floss) via its Python API instead of subprocess."""
    logging.info("Running FLOSS via Python API on %s (min_len=%d).", file_path, min_len)

    # Cattura stdout di FLOSS
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        floss_call([str(file_path)])
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout

    out: list[dict[str, Any]] = []
    for l in output.splitlines():
        s = l.strip()
        if not s:
            continue
        addr = None
        if (m := re.match(r"^(0x[a-fA-F0-9]+|\d+):\s*(.+)$", s)):
            addr, s = m.group(1), m.group(2).strip()
        if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
            s = s[1:-1]
        if len(s) >= min_len:
            out.append({"string": s, "source": "floss", "offset": addr})

    logging.info("Extracted %d decoded strings via FLOSS from %s", len(out), file_path)
    return out

###################################################################################################

def dedupe(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Deduplicate strings while preserving first-seen order."""
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
