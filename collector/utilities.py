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
    """Iterate over files in a directory, excluding JSON files."""
    if not os.path.isdir(dir):
        return None
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        # Yield only regular files that are not JSON
        if os.path.isfile(path) and not name.lower().endswith(".json"):
            yield path

def iter_jsons(dir: str) -> Generator[str, None, None]:
    """Iterate over JSON files in a directory."""
    if not os.path.isdir(dir):
        return None
    for name in os.listdir(dir):
        # Yield only files ending with .json
        if name.lower().endswith(".json"):
            yield os.path.join(dir, name)

def iter_all(dir: str) -> Generator[str, None, None]:
    """Iterate over all entries (files + dirs) in a directory."""
    if not os.path.isdir(dir):
        return None
    for name in os.listdir(dir):
        yield os.path.join(dir, name)

def read_file(path: str) -> bytes | None:
    """Read a file in binary mode, return None on failure."""
    try:
        with open(path, "rb") as f:
            return f.read()
    except (IOError, OSError):
        return None
    
def read_json(path: str) -> Dict[str, Any] | None:
    """Read a JSON file, return parsed dict or None on error."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (IOError, OSError, json.JSONDecodeError):
        return None

def write_file(path: str, data: bytes) -> None:
    """Write raw bytes to a file."""
    with open(path, "wb") as f:
        f.write(data)

def write_json(path: str, obj: dict) -> None:
    """Write a JSON object to a file with formatting."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False, sort_keys=True)

###################################################################################################

# ================= Archives =================
def extract_zip(zip_path: str, password: str = "infected") -> Tuple[str, List[str]]:
    """Extract files from a password-protected ZIP archive into a temp dir."""
    if not zipfile.is_zipfile(zip_path):
        raise ValueError(f"Not a zip file: {zip_path}")

    # Create temporary directory for extracted files
    tmpdir = tempfile.mkdtemp(prefix="provider_extract_")
    extracted_paths: List[str] = []

    with zipfile.ZipFile(zip_path, "r") as zf:
        for member in zf.namelist():
            # Skip directories inside the archive
            if member.endswith("/"):
                continue
            try:
                # Extract file content using password
                content = zf.read(member, pwd=password.encode("utf-8"))
            except RuntimeError as re:
                raise RuntimeError(f"Failed to read '{member}' from zip: {re}")
            except zipfile.BadZipFile as bz:
                raise RuntimeError(f"Bad zip member '{member}': {bz}")

            # Ensure safe filename and avoid overwriting existing files
            safe_name = os.path.basename(member) or "extracted_file"
            out_path = os.path.join(tmpdir, safe_name)
            if os.path.exists(out_path):
                base, ext = os.path.splitext(safe_name)
                idx = 1
                while os.path.exists(os.path.join(tmpdir, f"{base}_{idx}{ext}")):
                    idx += 1
                out_path = os.path.join(tmpdir, f"{base}_{idx}{ext}")

            # Write extracted file to disk
            with open(out_path, "wb") as out_f:
                out_f.write(content)

            extracted_paths.append(out_path)

    return tmpdir, extracted_paths

###################################################################################################

# ================= Paths =================
def build_paths(filename: str, sha256: str) -> Tuple[str, str]:
    """Build safe storage paths for a sample and its metadata."""
    # Sanitize filename to avoid unsafe characters
    safe_name = "".join(c for c in filename if c.isalnum() or c in (".", "_", "-", " ")).strip()
    
    if not safe_name:
        safe_name = "sample.bin"
    
    # File path contains hash + original safe filename
    fname = f"{sha256}_{safe_name}"
    file_path = os.path.join(Settings.SAMPLES_DIR, fname)
    # Metadata path is always <sha256>.json
    meta_path = os.path.join(Settings.SAMPLES_DIR, f"{sha256}.json")
    return file_path, meta_path

def gather_targets(file_path: str) -> Tuple[List[str], Optional[str]]:
    """Gather files to process: single file or extracted ZIP content."""
    if zipfile.is_zipfile(file_path):
        tmpdir, extracted = extract_zip(file_path, password="infected")
        return extracted, tmpdir
    return [file_path], None

###################################################################################################

# ================= Normalization =================
def norm_ext(ext: Optional[str]) -> Optional[str]:
    """Normalize extension to lowercase, prefixed with a dot."""
    if not ext:
        return None
    e = ext.strip().casefold()
    if not e:
        return None
    return e if e.startswith(".") else f".{e}"

def norm_lower(s: Any) -> str:
    """Normalize string to lowercase."""
    return str(s).strip().casefold() if s is not None else ""

def norm_upper(s: Any) -> str:
    """Normalize string to uppercase."""
    return str(s).strip().upper() if s is not None else ""

def parse_iso(dt: Optional[str]) -> Optional[datetime]:
    """Parse ISO 8601 datetime string, return None on failure."""
    if not dt:
        return None
    try:
        # Replace trailing Z with +00:00 for UTC
        if dt.endswith("Z"):
            dt = dt[:-1] + "+00:00"
        return datetime.fromisoformat(dt)
    except Exception:
        return None

###################################################################################################
