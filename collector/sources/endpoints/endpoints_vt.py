#     ________                __                   _            _          
#    |_   __  |              |  ]                 (_)          / |_        
#      | |_ \_| _ .--.   .--.| | _ .--.    .--.   __   _ .--. `| |-'.--.   
#      |  _| _ [ `.-. |/ /'`\' |[ '/'`\ \/ .'`\ \[  | [ `.-. | | | ( (`\]  
#     _| |__/ | | | | || \__/  | | \__/ || \__. | | |  | | | | | |, `'.'.  
#    |________|[___||__]'.__.;__]| ;.__/  '.__.' [___][___||__]\__/[\__) ) 
#                               [__|                                       for VirusTotal.

# ───────────────────────────────────────────────────────────────
# Third-party libraries
from fastapi import APIRouter, Form, HTTPException, UploadFile
from fastapi.responses import JSONResponse

# ───────────────────────────────────────────────────────────────
# Local application imports
from collector.configs.config import settings
from collector.sources.virustotal import APIError, VTClient

# ───────────────────────────────────────────────────────────────
# Standard library
import shutil
from pathlib import Path

# ───────────────────────────────────────────────────────────────
# Router initialization
router = APIRouter()


###################################################################################################

# ================= Error Handler =================
def _raise_http(err: Exception) -> None:
    if isinstance(err, HTTPException):
        raise err
    
    if isinstance(err, APIError):
        raise HTTPException(status_code=502, detail=f"VirusTotal API error: {err}")
    
    raise HTTPException(status_code=500, detail=str(err))

###################################################################################################

# ================= Endpoints =================
@router.get("/virustotal/file/{file_id}", tags=["VirustTotal"], status_code=200,
        summary="VirusTotal file analysis by ID.",
        description="Retrieve VirusTotal analysis details of a specific file using its ID or hash.")
async def get_file_info(file_id: str):
    try:
        vt = VTClient()
        info = await vt.get_file_info(file_id)
        await vt.close()
        return JSONResponse(content=info)
    except Exception as e:
        _raise_http(e)

@router.get("/virustotal/url/", tags=["VirustTotal"], status_code=200,
        summary="VirusTotal URL analysis.",
        description="Retrieve the VirusTotal report for a given URL.")
async def get_url_info(url: str):
    try:
        vt = VTClient()
        info = await vt.get_url_info(url)
        await vt.close()
        return JSONResponse(content=info)
    except Exception as e:
        _raise_http(e)

@router.post("/virustotal/scan/file", tags=["VirustTotal"], status_code=200,
        summary="VirusTotal file scan.",
        description="Upload a file to VirusTotal for scanning. Returns the analysis result, either immediately or after completion if wait is enabled.")
async def scan_file(file: UploadFile, wait: bool = Form(True)):
    temp_path = Path(f"/tmp/{file.filename}")

    try:
        with temp_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        vt = VTClient()
        analysis = await vt.scan_file(temp_path, wait=wait)
        await vt.close()

        return JSONResponse(content=analysis)
    except Exception as e:
        _raise_http(e)
    finally:
        if temp_path.exists():
            temp_path.unlink(missing_ok=True)

@router.post("/virustotal/scan/url", tags=["VirustTotal"], status_code=200,
        summary="VirusTotal URL scan.",
        description="Submit a URL to VirusTotal for scanning. Returns the analysis status and results, depending on the wait option.")
async def scan_url(url: str = Form(...), wait: bool = Form(True)):
    try:
        vt = VTClient()
        analysis = await vt.scan_url(url, wait=wait)
        await vt.close()
        return JSONResponse(content=analysis)
    except Exception as e:
        _raise_http(e)

@router.get("/virustotal/download/{file_hash}", tags=["VirustTotal"], status_code=201,
        summary="VirusTotal download file.",
        description="Download a file from VirusTotal using its hash and save it locally.")
async def download_file(file_hash: str):
    dest_dir = settings.DOWNLOAD_DIR / "VirusTotal"
    dest_dir.mkdir(parents=True, exist_ok=True)

    try:
        vt = VTClient()
        out_path = await vt.download_file(file_hash, dest_dir=dest_dir)
        await vt.close()

        return JSONResponse(
            content={
                "success": True,
                "data": {
                    "file_hash": file_hash,
                    "provider": "VirusTotal",
                    "saved_path": str(out_path),
                },
                "message": "File successfully downloaded from VirusTotal."
            },
            status_code=201,
        )
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        _raise_http(e)

###################################################################################################
