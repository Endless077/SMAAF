#      ______    _                                        
#    .' ____ \  / |_                                      
#    | (___ \_|`| |-' .--.   _ .--.  ,--.   .--./) .---.  
#     _.____`.  | | / .'`\ \[ `/'`\]`'_\ : / /'`\;/ /__\\ 
#    | \____) | | |,| \__. | | |    // | |,\ \._//| \__., 
#     \______.' \__/ '.__.' [___]   \'-;__/.',__`  '.__.' 
#                                         ( ( __))        

# Imports
from typing import List, Dict, Iterable, Callable, Optional, Any
import shutil

# Project Modules
from models import *
from metadata import *
from utilities import *

from sources.virustotal import VTClient
from sources.virustshare import VSClient
from sources.malwarebazaar import MBClient

from configs.config import settings

###################################################################################################

def extract_provider(sample: str | None = None, provider: str | None = None) -> dict:
    if not provider:
        raise ValueError("Parameter 'provider' is required.")

    provider_dir = os.path.join(settings.DOWNLOAD_DIR, provider)
    if not os.path.isdir(provider_dir):
        raise FileNotFoundError(f"Provider directory not found: {provider_dir}")

    targets_on_disk: List[str] = []
    if sample:
        candidate = os.path.join(provider_dir, sample)
        if not os.path.isfile(candidate):
            raise FileNotFoundError(f"Sample not found: {candidate}")
        targets_on_disk = [candidate]
    else:
        for name in os.listdir(provider_dir):
            if name.startswith("."):
                continue
            p = os.path.join(provider_dir, name)
            if os.path.isfile(p):
                targets_on_disk.append(p)
        if not targets_on_disk:
            raise FileNotFoundError(f"No samples to process in {provider_dir}")

    items: List[dict] = []
    errors: List[str] = []

    for disk_fp in targets_on_disk:
        tmpdir = None
        try:
            targets_to_process, tmpdir = gather_targets(disk_fp)

            for actual_fp in targets_to_process:
                original_name = os.path.basename(actual_fp)
                with open(actual_fp, "rb") as f:
                    content = f.read()

                meta_dict = metadata_extractor(original_name, content)
                file_meta = FileMetadata(**meta_dict)
                sha256 = file_meta.sha256

                file_path, metadata_path = build_paths(original_name, sha256)
                if not os.path.exists(file_path):
                    write_file(file_path, content)

                meta_item = MetadataItem(
                    id=sha256,
                    original_name=original_name,
                    stored_path=file_path,
                    metadata_path=metadata_path,
                    metadata=file_meta,
                    tags=[provider],
                    source=provider,
                    note=f"Extracted from {provider} samples - {original_name}",
                    upload_time=datetime.now(timezone.utc).isoformat(),
                )

                write_json(metadata_path, meta_item.model_dump())

                items.append(meta_item.model_dump())

        except Exception as e:
            errors.append(f"{os.path.basename(disk_fp)}: {e}")

        finally:
            if tmpdir and os.path.isdir(tmpdir):
                try:
                    shutil.rmtree(tmpdir)
                except Exception:
                    pass

    processed = len(items)
    success = processed > 0

    return {
        "sample": sample,
        "provider": provider,
        "items": items,
        "errors": errors,
        "processed": processed,
        "success": success,
    }

def query_provider(sample: Optional[str] = None, provider: Optional[str] = None) -> dict:
    try:
        if provider == "VirusTotal":
            client = VTClient()
            data = client.get_file_info(sample)
        elif provider == "VirusShare":
            client = VSClient()
            data = client.file_report(sample)
        elif provider == "MalwareBazaar":
            client = MBClient()
            data = client.get_info(sample)
        else:
            raise ValueError(f"Unsupported provider: {provider}")

        return {"results": data, "provider": provider, "sample": sample, "success": True}
    except Exception as e:
        raise e
    
def samples_provider(sample: str = None, provider: str = None) -> dict:
    results = []

    if provider:
        dirpath = settings.PROVIDER_DIR_MAP[provider]
        if not dirpath.exists():
            return {"results": [], "success": False}

        files = [
            f.name
            for f in dirpath.iterdir()
            if f.is_file() and (not sample or sample in f.name)
        ]
        if files:
            results.append({"provider": provider, "sample": sample, "files": files})

    else: 
        for prov, folder in settings.PROVIDER_DIR_MAP.items():
            dirpath = settings.DOWNLOAD_DIR / folder
            if not dirpath.exists():
                continue
            files = [
                f.name
                for f in dirpath.iterdir()
                if f.is_file() and (not sample or sample in f.name)
            ]
            if files:
                results.append({"provider": prov, "sample": sample, "files": files})

    return {"results": results, "success": bool(results)}

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

def list_all_files() -> List[Dict[str, Any]]:
    results: List[Dict[str, Any]] = []
    for p in iter_files(settings.SAMPLES_DIR):
        obj = read_json(p)
        if obj:
            results.append(obj)
    return results

def list_all_metadata() -> List[Dict[str, Any]]:
    results: List[Dict[str, Any]] = []
    for p in iter_jsons(settings.SAMPLES_DIR):
        obj = read_json(p)
        if obj:
            results.append(obj)
    return results

###################################################################################################7
