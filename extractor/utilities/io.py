#     _____   ___    
#    |_   _|.'   `.  
#      | | /  .-.  \ 
#      | | | |   | | 
#     _| |_\  `-'  / 
#    |_____|`.___.'  
#                    

# ───────────────────────────────────────────────────────────────
# Standard library
import json
import logging
from pathlib import Path
from typing import Dict

###################################################################################################

# ================= Loaders =================
def load_static_info(extracted_dir: Path) -> dict:
    """
    Load static analysis info from a JSON file or from the first JSON in a directory.
    """
    if extracted_dir.is_file():
        logging.info("Loading static info from JSON file: %s", extracted_dir)
        try:
            return json.loads(extracted_dir.read_text(encoding="utf-8", errors="ignore"))
        except Exception as e:
            logging.error("Failed to parse JSON file %s: %s", extracted_dir, e)
            return {}

    if not extracted_dir.is_dir():
        logging.warning("Path is neither a file nor a directory: %s", extracted_dir)
        return {}

    logging.info("Searching for JSON files in directory: %s", extracted_dir)
    for candidate in extracted_dir.glob("*.json"):
        try:
            logging.debug("Trying JSON candidate: %s", candidate)
            return json.loads(candidate.read_text(encoding="utf-8", errors="ignore"))
        except Exception as e:
            logging.warning("Failed to parse JSON file %s: %s", candidate, e)

    logging.warning("No valid JSON file found in directory: %s", extracted_dir)
    return {}

###################################################################################################

# ================= I/O =================
def read_text_files(root: Path, exts=(".asm", ".c", ".txt", ".h")) -> dict[str, str]:
    """
    Recursively read text files with selected extensions into a path->content map.
    """
    texts: dict[str, str] = {}
    logging.info("Scanning directory %s for text files with extensions %s", root, exts)

    # Walk the tree and read files that match the allowed extensions
    for p in root.rglob("*"):
        if p.suffix.lower() in exts:
            try:
                texts[str(p)] = p.read_text(encoding="utf-8", errors="ignore")
                logging.debug("Loaded text file: %s", p)
            except Exception as e:
                logging.warning("Failed to read file %s: %s", p, e)

    logging.info("Collected %d text files from %s", len(texts), root)
    return texts

def write_json(path: Path, data: Dict) -> None:
    """
    Write a Python dict to pretty-printed UTF-8 JSON.
    """
    try:
        # Ensure parent directories exist
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        logging.info("JSON successfully written to %s", path)
    except Exception as e:
        logging.error("Failed to write JSON to %s: %s", path, e)

###################################################################################################
