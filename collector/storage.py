# storage.py
import os
import json
from datetime import datetime
from typing import Tuple

SAMPLES_DIR = os.getenv("SAMPLES_DIR", "./samples")


def ensure_samples_dir() -> str:
    """Make sure samples directory exists."""
    os.makedirs(SAMPLES_DIR, exist_ok=True)
    return SAMPLES_DIR


def build_sample_paths(sha256: str, original_name: str) -> Tuple[str, str]:
    """
    Return (file_path, metadata_path).
    File:     samples/<sha256>_<sanitized_name>
    Metadata: samples/<sha256>.json
    """
    safe_name = "".join(c for c in original_name if c.isalnum() or c in (".", "_", "-", " ")).strip()
    if not safe_name:
        safe_name = "sample.bin"
    fname = f"{sha256}_{safe_name}"
    file_path = os.path.join(SAMPLES_DIR, fname)
    meta_path = os.path.join(SAMPLES_DIR, f"{sha256}.json")
    return file_path, meta_path


def write_file(path: str, data: bytes) -> None:
    """Persist raw bytes to disk."""
    with open(path, "wb") as f:
        f.write(data)


def write_metadata(path: str, obj: dict) -> None:
    """Persist metadata as JSON."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False, sort_keys=True)


# storage.py (aggiunte)
import os
import json
from typing import Dict, Any, Generator, List

def _iter_metadata_files() -> Generator[str, None, None]:
    """Yield absolute paths of all metadata JSON files under SAMPLES_DIR."""
    if not os.path.isdir(SAMPLES_DIR):
        return
    for name in os.listdir(SAMPLES_DIR):
        if name.lower().endswith(".json"):
            yield os.path.join(SAMPLES_DIR, name)

def load_metadata_file(path: str) -> Dict[str, Any] | None:
    """Load a single metadata JSON; returns None on errors."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def list_all_metadata() -> List[Dict[str, Any]]:
    """Return all stored metadata objects found in SAMPLES_DIR."""
    out: List[Dict[str, Any]] = []
    for p in _iter_metadata_files():
        obj = load_metadata_file(p)
        if obj:
            out.append(obj)
    return out

def looks_like_hex(s: str) -> bool:
    try:
        int(s, 16)
        return True
    except Exception:
        return False

def classify_hash(s: str) -> str | None:
    """Return 'sha256' | 'sha1' | 'md5' if length & hex match, otherwise None."""
    sl = len(s)
    s_lower = s.lower()
    if sl == 64 and looks_like_hex(s_lower): return "sha256"
    if sl == 40 and looks_like_hex(s_lower): return "sha1"
    if sl == 32 and looks_like_hex(s_lower): return "md5"
    return None

def search_metadata(q: str) -> List[Dict[str, Any]]:
    """
    Search by:
      - hash (sha256/sha1/md5) exact match
      - filename exact match (metadata['metadata']['filename'])
    Returns a list (filename could have multiple matches).
    """
    q = q.strip()
    kind = classify_hash(q)

    results: List[Dict[str, Any]] = []
    for obj in list_all_metadata():
        meta = obj.get("metadata", {})
        if kind:
            # hash match
            if meta.get(kind, "").lower() == q.lower():
                results.append(obj)
        else:
            # filename exact match (case-sensitive by default; change if desired)
            if meta.get("filename") == q:
                results.append(obj)
    return results

# storage.py (new code to add)
from typing import Iterable, Optional, List, Dict, Any
from datetime import datetime

def _norm_ext(ext: Optional[str]) -> Optional[str]:
    if not ext:
        return None
    e = ext.strip().lower()
    if not e:
        return None
    return e if e.startswith(".") else f".{e}"

def filter_metadata(
    objects: Iterable[Dict[str, Any]],
    tags: Optional[List[str]] = None,
    tags_mode: str = "any",              # "any" or "all"
    source: Optional[str] = None,
    ext: Optional[str] = None,
    file_kind: Optional[str] = None,     # PE | ELF | MACHO | UNKNOWN
    mime_contains: Optional[str] = None, # substring check on metadata.mime_magic
    min_size: Optional[int] = None,      # bytes
    max_size: Optional[int] = None,      # bytes
    since_iso: Optional[str] = None,     # filter by received_at >= since
    until_iso: Optional[str] = None,     # filter by received_at <= until
    has_providers: Optional[bool] = None # True: at least 1 provider; False: none
) -> List[Dict[str, Any]]:
    """
    Apply AND-combined filters over the stored metadata objects.
    Every filter is optional; omitted filters are ignored.
    """
    ext = _norm_ext(ext)
    tags_set = set([t.strip().lower() for t in (tags or []) if t and t.strip()])
    src_norm = source.strip().lower() if source else None
    fk_norm  = file_kind.strip().upper() if file_kind else None
    mime_sub = mime_contains.strip().lower() if mime_contains else None

    def parse_dt(s: Optional[str]) -> Optional[datetime]:
        if not s:
            return None
        try:
            # Accept both with 'Z' and with timezone offset
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

        # --- providers presence ---
        if has_providers is not None:
            providers = (meta.get("external_providers") or {})
            if has_providers and not providers:
                continue
            if (has_providers is False) and providers:
                continue

        out.append(obj)

    return out
