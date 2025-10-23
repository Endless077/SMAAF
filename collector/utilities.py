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
import pyzipper
import tempfile

import shlex
import shutil
import subprocess

from datetime import datetime
from typing import List, Tuple, Dict, Generator, Optional, Any

# Project Configs
from collector.configs.config import Settings

###################################################################################################

# ================= Files =================
def iter_files(dir) -> Generator[str, None, None]:
    """
    Iterate over files in a directory, excluding JSON files.
    """
    if not os.path.isdir(dir):
        return None
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        # Yield only regular files that are not JSON
        if os.path.isfile(path) and not name.lower().endswith(".json"):
            yield path

def iter_jsons(dir: str) -> Generator[str, None, None]:
    """
    Iterate over JSON files in a directory.
    """
    if not os.path.isdir(dir):
        return None
    for name in os.listdir(dir):
        # Yield only files ending with .json
        if name.lower().endswith(".json"):
            yield os.path.join(dir, name)

def iter_all(dir: str) -> Generator[str, None, None]:
    """
    Iterate over all entries (files + dirs) in a directory.
    """
    if not os.path.isdir(dir):
        return None
    for name in os.listdir(dir):
        yield os.path.join(dir, name)

def read_file(path: str) -> bytes | None:
    """
    Read a file in binary mode, return None on failure.
    """
    try:
        with open(path, "rb") as f:
            return f.read()
    except (IOError, OSError):
        return None
    
def read_json(path: str) -> Dict[str, Any] | None:
    """
    Read a JSON file, return parsed dict or None on error.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (IOError, OSError, json.JSONDecodeError):
        return None

def write_file(path: str, data: bytes) -> None:
    """
    Write raw bytes to a file.
    """
    with open(path, "wb") as f:
        f.write(data)

def write_json(path: str, obj: dict) -> None:
    """
    Write a JSON object to a file with formatting.
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)

###################################################################################################

# ================= Archives =================
def extract_zip(zip_path: str, password: str = "infected") -> Tuple[str, List[str]]:
    """
    Extract files from a ZIP archive (including password-protected ones)
    with maximum compatibility.
    """
     # Validate input path
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"ZIP file not found: {zip_path}")

    # Create a temporary working directory for extracted files
    tmpdir = tempfile.mkdtemp(prefix="provider_extract_")
    extracted_paths: List[str] = []

    # pyzipper (supports AES, Deflate64, and encrypted ZIPs)
    try:
        with pyzipper.AESZipFile(zip_path, "r") as zf:
            # Configure password for encrypted archives
            zf.pwd = password.encode("utf-8")

            # Iterate through ZIP members and extract files
            for member in zf.namelist():
                # Skip directory entries
                if member.endswith("/"):
                    continue
                
                try:
                    # Read the file content into memory
                    content = zf.read(member)
                except RuntimeError as e:
                    shutil.rmtree(tmpdir, ignore_errors=True)
                    raise RuntimeError(f"Incorrect password for '{os.path.basename(zip_path)}'") from e
                
                # Generate a safe filename to prevent path traversal
                safe_name = os.path.basename(member) or "extracted.bin"
                out_path = os.path.join(tmpdir, safe_name)

                # Write extracted file to the temp directory
                with open(out_path, "wb") as out_f:
                    out_f.write(content)
                
                extracted_paths.append(out_path)

        # If extraction succeeded with pyzipper, return early
        if extracted_paths:
            return tmpdir, extracted_paths

    except RuntimeError as e:
        # Incorrect Passowrd followup
        # rise, unzip interrupted.
        raise e
    
    except Exception as e:
        # pyzipper failure, fallback
        # to system wide solution
        pass

    # 7-Zip external tool (massive compatibility)
    try:
        # Build the 7z command for silent extraction
        cmd = f'7z x -p{password} -o"{tmpdir}" "{zip_path}" -y'

        # Run 7z via subprocess to avoid shell injection risks
        subprocess.run(
            shlex.split(cmd),
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        # Collect all extracted files from the temporary directory
        for root, _, files in os.walk(tmpdir):
            for f in files:
                extracted_paths.append(os.path.join(root, f))

        # Verify that at least one file was successfully extracted
        if not extracted_paths:
            shutil.rmtree(tmpdir, ignore_errors=True)
            raise RuntimeError("7z extracted no files.")

        return tmpdir, extracted_paths

    except FileNotFoundError:
        shutil.rmtree(tmpdir, ignore_errors=True)
        raise RuntimeError("Extraction failed: '7z' not found.")
    except subprocess.CalledProcessError as e:
        shutil.rmtree(tmpdir, ignore_errors=True)
        raise RuntimeError(f"7z returned an error during extraction: {e}")

###################################################################################################

# ================= Paths =================
def build_paths(filename: str, sha256: str, relative: bool = True) -> Tuple[str, str]:
    """
    Build safe storage paths for a sample and its metadata.
    """
    # Sanitize filename to avoid unsafe characters
    safe_name = "".join(c for c in filename if c.isalnum() or c in (".", "_", "-", " ")).strip()
    if not safe_name:
        safe_name = "sample.bin"

    # Compose safe filenames
    fname = f"{sha256}_{safe_name}"
    file_path = os.path.join(Settings.SAMPLES_DIR, fname)
    meta_path = os.path.join(Settings.SAMPLES_DIR, f"{sha256}.json")

    if relative:
        # Convert absolute paths to relative ones, relative to the project root
        base_dir = os.path.dirname(Settings.SAMPLES_DIR)
        file_path = os.path.relpath(file_path, base_dir)
        meta_path = os.path.relpath(meta_path, base_dir)

    return file_path, meta_path

def gather_targets(file_path: str) -> Tuple[List[str], Optional[str]]:
    """
    Gather files to process: single file or extracted ZIP content.
    """
    if zipfile.is_zipfile(file_path):
        tmpdir, extracted = extract_zip(file_path, password="infected")
        return extracted, tmpdir
    return [file_path], None

###################################################################################################

# ================= Normalization =================
def norm_ext(ext: Optional[str]) -> Optional[str]:
    """
    Normalize extension to lowercase, prefixed with a dot.
    """
    if not ext:
        return None
    e = ext.strip().casefold()
    if not e:
        return None
    return e if e.startswith(".") else f".{e}"

def norm_lower(s: Any) -> str:
    """
    Normalize string to lowercase.
    """
    return str(s).strip().casefold() if s is not None else ""

def norm_upper(s: Any) -> str:
    """
    Normalize string to uppercase.
    """
    return str(s).strip().upper() if s is not None else ""

def parse_iso(dt: Optional[str]) -> Optional[datetime]:
    """
    Parse ISO 8601 datetime string, return None on failure.
    """
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
