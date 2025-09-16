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
import zipfile
import tempfile
from datetime import datetime
from typing import List, Tuple, Dict, Generator, Optional, Any

# Project Configs
from configs.config import Settings

###################################################################################################

# ================= Files =================
def iter_files(dir) -> Generator[str, None, None]:
    if not os.path.isdir(dir):
        return None
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path) and not name.lower().endswith(".json"):
            yield path

def iter_jsons(dir: str) -> Generator[str, None, None]:
    if not os.path.isdir(dir):
        return None
    for name in os.listdir(dir):
        if name.lower().endswith(".json"):
            yield os.path.join(dir, name)

def iter_all(dir: str) -> Generator[str, None, None]:
    if not os.path.isdir(dir):
        return None
    for name in os.listdir(dir):
        yield os.path.join(dir, name)

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

# ================= Archives =================
def extract_zip(zip_path: str, password: str = "infected") -> Tuple[str, List[str]]:
    if not zipfile.is_zipfile(zip_path):
        raise ValueError(f"Not a zip file: {zip_path}")

    tmpdir = tempfile.mkdtemp(prefix="provider_extract_")
    extracted_paths: List[str] = []

    with zipfile.ZipFile(zip_path, "r") as zf:
        for member in zf.namelist():
            if member.endswith("/"):
                continue
            try:
                content = zf.read(member, pwd=password.encode("utf-8"))
            except RuntimeError as re:
                raise RuntimeError(f"Failed to read '{member}' from zip: {re}")
            except zipfile.BadZipFile as bz:
                raise RuntimeError(f"Bad zip member '{member}': {bz}")

            safe_name = os.path.basename(member) or "extracted_file"
            out_path = os.path.join(tmpdir, safe_name)
            if os.path.exists(out_path):
                base, ext = os.path.splitext(safe_name)
                idx = 1
                while os.path.exists(os.path.join(tmpdir, f"{base}_{idx}{ext}")):
                    idx += 1
                out_path = os.path.join(tmpdir, f"{base}_{idx}{ext}")

            with open(out_path, "wb") as out_f:
                out_f.write(content)

            extracted_paths.append(out_path)

    return tmpdir, extracted_paths

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

def gather_targets(file_path: str) -> Tuple[List[str], Optional[str]]:
    if zipfile.is_zipfile(file_path):
        tmpdir, extracted = extract_zip(file_path, password="infected")
        return extracted, tmpdir
    return [file_path], None

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
