#     ________                __                   _            _          
#    |_   __  |              |  ]                 (_)          / |_        
#      | |_ \_| _ .--.   .--.| | _ .--.    .--.   __   _ .--. `| |-'.--.   
#      |  _| _ [ `.-. |/ /'`\' |[ '/'`\ \/ .'`\ \[  | [ `.-. | | | ( (`\]  
#     _| |__/ | | | | || \__/  | | \__/ || \__. | | |  | | | | | |, `'.'.  
#    |________|[___||__]'.__.;__]| ;.__/  '.__.' [___][___||__]\__/[\__) ) 
#                               [__|                                       for VirusShare.

from fastapi.responses import JSONResponse
from fastapi import HTTPException, Path, Query

###

from sources.virustshare import VSClient, VirusShareError
from configs.config import settings
from collector.main import app

###################################################################################################

# ================= Error Handler =================
def _raise_http(err: Exception) -> None:
    if isinstance(err, HTTPException):
        raise err
    
    msg = str(err)
    
    if isinstance(err, VirusShareError):
        if "Forbidden" in msg or "403" in msg or "unauthorized" in msg:
            raise HTTPException(status_code=403, detail=msg)
        if "Not found" in msg or "404" in msg:
            raise HTTPException(status_code=404, detail=msg)
        if "Bad request" in msg or "400" in msg or "missing" in msg or "incorrect" in msg:
            raise HTTPException(status_code=400, detail=msg)
        if "Service unavailable" in msg or "503" in msg:
            raise HTTPException(status_code=503, detail=msg)
        if "Internal server error" in msg or "500" in msg:
            raise HTTPException(status_code=503, detail=msg)
        if "Request rate limit exceeded" in msg or "204" in msg:
            raise HTTPException(status_code=429, detail=msg)
        raise HTTPException(status_code=502, detail=f"VirusShare APIs error: {msg}")
    
    raise HTTPException(status_code=500, detail=msg)

###################################################################################################

# ================= Endpoints =================
@app.get("/virusshare/file/{hash_value}", tags=["VirusShare"], status_code=200,
        summary="VirusShare file report",
        description="Retrieve detailed VirusShare report for a file using its hash value.")
def vs_file_report(hash_value: str = Path(...)):
    try:
        client = VSClient()
        data = client.file_report(hash_value)
        return JSONResponse(content=data)
    except Exception as e:
        _raise_http(e)

@app.get("/virusshare/quick/{hash_value}", tags=["VirusShare"], status_code=200,
        summary="VirusShare quick file status.",
        description="Get a quick status check from VirusShare for a file using its hash value.")
def vs_quick_status(hash_value: str = Path(...)):
    try:
        client = VSClient()
        status = client.quick_status(hash_value)
        return {"response": status}
    except Exception as e:
        _raise_http(e)

@app.get("/virusshare/source/{sha256}", tags=["VirusShare"], status_code=200,
        summary="VirusShare source info.",
        description="Retrieve source information from VirusShare for a file using its SHA-256 hash.")
def vs_source_info(sha256: str = Path(...)):
    try:
        client = VSClient()
        data = client.source_info(sha256)
        return JSONResponse(content=data)
    except Exception as e:
        _raise_http(e)

@app.get("/virusshare/download/{hash_value}", tags=["VirusShare"], status_code=201,
          summary="VirusShare download sample.",
         description="Download a malware sample from VirusShare using its hash value. Optionally specify a custom filename. The sample is saved locally.")
def vs_download_sample(
    hash_value: str = Path(...),
    filename: str | None = Query(None)
):
    dest_dir = settings.DOWNLOAD_DIR / "VirusShare"
    dest_dir.mkdir(parents=True, exist_ok=True)

    try:
        client = VSClient()
        path = client.download_sample(
            hash_value,
            dest_dir=dest_dir,
            filename=filename
            )
        
        return JSONResponse(
            content={
                "success": True,
                "data": {
                    "hash": hash_value,
                    "provider": "VirusShare",
                    "saved_path": str(path),
                },
                "message": "Sample successfully downloaded from VirusShare."
            },
            status_code=200,
        )
        
    except Exception as e:
        _raise_http(e)

###################################################################################################
