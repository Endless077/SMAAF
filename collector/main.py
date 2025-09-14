#     ________               _        _       _______  _____  
#    |_   __  |             / |_     / \     |_   __ \|_   _| 
#      | |_ \_|,--.   .--. `| |-'   / _ \      | |__) | | |   
#      |  _|  `'_\ : ( (`\] | |    / ___ \     |  ___/  | |   
#     _| |_   // | |, `'.'. | |, _/ /   \ \_  _| |_    _| |_  
#    |_____|  \'-;__/[\__) )\__/|____| |____||_____|  |_____| 
#                                                             

# Imports
import os
import sys
import signal
from datetime import datetime, timezone

# Server
import uvicorn

from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi import File, Form, Query, Body, UploadFile

from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

# Providers Endpoints
from sources.endpoints.endpoints_vt import *
from sources.endpoints.endpoints_vs import *
from sources.endpoints.endpoints_mb import *

# Project Stuffs
from models import *
from storage import *
from utilities import *

from utils.logger import get_logging
LOG_SYS = get_logging()

###################################################################################################

# To Run: uvicorn main:app --host 127.0.0.1 --port 8080 --reload
# To Run: uvicorn main:app --host 127.0.0.1 --port 8080

TAG = "FastAPI"

app = FastAPI(title="FastAPI - Malware Collector",
              summary="Some easy API for a Malware Collector.",
              description="A simple and fast api suite for a malware collector (Static Malware Analysis).",
              contact={
                  "email": "antonio.garofalo125@gmail.com",
                  "name": "Antonio Garofalo",
                  "url": "https://github.com/Endless077"
              },
              terms_of_service="http://example.com/terms/",
              license_info={
                  "identifier": "GNU",
                  "name": "GNU General Public License v3",
                  "url": "https://opensource.org/license/gpl-3-0/"
              },
              version="1.0"
              )

