#     ____  ____                       ________                   _                  
#    |_  _||_  _|                     |_   __  |                 (_)                 
#      \ \  / / ,--.   _ .--.  ,--.     | |_ \_| _ .--.   .--./) __   _ .--.  .---.  
#       \ \/ / `'_\ : [ `/'`\]`'_\ :    |  _| _ [ `.-. | / /'`\;[  | [ `.-. |/ /__\\ 
#       _|  |_ // | |, | |    // | |,  _| |__/ | | | | | \ \._// | |  | | | || \__., 
#      |______|\'-;__/[___]   \'-;__/ |________|[___||__].',__` [___][___||__]'.__.' 
#                                                       ( ( __))                     

from typing import List, Dict, Any, Optional
from pathlib import Path
import binascii
import logging
import yara

###################################################################################################

# ================= Helpers =================
def _hex_preview(b: bytes, max_bytes: int = 64) -> str:
    """Return a hexadecimal preview of the data for debugging/triage purposes."""
    h = binascii.hexlify(b[:max_bytes]).decode("ascii")
    if len(b) > max_bytes:
        h += "…"
    return h

def _safe_ascii(b: bytes, max_len: int = 200) -> str:
    """Return a best-effort ASCII preview, replacing non-printable characters."""
    s = b.decode("utf-8", errors="replace")
    return (s[:max_len] + "…") if len(s) > max_len else s

def _serialize_match(m: yara.Match, *, max_strings: int = 25, max_ascii_len: int = 200, max_hex_bytes: int = 64) -> Dict[str, Any]:
    """Serialize a yara.Match object including its matched strings with offset, identifier, and data previews."""
    serialization: Dict[str, Any] = {
        "rule": m.rule,
        "tags": list(m.tags),
        "meta": dict(m.meta) if m.meta else {},
        "strings": []
    }
    
    # Lightweight deduplication by (offset, identifier, data prefix)
    # and enforce a maximum number of strings.
    seen = set()
    for off, ident, data in m.strings:
        key = (off, ident, data[:64]) 
        if key in seen:
            continue
        seen.add(key)

        serialization["strings"].append({
            "offset": off,
            "identifier": ident,
            "ascii": _safe_ascii(data, max_ascii_len),
            "hex": _hex_preview(data, max_hex_bytes),
            "length": len(data),
        })

        if len(serialization["strings"]) >= max_strings:
            serialization["strings"].append({"note": f"truncated at {max_strings} strings"})
            break

    return serialization

###################################################################################################

# ================= Rules Compiler =================
def compile_dir(yara_dir: Optional[Path]) -> Optional[yara.Rules]:
    """Compile all YARA rules in a directory (recursively)."""
    if not yara_dir:
        logging.warning("No YARA directory provided")
        return None
    if not yara_dir.exists():
        logging.warning("YARA directory does not exist: %s", yara_dir)
        return None

    logging.info("Scanning for YARA files in %s", yara_dir)
    filepaths = {}
    for idx, f in enumerate(sorted(yara_dir.rglob("*"))):
        if f.suffix.lower() in {".yar", ".yara"}:
            filepaths[f"r{idx}"] = str(f)

    if not filepaths:
        logging.warning("No YARA files found in %s", yara_dir)
        return None

    logging.info("Compiling %d YARA files", len(filepaths))
    try:
        rules = yara.compile(filepaths=filepaths)
        logging.info("YARA compilation succeeded.")
        return rules
    except Exception as e:
        logging.error("YARA compilation failed: %s", e)
        return None

###################################################################################################

# ================= Scanners =================
def scan_file(ruleset: yara.Rules, target: Path, *, max_strings: int = 25) -> List[Dict[str, Any]]:
    """Scan a file with a given YARA ruleset. Include dettagli delle stringhe matchate."""
    logging.info("Scanning file with YARA: %s", target)
    out: list[dict[str, Any]] = []
    try:
        for m in ruleset.match(str(target)):
            out.append(_serialize_match(m, max_strings=max_strings))
        logging.info("YARA file scan complete: %d matches in %s", len(out), target)
    except Exception as e:
        logging.warning("YARA file scan failed for %s: %s", target, e)
    return out

def scan_text(ruleset: yara.Rules, text: str, *, max_strings: int = 25) -> List[Dict[str, Any]]:
    """Scan a text string with a given YARA ruleset. Include dettagli delle stringhe matchate."""
    logging.info("Scanning text buffer with YARA (size=%d chars).", len(text))
    out: list[dict[str, Any]] = []
    try:
        for m in ruleset.match(data=text):
            out.append(_serialize_match(m, max_strings=max_strings))
        logging.info("YARA text scan complete: %d matches", len(out))
    except Exception as e:
        logging.warning("YARA text scan failed: %s", e)
    return out

###################################################################################################
