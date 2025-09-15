#     ________                __                   _            _          
#    |_   __  |              |  ]                 (_)          / |_        
#      | |_ \_| _ .--.   .--.| | _ .--.    .--.   __   _ .--. `| |-'.--.   
#      |  _| _ [ `.-. |/ /'`\' |[ '/'`\ \/ .'`\ \[  | [ `.-. | | | ( (`\]  
#     _| |__/ | | | | || \__/  | | \__/ || \__. | | |  | | | | | |, `'.'.  
#    |________|[___||__]'.__.;__]| ;.__/  '.__.' [___][___||__]\__/[\__) ) 
#                               [__|                                       for VirusTotal.

from fastapi.responses import JSONResponse
from fastapi import UploadFile, Form, HTTPException

from pathlib import Path
import shutil

###

from sources.virustotal import VTClient, APIError
from configs.config import settings
from collector.main import app

###################################################################################################

# ================= Error Handler =================
def _raise_http(err: Exception) -> None:
    if isinstance(err, HTTPException):
        raise err
    
    raise HTTPException(status_code=500, detail=str(err))

###################################################################################################

# ================= Endpoints =================
@app.get("/virustotal/file/{file_id}", tags=["VirustTotal"], status_code=200)
def get_file_info(file_id: str):
    try:
        with VTClient() as vt:
            info = vt.get_file_info(file_id)
        return JSONResponse(content=info)
    except Exception as e:
        _raise_http(e)

@app.get("/virustotal/url/", tags=["VirustTotal"], status_code=200)
def get_url_info(url: str):
    try:
        with VTClient() as vt:
            info = vt.get_url_info(url)
        return JSONResponse(content=info)
    except Exception as e:
        _raise_http(e)

@app.post("/virustotal/scan/file", tags=["VirustTotal"], status_code=200)
async def scan_file(file: UploadFile, wait: bool = Form(True)):
    temp_path = Path(f"/tmp/{file.filename}")

    try:
        with temp_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        with VTClient() as vt:
            analysis = vt.scan_file(temp_path, wait=wait)

        return JSONResponse(content=analysis)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        _raise_http(e)
    finally:
        if temp_path.exists():
            temp_path.unlink(missing_ok=True)

@app.post("/virustotal/scan/url", tags=["VirustTotal"], status_code=200)
def scan_url(url: str = Form(...), wait: bool = Form(True)):
    try:
        with VTClient() as vt:
            analysis = vt.scan_url(url, wait=wait)
        return JSONResponse(content=analysis)
    except Exception as e:
        _raise_http(e)

@app.get("/virustotal/download/{file_hash}", tags=["VirustTotal"], status_code=201)
def download_file(file_hash: str):
    dest_dir = settings.DOWNLOAD_DIR / "VirusTotal"
    dest_dir.mkdir(parents=True, exist_ok=True)

    try:
        with VTClient() as vt:
            out_path = vt.download_file(file_hash, dest_dir=dest_dir)
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