origins = [
    "http://127.0.0.1",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

###################################################################################################

@app.post("/upload", response_model=UploadResponse, status_code=201, tags=["Upload"],
    summary="Upload a sample and persist metadata.",
    description=("Accepts a file (multipart/form-data) and stores it under /samples with a JSON metadata file.")
)
async def upload(
    file: UploadFile = File(..., description="The file to upload."),
    source: str | None = Form(default=None, description="Source where file come from."),
    tags: list[str] | None = Form(default=None, description="Some tags about the file."),
    note: str | None = Form(default=None, description="Some notes about the file.")
):

    try:
        # Extract the metadata
        content = await file.read()
        meta_dict = metadata_extractor(file.filename, content)

        # Build FileMetadata Pydantic object
        metadata = FileMetadata(**meta_dict)

        # Paths
        sha256 = metadata.sha256
        file_path, metadata_path = build_paths(file.filename, sha256)

        # Persist sample
        if not os.path.exists(file_path):
            write_file(file_path, content)

        # Persist metadata JSON
        meta_obj = {
            "id": sha256,
            "stored_path": file_path,
            "metadata_path": metadata_path,
            "metadata": metadata.model_dump(),
            "tags": tags,
            "source": source,
            "note": note,
            "upload_time": datetime.now(timezone.utc).isoformat()
        }

        write_json(metadata_path, meta_obj)

        LOG_SYS.write(TAG, f"New sample stored: {file_path}")

        return UploadResponse(
            id=sha256,
            stored_path=file_path,
            metadata_path=metadata_path,
            metadata=metadata,
            tags=tags,
            source=source,
            note=note,
            upload_time=datetime.now(timezone.utc).isoformat()
        )

    except Exception as e:
        LOG_SYS.write(TAG, f"Upload error: {e}")
        raise HTTPException(status_code=500, detail=f"Upload failed: {e}")

@app.get("/metadata/search", response_model=SearchResponse, status_code=200, tags=["Metadata"],
    summary="Search metadata by filename or hash, with optional filters (or list all)",
    description=(
        "This query applies optional filters if provided by the user (all filters are AND-combined).\n"
        "If `query` is provided and looks like a hash, match by hash; otherwise match exact filename.\n"
        "If `query` is omitted, process a big get query from the samples directory with all metadata."
    ),
)
async def metadata_search(
    query: Optional[str] = Query(None, description="Leave empty to list all (filename OR hash (md5/sha1/sha256)."),
    
    tags: Optional[List[str]] = Query(None, description="Repeatable tag filter (?tags=...&tags=...)."),
    tags_mode: str = Query("any", pattern="^(any|all)$", description="Provide a tags AND/OR query."),
    source: Optional[str] = Query(None, description="Exact source match (case-insensitive)."),
    ext: Optional[str] = Query(None, description="File extension (with or without the dot '.')."),
    file_kind: Optional[str] = Query(None, description="ELF | MACHO | PE | Unknown"),
    mime_contains: Optional[str] = Query(None, description="Substring on libmagic description."),
    min_size: Optional[int] = Query(None, ge=0, description="Minimum size in bytes."),
    max_size: Optional[int] = Query(None, ge=0, description="Maximum size in bytes."),
    since: Optional[str] = Query(None, description="ISO datetime filter (upload_time >=)."),
    until: Optional[str] = Query(None, description="ISO datetime filter (upload_time <=).")
):
    # Step 1: base set (query or get all)
    base = search_metadata(query) if query else list_all_metadata()

    # Step 2: apply filters (all AND-combined)
    filtered = filter_metadata(
        base,
        tags=tags,
        tags_mode=tags_mode,
        source=source,
        ext=ext,
        file_kind=file_kind,
        mime_contains=mime_contains,
        min_size=min_size,
        max_size=max_size,
        since_iso=since,
        until_iso=until
    )

    return SearchResponse(count=len(filtered), results=filtered)

app.post("/metadata/update", response_model=UpdateResponse,  status_code=204, tags=["Metadata"],
    summary="Update metadata from external providers.",
    description=(
        "Update the local metadata of a stored sample by querying an external provider API "
        "(e.g., VirusTotal, VirusShare, MalwareBazaar, ). "
        "The provider's response is stored inside the sample's `metadata.external_providers` section. "
        "Returns an object indicating the update status, the sample identifier, and the provider used."
    ), 
)
async def metadata_update(sample: str, provider: str):
    # Step 1: search sample metadata
    results = search_metadata(sample)
    if not results:
        raise HTTPException(status_code=404, detail="Sample not found.")
    result = results[0]

    metadata_path = result.get("metadata_path")
    if not metadata_path or not os.path.exists(metadata_path):
        raise HTTPException(status_code=500, detail="Metadata file not found on disk.")

    # Step 2: query information via providers
    provider_key = provider.strip().lower()
    if provider not in Settings.PROVIDERS:
        raise HTTPException(status_code=400, detail=f"Provider '{provider}' not supported.")

    try:
        provider_response = query_provider(sample, provider_key)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Provider '{provider}' call failed: {e!s}")

    # Step 3: read the metadata section and update
    metadata_file = read_json(metadata_path)
    if not isinstance(metadata_file, dict):
        raise HTTPException(status_code=500, detail="Invalid metadata JSON")

    metadata = metadata_file.get("metadata")
    if not isinstance(metadata, dict):
        raise HTTPException(status_code=500, detail="'metadata' section missing or invalid")

    external_providers = metadata.get("external_providers")
    if external_providers is None:
        external_providers = {}
    elif not isinstance(external_providers, dict):
        raise HTTPException(status_code=500, detail="'external_providers' must be an object")

    # serialize the query provider response into JSON
    external_providers[provider_key] = jsonable_encoder(provider_response)

    # save the structure in the metadata file
    metadata["external_providers"] = external_providers
    metadata_file["metadata"] = metadata
    write_json(metadata_path, metadata_file)

    return UpdateResponse(
        status="updated",
        sample=sample,
        provider=provider_key,
        update=external_providers[provider_key],
    )

@app.post("/providers/extract", tags=["Providers"], status_code=200)
async def providers_extract(sample: str, provider: str): 
    raise NotImplementedError

@app.post("/providers/query", tags=["Providers"], status_code=200)
async def providers_query(sample: str, provider: str):
    raise NotImplementedError

@app.get("/providers/samples", tags=["Providers"], status_code=200)
async def providers_samples(provider: str):
    raise NotImplementedError

###################################################################################################

@app.get("/", status_code=200, tags=["About"],
         summary="About Route.",
         description="About Route.")
@app.get("/about", status_code=200, tags=["About"],
         summary="About Route.",
         description="About Route.")
async def about():
    return RedirectResponse(url="/docs")
    
###################################################################################################

STARTUP_TAG = "Startup"
SHUTDOWN_TAG = "Shutdown"


def startup():
    LOG_SYS.write(STARTUP_TAG, r" ________               _        _       _______  _____  ")
    LOG_SYS.write(STARTUP_TAG, r"|_   __  |             / |_     / \     |_   __ \|_   _| ")
    LOG_SYS.write(STARTUP_TAG, r"  | |_ \_|,--.   .--. `| |-'   / _ \      | |__) | | |   ")
    LOG_SYS.write(STARTUP_TAG, r"  |  _|  `'_\ : ( (`\] | |    / ___ \     |  ___/  | |   ")
    LOG_SYS.write(STARTUP_TAG, r" _| |_   // | |, `'.'. | |, _/ /   \ \_  _| |_    _| |_  ")
    LOG_SYS.write(STARTUP_TAG, r"|_____|  \'-;__/[\__) )\__/|____| |____||_____|  |_____| ")

def shutdown(signum, frame):
    try:
        LOG_SYS.write(SHUTDOWN_TAG, "Shutdown FastAPI server.")
        sys.exit(0)
    except Exception as e:
        LOG_SYS.write(SHUTDOWN_TAG, f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == '__main__':
    # Call Signal Registration
    signal.signal(signal.SIGINT, shutdown)   # Ctrl+C
    signal.signal(signal.SIGTERM, shutdown)  # kill
    signal.signal(signal.SIGHUP, shutdown)   # Terminal closed
    signal.signal(signal.SIGQUIT, shutdown)  # Quit signal
    signal.signal(signal.SIGABRT, shutdown)  # Abort signal
    signal.signal(signal.SIGUSR1, shutdown)  # User-defined signal 1
    signal.signal(signal.SIGUSR2, shutdown)  # User-defined signal 2

    # Startup
    startup()

    # Debug Mode
    #uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

    # Start Uvicorn App
    uvicorn.run(app, host="127.0.0.1", port=8000)

###################################################################################################