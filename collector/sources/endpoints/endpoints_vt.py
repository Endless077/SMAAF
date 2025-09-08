from fastapi import UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil

from vt.error import APIError
from sources.virustotal import VTClient

from collector.main import app

# ------------------------------ error handler ------------------------------
def _raise_http_vt(err: Exception) -> None:
    msg = str(err)
    if isinstance(err, APIError):
        # Mapping dei codici VirusTotal
        if err.code == "NotFoundError":
            raise HTTPException(status_code=404, detail=msg)
        if err.code == "InvalidArgumentError":
            raise HTTPException(status_code=400, detail=msg)
        if err.code == "PermissionDeniedError":
            raise HTTPException(status_code=403, detail=msg)
        if err.code == "QuotaExceededError":
            raise HTTPException(status_code=429, detail="Quota exceeded / rate limited")
        # fallback generico API VirusTotal
        raise HTTPException(status_code=502, detail=f"VirusTotal API error: {msg}")
    # fallback generico
    raise HTTPException(status_code=500, detail=msg)


# -------------------------------------------------
# 1) Get file info
# -------------------------------------------------
@app.get("/virustotal/file/{file_id}")
def get_file_info(file_id: str):
    try:
        with VTClient() as vt:
            info = vt.get_file_info(file_id)
        return JSONResponse(content=info)
    except Exception as e:
        _raise_http_vt(e)


# -------------------------------------------------
# 2) Get URL info
# -------------------------------------------------
@app.get("/virustotal/url/")
def get_url_info(url: str):
    try:
        with VTClient() as vt:
            info = vt.get_url_info(url)
        return JSONResponse(content=info)
    except Exception as e:
        _raise_http_vt(e)


# -------------------------------------------------
# 3) Scan file
# -------------------------------------------------
@app.post("/virustotal/scan/file")
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
        _raise_http_vt(e)
    finally:
        if temp_path.exists():
            temp_path.unlink(missing_ok=True)


# -------------------------------------------------
# 4) Scan URL
# -------------------------------------------------
@app.post("/virustotal/scan/url")
def scan_url(url: str = Form(...), wait: bool = Form(True)):
    try:
        with VTClient() as vt:
            analysis = vt.scan_url(url, wait=wait)
        return JSONResponse(content=analysis)
    except Exception as e:
        _raise_http_vt(e)


# -------------------------------------------------
# 5) Download file
# -------------------------------------------------
@app.get("/virustotal/download/{file_hash}")
def download_file(file_hash: str):
    dest_dir = Path("download/VirusTotal")
    dest_dir.mkdir(parents=True, exist_ok=True)

    try:
        with VTClient() as vt:
            out_path = vt.download_file(file_hash, dest_dir=dest_dir)
        return {"saved_path": str(out_path)}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        _raise_http_vt(e)
