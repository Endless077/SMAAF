#     ____  ____                       ________                   _                  
#    |_  _||_  _|                     |_   __  |                 (_)                 
#      \ \  / / ,--.   _ .--.  ,--.     | |_ \_| _ .--.   .--./) __   _ .--.  .---.  
#       \ \/ / `'_\ : [ `/'`\]`'_\ :    |  _| _ [ `.-. | / /'`\;[  | [ `.-. |/ /__\\ 
#       _|  |_ // | |, | |    // | |,  _| |__/ | | | | | \ \._// | |  | | | || \__., 
#      |______|\'-;__/[___]   \'-;__/ |________|[___||__].',__` [___][___||__]'.__.' 
#                                                       ( ( __))                     

# ───────────────────────────────────────────────────────────────
# Third-party libraries
import yara

# ───────────────────────────────────────────────────────────────
# Standard library
import binascii
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

###################################################################################################

# ================= Helpers =================
def _hex_preview(b: bytes, max_bytes: int = 64) -> str:
    """
    Return a hexadecimal preview of the data for debugging/triage purposes.
    """
    h = binascii.hexlify(b[:max_bytes]).decode("ascii")
    if len(b) > max_bytes:
        h += "…"
    return h

def _safe_ascii(b: bytes, max_len: int = 200) -> str:
    """
    Return a best-effort ASCII preview, replacing non-printable characters.
    """
    s = b.decode("utf-8", errors="replace")
    return (s[:max_len] + "…") if len(s) > max_len else s

def _serialize_match(m: yara.Match, *, max_strings: int = 25, max_ascii_len: int = 200, max_hex_bytes: int = 64) -> Dict[str, Any]:
    """
    Serialize a yara.Match object including its matched strings with offset, identifier, and data previews.
    """
    serialization: Dict[str, Any] = {
        "rule": m.rule,
        "namespace": getattr(m, "namespace", None),
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
def compile_path(path: Union[str, Path]) -> Optional[yara.Rules]:
    """
    Compile YARA rules from:
      - a single rules file in YARA format (.yar)
      - a directory: if index exists in root, compile only that, otherwise recursively compile all .yar files.

    Returns yara.Rules or None on failure.
    """
    p = Path(path) if not isinstance(path, Path) else path
    
    if not p.exists():
        logging.warning("File/Directory not found: %s", p)
        return None

    try:
        if p.is_file() and p.suffix.lower() in {".yar"}:
            # File case (index.yar)
            logging.info("Compiling YARA from file: %s", p)
            return yara.compile(filepath=str(p), includes=True)

        if p.is_dir():
            # Directory
            index_candidates = [p / "index.yar"]
            for idx in index_candidates:
                if idx.exists():
                    logging.info("Found YARA index: %s (compiling only this file).", idx)
                    return yara.compile(filepath=str(idx), includes=True)

            # No index: compile all .yar recursively
            logging.info("No index found. Compiling all .yar in %s recursively.", p)
            filepaths = {}
            for i, f in enumerate(sorted(p.rglob("*"))):
                if f.suffix.lower() in {".yar"}:
                    # simple namespace
                    ns = f"r{i}"
                    filepaths[ns] = str(f)
            if not filepaths:
                logging.warning("YARA files not found: %s", p)
                return None
            return yara.compile(filepaths=filepaths, includes=True)

        logging.warning("Path is neither YARA file nor directory: %s", p)
        return None

    except yara.SyntaxError as e:
        logging.error("YARA Syntax Error: %s", e)
        logging.warning("Skipping invalid YARA file due to syntax error.")
        return None
    
    except Exception as e:
        logging.error("YARA compilation failed: %s", e)
        return None

###################################################################################################

# ================= Scanners =================
def scan_file(ruleset: yara.Rules, target: Path, *, max_strings: int = 25, timeout: int = 10) -> List[Dict[str, Any]]:
    """
    Scan a file with a given YARA ruleset. Includes details about the string match.
    """
    try:
        time = max(1, int(timeout))
    except Exception:
        time = 10

    logging.info("Scanning file with YARA: %s (timeout=%ds)", target, time)

    output: List[Dict[str, Any]] = []
    
    if ruleset is None:
        logging.debug("No YARA ruleset provided, skipping file scan.")
        return output

    try:
        for m in ruleset.match(filepath=str(target), timeout=time):
            output.append(_serialize_match(m, max_strings=max_strings))
        logging.info("YARA file scan complete: %d matches in %s", len(output), target)
    except yara.TimeoutError:
        logging.warning("YARA timeout on file: %s (timeout=%ds).", target, time)
    except TypeError as e:
        logging.warning("YARA file scan failed for %s: %s", target, e)
    except Exception as e:
        logging.warning("YARA file scan failed for %s: %s", target, e)
    return output

def scan_text(ruleset: yara.Rules, text: str, *, max_strings: int = 25, timeout: int = 10) -> List[Dict[str, Any]]:
    """
    Scan a text string with a given YARA ruleset. Includes details about the string match.
    """
    logging.info("Scanning text buffer with YARA (size=%d chars, timeout=%ds).", len(text), int(timeout))
    output: List[Dict[str, Any]] = []
    
    try:
        data = text.encode("utf-8", errors="ignore")
        time = int(timeout)
        for m in ruleset.match(data=data, timeout=time):
            output.append(_serialize_match(m, max_strings=max_strings))
        logging.info("YARA text scan complete: %d matches.", len(output))
    except yara.TimeoutError:
        logging.warning("YARA timeout on text buffer (timeout=%ds).", int(timeout))
    except TypeError as e:
        logging.warning("YARA text scan failed: %s", e)
    except Exception as e:
        logging.warning("YARA text scan failed: %s", e)
    return output

###################################################################################################
