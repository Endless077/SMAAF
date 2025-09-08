#      ______    _                                        
#    .' ____ \  / |_                                      
#    | (___ \_|`| |-' .--.   _ .--.  ,--.   .--./) .---.  
#     _.____`.  | | / .'`\ \[ `/'`\]`'_\ : / /'`\;/ /__\\ 
#    | \____) | | |,| \__. | | |    // | |,\ \._//| \__., 
#     \______.' \__/ '.__.' [___]   \'-;__/.',__`  '.__.' 
#                                         ( ( __))        

# Imports
from typing import List, Dict, Iterable, Callable, Generator, Optional, Any

# Project Modules
from metadata import *
from utilities import *

# Project Configs
from configs.config import Settings

###################################################################################################

def extract_provider(provider: str, sample: str) -> dict:
    return {"provider": provider, "sample": sample, "ok": True}

def query_provider(provider: str, sample: str) -> dict:
    return {"provider": provider, "sample": sample, "ok": True}

###################################################################################################

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
) -> List[Dict[str, Any]]:
    ext_norm   = norm_ext(ext)
    src_norm   = norm_lower(source)
    fk_norm    = norm_upper(file_kind)
    mime_sub   = norm_lower(mime_contains)
    tags_set   = {t.strip().casefold() for t in (tags or []) if t and t.strip()}
    since_dt   = parse_iso(since_iso)
    until_dt   = parse_iso(until_iso)

    if tags_mode not in {"any", "all"}:
        raise ValueError("tags_mode must be 'any' or 'all'")

    predicates: List[Callable[[Dict[str, Any]], bool]] = []

    # --- tags ---
    if tags_set:
        if tags_mode == "all":
            predicates.append(lambda obj: tags_set.issubset({norm_lower(t) for t in (obj.get("tags") or [])}))
        else:
            predicates.append(lambda obj: not set({*(norm_lower(t) for t in (obj.get("tags") or []))}).isdisjoint(tags_set))

    # --- source ---
    if src_norm:
        predicates.append(lambda obj: norm_lower(obj.get("source")) == src_norm)

    # --- extension ---
    if ext_norm:
        predicates.append(lambda obj: norm_lower((obj.get("metadata") or {}).get("ext")) == ext_norm)

    # --- file kind ---
    if fk_norm:
        predicates.append(lambda obj: norm_upper((obj.get("metadata") or {}).get("file_kind")) == fk_norm)

    # --- mime substring ---
    if mime_sub:
        predicates.append(lambda obj: mime_sub in norm_lower((obj.get("metadata") or {}).get("mime_magic")))

    # --- size range ---
    if min_size is not None:
        predicates.append(lambda obj: int((obj.get("metadata") or {}).get("size_bytes") or 0) >= min_size)
    if max_size is not None:
        predicates.append(lambda obj: int((obj.get("metadata") or {}).get("size_bytes") or 0) <= max_size)

    # --- datetime range ---
    if since_dt or until_dt:
        def _dt_ok(obj: Dict[str, Any]) -> bool:
            ra_dt = parse_iso(obj.get("upload_time"))
            if since_dt and (ra_dt is None or ra_dt < since_dt):
                return False
            if until_dt and (ra_dt is None or ra_dt > until_dt):
                return False
            return True
        predicates.append(_dt_ok)

    return [obj for obj in objects if all(pred(obj) for pred in predicates)]
       
def search_metadata(query: str) -> List[Dict[str, Any]]:
    query = query.strip()
    hash = classify_hash(query)

    results: List[Dict[str, Any]] = []
    for obj in list_all_metadata():
        meta = obj.get("metadata", {})
        if hash:
            if meta.get(hash, "").lower() == query.lower():
                results.append(obj)
        else:
            if meta.get("filename") == query:
                results.append(obj)

    return results

def list_all_metadata() -> List[Dict[str, Any]]:
    results: List[Dict[str, Any]] = []
    for p in iter_metadata():
        obj = read_metadata(p)
        if obj:
            results.append(obj)
    return results

###################################################################################################7
