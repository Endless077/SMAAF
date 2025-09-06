# Logging Analytics System
from utils.logger import get_logging
LOG_SYS = get_logging()

# Support Modules
import os
import sys
import signal

from datetime import datetime, timezone

###################################################################################################

# Server
import uvicorn

from fastapi import FastAPI, HTTPException, File, Header, Request, Response, status
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi import Form, Query, Depends, UploadFile
from fastapi.middleware.cors import CORSMiddleware

# Stuff
from .models import *
from .storage import *
from .utilities import *

###################################################################################################

# To Run: uvicorn server:app --host 127.0.0.1 --port 8080 --reload
# To Run: uvicorn server:app --host 127.0.0.1 --port 8080

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

@app.post("/upload", response_model=UploadResponse, status_code=201, tags=["Upload"],
    summary="Upload a sample and persist metadata.",
    description=("Accepts a file (multipart/form-data) and stores it under /samples with a JSON metadata file.")
)
async def upload(
    file: UploadFile = File(..., description="The file to upload."),
    source: str | None = Form(default=None),
    tags: list[str] | None = Form(default=None),
    note: str | None = Form(default=None),
):

    try:
        ensure_samples_dir()

        content = await file.read()
        meta_dict = full_metadata_from_bytes(file.filename, content)

        # Build FileMetadata Pydantic object (includes empty external_providers map)
        metadata = FileMetadata(**meta_dict)

        # Paths
        sha256 = metadata.sha256
        dst_path, meta_path = build_sample_paths(sha256, file.filename)

        # Persist sample
        if not os.path.exists(dst_path):
            write_file(dst_path, content)

        # Persist metadata JSON (API response aligned with models.UploadResponse)
        meta_obj = {
            "id": sha256,
            "stored_path": dst_path,
            "metadata_path": meta_path,
            "metadata": metadata.model_dump(),
            "received_at": datetime.now(timezone.utc).isoformat(),
            "source": source,
            "tags": tags,
            "note": note,
        }
        write_metadata(meta_path, meta_obj)

        LOG_SYS.write(TAG, f"New sample stored: {dst_path}")

        return UploadResponse(
            id=sha256,
            stored_path=dst_path,
            metadata_path=meta_path,
            metadata=metadata,
            received_at=datetime.now(timezone.utc).isoformat(),
            source=source,
            tags=tags,
            note=note,
        )

    except Exception as e:
        LOG_SYS.write(TAG, f"Upload error: {e}")
        raise HTTPException(status_code=500, detail=f"Upload failed: {e}")


@app.get(
    "/api/v1/metadata/search",
    response_model=MetadataSearchResponse,
    tags=["Collector"],
    summary="Search metadata by filename or hash, with optional filters (or list all)",
    description=(
        "If `q` is provided and looks like a hash, match by hash; otherwise match exact filename. "
        "If `q` is omitted, start from the full list. "
        "Then apply optional filters (tags/source/ext/file_kind/mime/size/date/providers). "
        "All filters are AND-combined."
    ),
)
async def search_metadata_route(
    q: Optional[str] = Query(
        None, description="Filename OR hash (sha256/sha1/md5). Leave empty to list all."
    ),
    # --- filters ---
    tags: Optional[List[str]] = Query(
        None, description="Repeatable tag filter: ?tags=a&tags=b"
    ),
    tags_mode: str = Query(
        "any", pattern="^(any|all)$",
        description="'any' = at least one tag matches; 'all' = all provided tags must be present."
    ),
    source: Optional[str] = Query(None, description="Exact source match (case-insensitive)."),
    ext: Optional[str] = Query(None, description="File extension, e.g. '.exe' or 'exe'."),
    file_kind: Optional[str] = Query(None, description="PE | ELF | MACHO | UNKNOWN"),
    mime_contains: Optional[str] = Query(None, description="Substring on libmagic description."),
    min_size: Optional[int] = Query(None, ge=0, description="Minimum size in bytes."),
    max_size: Optional[int] = Query(None, ge=0, description="Maximum size in bytes."),
    since: Optional[str] = Query(None, description="ISO datetime filter (received_at >=)."),
    until: Optional[str] = Query(None, description="ISO datetime filter (received_at <=)."),
    has_providers: Optional[bool] = Query(
        None, description="True: only entries with external_providers; False: only without."
    ),
):
    # Step 1: base set (query or all)
    base = search_metadata(q) if q else list_all_metadata()

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
        until_iso=until,
        has_providers=has_providers,
    )

    return MetadataSearchResponse(count=len(filtered), results=filtered)


###################################################################################################

@app.get("/", status_code=200, tags=["About"],
         summary="",
         description="About Route.")
@app.get("/about", status_code=200, tags=["About"],
         summary="",
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