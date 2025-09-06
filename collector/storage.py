#      ______    _                                        
#    .' ____ \  / |_                                      
#    | (___ \_|`| |-' .--.   _ .--.  ,--.   .--./) .---.  
#     _.____`.  | | / .'`\ \[ `/'`\]`'_\ : / /'`\;/ /__\\ 
#    | \____) | | |,| \__. | | |    // | |,\ \._//| \__., 
#     \______.' \__/ '.__.' [___]   \'-;__/.',__`  '.__.' 
#                                         ( ( __))        

import os
import json
from datetime import datetime
from typing import List, Dict, Tuple, Iterable, Generator, Optional, Any

SAMPLES_DIR = os.getenv("SAMPLES_DIR", "./samples")

###################################################################################################

def ensure_samples_dir() -> str:
    os.makedirs(SAMPLES_DIR, exist_ok=True)
    return SAMPLES_DIR

def build_sample_paths(sha256: str, original_name: str) -> Tuple[str, str]:
    safe_name = "".join(c for c in original_name if c.isalnum() or c in (".", "_", "-", " ")).strip()
    
    if not safe_name:
        safe_name = "sample.bin"
    
    fname = f"{sha256}_{safe_name}"
    file_path = os.path.join(SAMPLES_DIR, fname)
    meta_path = os.path.join(SAMPLES_DIR, f"{sha256}.json")
    return file_path, meta_path

def write_file(path: str, data: bytes) -> None:
    with open(path, "wb") as f:
        f.write(data)

def write_metadata(path: str, obj: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False, sort_keys=True)

###################################################################################################

def _iter_metadata_files() -> Generator[str, None, None]:
    if not os.path.isdir(SAMPLES_DIR):
        return
    for name in os.listdir(SAMPLES_DIR):
        if name.lower().endswith(".json"):
            yield os.path.join(SAMPLES_DIR, name)

def load_metadata_file(path: str) -> Dict[str, Any] | None:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def list_all_metadata() -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for p in _iter_metadata_files():
        obj = load_metadata_file(p)
        if obj:
            out.append(obj)
    return out

###################################################################################################

def _norm_ext(ext: Optional[str]) -> Optional[str]:
    if not ext:
        return None
    e = ext.strip().lower()
    if not e:
        return None
    return e if e.startswith(".") else f".{e}"

def looks_like_hex(s: str) -> bool:
    try:
        int(s, 16)
        return True
    except Exception:
        return False

def classify_hash(s: str) -> str | None:
    sl = len(s)
    s_lower = s.lower()
    if sl == 32 and looks_like_hex(s_lower): return "md5"
    if sl == 40 and looks_like_hex(s_lower): return "sha1"
    if sl == 64 and looks_like_hex(s_lower): return "sha256"
    return None

def search_metadata(query: str) -> List[Dict[str, Any]]:
    query = query.strip()
    kind = classify_hash(query)

    results: List[Dict[str, Any]] = []
    for obj in list_all_metadata():
        meta = obj.get("metadata", {})
        if kind:
            if meta.get(kind, "").lower() == query.lower():
                results.append(obj)
        else:
            if meta.get("filename") == query:
                results.append(obj)
    return results

def filter_metadata(
    objects: Iterable[Dict[str, Any]],
    tags: Optional[List[str]] = None,
    tags_mode: str = "any",
    source: Optional[str] = None,
    ext: Optional[str] = None,
    file_kind: Optional[str] = None,
    mime_contains: Optional[str] = None,
    min_size: Optional[int] = None,
    max_size: Optional[int] = None,
    since_iso: Optional[str] = None,
    until_iso: Optional[str] = None,
    has_providers: Optional[bool] = None
) -> List[Dict[str, Any]]:
    
    ext = _norm_ext(ext)
    src_norm = source.strip().lower() if source else None
    fk_norm  = file_kind.strip().upper() if file_kind else None
    mime_sub = mime_contains.strip().lower() if mime_contains else None
    tags_set = set([t.strip().lower() for t in (tags or []) if t and t.strip()])
    
    def parse_dt(s: Optional[str]) -> Optional[datetime]:
        if not s:
            return None
        try:
            if s.endswith("Z"):
                s = s[:-1] + "+00:00"
            return datetime.fromisoformat(s)
        except Exception:
            return None

    since_dt = parse_dt(since_iso)
    until_dt = parse_dt(until_iso)

    out: List[Dict[str, Any]] = []
    for obj in objects:
        meta: Dict[str, Any] = obj.get("metadata", {})
        
        # --- tags ---
        if tags_set:
            obj_tags = set([str(t).strip().lower() for t in (obj.get("tags") or [])])
            if tags_mode == "all":
                if not tags_set.issubset(obj_tags):
                    continue
            else:  # "any"
                if obj_tags.isdisjoint(tags_set):
                    continue

        # --- source ---
        if src_norm:
            if (obj.get("source") or "").strip().lower() != src_norm:
                continue

        # --- extension ---
        if ext:
            if (meta.get("ext") or "").strip().lower() != ext:
                continue

        # --- file_kind ---
        if fk_norm:
            if (meta.get("file_kind") or "").strip().upper() != fk_norm:
                continue

        # --- mime substring ---
        if mime_sub:
            mm = (meta.get("mime_magic") or "").strip().lower()
            if mime_sub not in mm:
                continue

        # --- size range ---
        size = int(meta.get("size_bytes") or 0)
        if min_size is not None and size < min_size:
            continue
        if max_size is not None and size > max_size:
            continue

        # --- date range on received_at (top-level, saved by server) ---
        ra = obj.get("received_at")
        ra_dt = parse_dt(ra)
        if since_dt and (ra_dt is None or ra_dt < since_dt):
            continue
        if until_dt and (ra_dt is None or ra_dt > until_dt):
            continue

        out.append(obj)

    return out
