#     _____  _____  _    _   __    _   _    _                
#    |_   _||_   _|/ |_ (_) [  |  (_) / |_ (_)               
#      | |    | | `| |-'__   | |  __ `| |-'__  .---.  .--.   
#      | '    ' |  | | [  |  | | [  | | | [  |/ /__\\( (`\]  
#       \ \__/ /   | |, | |  | |  | | | |, | || \__., `'.'.  
#        `.__.'    \__/[___][___][___]\__/[___]'.__.'[\__) ) 
#                                                            

# Imports
import os
import json
from datetime import datetime
from typing import Tuple, Dict, Generator, Optional, Any

# Project Configs
from configs.config import Settings

###################################################################################################

# ================= Files =================
def iter_files() -> Generator[str, None, None]:
    if not os.path.isdir(Settings.SAMPLES_DIR):
        return
    for name in os.listdir(Settings.SAMPLES_DIR):
        path = os.path.join(Settings.SAMPLES_DIR, name)
        if os.path.isfile(path) and not name.lower().endswith(".json"):
            yield path

def iter_jsons() -> Generator[str, None, None]:
    if not os.path.isdir(Settings.SAMPLES_DIR):
        return
    for name in os.listdir(Settings.SAMPLES_DIR):
        if name.lower().endswith(".json"):
            yield os.path.join(Settings.SAMPLES_DIR, name)

def read_file(path: str) -> bytes | None:
    try:
        with open(path, "rb") as f:
            return f.read()
    except (IOError, OSError):
        return None
    
def read_json(path: str) -> Dict[str, Any] | None:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (IOError, OSError, json.JSONDecodeError):
        return None

def write_file(path: str, data: bytes) -> None:
    with open(path, "wb") as f:
        f.write(data)

def write_json(path: str, obj: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False, sort_keys=True)

###################################################################################################

# ================= Paths =================
def build_paths(filename: str, sha256: str) -> Tuple[str, str]:
    safe_name = "".join(c for c in filename if c.isalnum() or c in (".", "_", "-", " ")).strip()
    
    if not safe_name:
        safe_name = "sample.bin"
    
    fname = f"{sha256}_{safe_name}"
    file_path = os.path.join(Settings.SAMPLES_DIR, fname)
    meta_path = os.path.join(Settings.SAMPLES_DIR, f"{sha256}.json")
    return file_path, meta_path

###################################################################################################

# ================= Normalization =================
def norm_ext(ext: Optional[str]) -> Optional[str]:
    if not ext:
        return None
    e = ext.strip().casefold()
    if not e:
        return None
    return e if e.startswith(".") else f".{e}"

def norm_lower(s: Any) -> str:
    return str(s).strip().casefold() if s is not None else ""

def norm_upper(s: Any) -> str:
    return str(s).strip().upper() if s is not None else ""

def parse_iso(dt: Optional[str]) -> Optional[datetime]:
    if not dt:
        return None
    try:
        if dt.endswith("Z"):
            dt = dt[:-1] + "+00:00"
        return datetime.fromisoformat(dt)
    except Exception:
        return None

###################################################################################################
