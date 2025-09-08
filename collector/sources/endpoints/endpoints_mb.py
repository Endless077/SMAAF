from fastapi import HTTPException, UploadFile, File, Form, Path, Query, Body
from fastapi.responses import JSONResponse
from pathlib import Path as SysPath
import json

from sources.malwarebazaar import MBClient, MalwareBazaarError

from collector.main import app

# ------------------------------ error handler ------------------------------
def _raise_http_mb(err: Exception) -> None:
    msg = str(err)
    if isinstance(err, MalwareBazaarError):
        if "no_api_key" in msg or "Auth-Key" in msg or "user_blacklisted" in msg:
            raise HTTPException(status_code=403, detail=msg)
        if "http_post_expected" in msg or "illegal_sha256_hash" in msg or "Bad request" in msg:
            raise HTTPException(status_code=400, detail=msg)
        if "file_not_found" in msg or "not found" in msg:
            raise HTTPException(status_code=404, detail=msg)
        # altri errori lato MB → 502
        raise HTTPException(status_code=502, detail=f"MalwareBazaar API error: {msg}")
    raise HTTPException(status_code=500, detail=msg)

# ------------------------------ endpoints -----------------------------------
@app.post("/malwarebazaar/query")
def mb_query(payload: dict = Body(..., example={"query": "get_info", "hash": "…"})):
    if "query" not in payload:
        raise HTTPException(status_code=400, detail="Missing 'query' field.")
    q = payload.pop("query")
    try:
        client = MBClient()
        data = client.query(q, **payload)
        return JSONResponse(content=data)
    except Exception as e:
        _raise_http_mb(e)

@app.get("/malwarebazaar/info/{hash_value}")
def mb_get_info(hash_value: str = Path(...)):
    try:
        client = MBClient()
        return client.get_info(hash_value)
    except Exception as e:
        _raise_http_mb(e)

@app.get("/malwarebazaar/recent")
def mb_get_recent(selector: str = Query("time"), limit: int = Query(10, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_recent(selector=selector, limit=limit)
    except Exception as e:
        _raise_http_mb(e)

@app.get("/malwarebazaar/tag/{tag}")
def mb_get_taginfo(tag: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_taginfo(tag, limit=limit)
    except Exception as e:
        _raise_http_mb(e)

@app.get("/malwarebazaar/signature/{signature}")
def mb_get_siginfo(signature: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_siginfo(signature, limit=limit)
    except Exception as e:
        _raise_http_mb(e)

@app.get("/malwarebazaar/yarainfo/{rule_name}")
def mb_get_yarainfo(rule_name: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_yarainfo(rule_name, limit=limit)
    except Exception as e:
        _raise_http_mb(e)

@app.get("/malwarebazaar/imphash/{imphash}")
def mb_get_imphash(imphash: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_imphash(imphash, limit=limit)
    except Exception as e:
        _raise_http_mb(e)

@app.get("/malwarebazaar/tlsh/{tlsh}")
def mb_get_tlsh(tlsh: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_tlsh(tlsh, limit=limit)
    except Exception as e:
        _raise_http_mb(e)

@app.get("/malwarebazaar/clamav/{sig}")
def mb_get_clamav(sig: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_clamav(sig, limit=limit)
    except Exception as e:
        _raise_http_mb(e)

@app.get("/malwarebazaar/certs/issuer/{issuer_cn}")
def mb_get_issuerinfo(issuer_cn: str):
    try:
        client = MBClient()
        return client.get_issuerinfo(issuer_cn)
    except Exception as e:
        _raise_http_mb(e)

@app.get("/malwarebazaar/certs/subject/{subject_cn}")
def mb_get_subjectinfo(subject_cn: str):
    try:
        client = MBClient()
        return client.get_subjectinfo(subject_cn)
    except Exception as e:
        _raise_http_mb(e)

@app.get("/malwarebazaar/certs/serial/{serial_number}")
def mb_get_certificate(serial_number: str):
    try:
        client = MBClient()
        return client.get_certificate(serial_number)
    except Exception as e:
        _raise_http_mb(e)

@app.get("/malwarebazaar/certs/cscb")
def mb_get_cscb():
    try:
        client = MBClient()
        return client.get_cscb()
    except Exception as e:
        _raise_http_mb(e)

@app.post("/malwarebazaar/download/{sha256}")
def mb_download_sample(
    sha256: str = Path(..., description="SHA256"),
    filename: str | None = Query(None, description="Nome file opzionale")
):
    dest_dir = SysPath("download/MalwareBazaar")
    dest_dir.mkdir(parents=True, exist_ok=True)
    try:
        client = MBClient()
        saved = client.download_sample(sha256, dest_dir=dest_dir, filename=filename)
        return {"saved_path": str(saved)}
    except Exception as e:
        _raise_http_mb(e)

@app.post("/malwarebazaar/submit")
async def mb_submit_sample(
    file: UploadFile = File(...),
    anonymous: int = Form(0),
    delivery_method: str | None = Form(None),
    tags: str | None = Form(None, description="CSV: 'emotet,banking'"),
    references_json: str | None = Form(None, description='JSON: {"links": ["…"]}'),
    context_json: str | None = Form(None, description='JSON: {"country": "…", "source": ["…"]}')
):
    try:
        tmp_dir = SysPath("/tmp"); tmp_dir.mkdir(parents=True, exist_ok=True)
        tmp_path = tmp_dir / file.filename
        tmp_path.write_bytes(await file.read())

        tag_list = [t.strip() for t in tags.split(",")] if tags else None
        refs = json.loads(references_json) if references_json else None
        ctx = json.loads(context_json) if context_json else None

        client = MBClient()
        res = client.submit_sample(
            tmp_path,
            anonymous=anonymous,
            delivery_method=delivery_method,
            tags=tag_list,
            references=refs,
            context=ctx,
        )
        try:
            tmp_path.unlink(missing_ok=True)
        finally:
            pass
        return JSONResponse(content=res)
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON in references/context: {e}")
    except Exception as e:
        _raise_http_mb(e)
