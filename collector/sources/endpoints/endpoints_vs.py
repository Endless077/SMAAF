from fastapi import HTTPException, Path, Query
from fastapi.responses import JSONResponse
from pathlib import Path as SysPath

from sources.virustshare import VSClient, VirusShareError

from collector.main import app

# ------------------------------ error handler ------------------------------
def _raise_http_vs(err: Exception) -> None:
    msg = str(err)
    if isinstance(err, VirusShareError):
        if "Rate limit" in msg or "204" in msg:
            raise HTTPException(status_code=429, detail=msg)
        if "Forbidden" in msg or "403" in msg or "unauthorized" in msg:
            raise HTTPException(status_code=403, detail=msg)
        if "Bad request" in msg or "400" in msg or "missing" in msg or "incorrect" in msg:
            raise HTTPException(status_code=400, detail=msg)
        if "Service unavailable" in msg or "503" in msg:
            raise HTTPException(status_code=503, detail=msg)
        if "not found" in msg or "404" in msg:
            raise HTTPException(status_code=404, detail=msg)
        # altri errori lato VirusShare → 502
        raise HTTPException(status_code=502, detail=f"VirusShare API error: {msg}")
    raise HTTPException(status_code=500, detail=msg)

# ------------------------------ endpoints -----------------------------------
@app.get("/virusshare/file/{hash_value}")
def vs_file_report(hash_value: str = Path(..., description="MD5/SHA1/SHA256/SHA512")):
    try:
        with VSClient() as vs:
            data = vs.file_report(hash_value)
        return JSONResponse(content=data)
    except Exception as e:
        _raise_http_vs(e)

@app.get("/virusshare/quick/{hash_value}")
def vs_quick_status(hash_value: str = Path(...)):
    try:
        with VSClient() as vs:
            status = vs.quick_status(hash_value)
        return {"response": status}
    except Exception as e:
        _raise_http_vs(e)

@app.get("/virusshare/source/{sha256}")
def vs_source_info(sha256: str = Path(..., description="SHA256")):
    try:
        with VSClient() as vs:
            data = vs.source_info(sha256)
        return JSONResponse(content=data)
    except Exception as e:
        _raise_http_vs(e)

@app.get("/virusshare/download/{hash_value}")
def vs_download_sample(
    hash_value: str = Path(...),
    filename: str | None = Query(None, description="Nome file opzionale (.zip)")
):
    dest_dir = SysPath("download/VirusShare")
    dest_dir.mkdir(parents=True, exist_ok=True)
    try:
        with VSClient() as vs:
            out_path = vs.download_sample(hash_value, dest_dir=dest_dir, filename=filename)
        return {"saved_path": str(out_path)}
    except Exception as e:
        _raise_http_vs(e)
