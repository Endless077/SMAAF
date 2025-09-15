#     ________                __                   _            _          
#    |_   __  |              |  ]                 (_)          / |_        
#      | |_ \_| _ .--.   .--.| | _ .--.    .--.   __   _ .--. `| |-'.--.   
#      |  _| _ [ `.-. |/ /'`\' |[ '/'`\ \/ .'`\ \[  | [ `.-. | | | ( (`\]  
#     _| |__/ | | | | || \__/  | | \__/ || \__. | | |  | | | | | |, `'.'.  
#    |________|[___||__]'.__.;__]| ;.__/  '.__.' [___][___||__]\__/[\__) ) 
#                               [__|                                       for MalwareBazaar.

import json
import requests
from pathlib import Path as SysPath
from fastapi.responses import JSONResponse
from fastapi import HTTPException, UploadFile, File, Form, Path, Query, Body

###

from sources.malwarebazaar import MBClient, MalwareBazaarError
from configs.config import settings
from collector.main import app

###################################################################################################

# ================= Error Handler =================
def _raise_http(err: Exception) -> None:
    if isinstance(err, HTTPException):
        raise err
    
    if isinstance(err, MalwareBazaarError):
        raise HTTPException(status_code=400, detail=str(err)) from err

    if isinstance(err, requests.HTTPError):
        response = err.response
        status = response.status_code if response is not None else 502
        body_snippet = None
        if response is not None:
            try:
                body_snippet = response.text
                if body_snippet and len(body_snippet) > 500:
                    body_snippet = body_snippet[:500] + "...(truncated)"
            except Exception:
                body_snippet = None

        detail = f"HTTP error: {str(err)}"
        if body_snippet:
            detail += f" | body: {body_snippet}"
        raise HTTPException(status_code=status, detail=detail) from err

    if isinstance(err, requests.Timeout):
        raise HTTPException(status_code=504, detail=f"Timeout: {err}") from err

    if isinstance(err, requests.RequestException):
        raise HTTPException(status_code=502, detail=f"Request failed: {err}") from err

    if isinstance(err, json.JSONDecodeError):
        raise HTTPException(status_code=502, detail=f"Invalid JSON from upstream: {err}") from err

    raise HTTPException(status_code=500, detail=f"Internal error: {err}") from err

###################################################################################################

# ================= Endpoints =================
@app.post("/malwarebazaar/query", tags=["Malware Bazaar"], status_code=200)
def mb_query(payload: dict = Body(..., example={"query": "get_info", "hash": "…"})):
    if "query" not in payload:
        raise HTTPException(status_code=400, detail="Missing 'query' field.")
    q = payload.pop("query")
    try:
        client = MBClient()
        data = client.query(q, **payload)
        return JSONResponse(content=data)
    except Exception as e:
        _raise_http(e)

@app.get("/malwarebazaar/info/{hash_value}", tags=["Malware Bazaar"], status_code=200)
def mb_get_info(hash_value: str = Path(...)):
    try:
        client = MBClient()
        return client.get_info(hash_value)
    except Exception as e:
        _raise_http(e)

@app.get("/malwarebazaar/recent", tags=["Malware Bazaar"], status_code=200)
def mb_get_recent(selector: str = Query("time"), limit: int = Query(10, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_recent(selector=selector, limit=limit)
    except Exception as e:
        _raise_http(e)

@app.get("/malwarebazaar/tag/{tag}", tags=["Malware Bazaar"], status_code=200)
def mb_get_taginfo(tag: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_taginfo(tag, limit=limit)
    except Exception as e:
        _raise_http(e)

@app.get("/malwarebazaar/signature/{signature}", tags=["Malware Bazaar"], status_code=200)
def mb_get_siginfo(signature: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_siginfo(signature, limit=limit)
    except Exception as e:
        _raise_http(e)

@app.get("/malwarebazaar/filetype/{filetype}", tags=["Malware Bazaar"], status_code=200)
def mb_get_taginfo(filetype: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_filetype(filetype, limit=limit)
    except Exception as e:
        _raise_http(e)

@app.get("/malwarebazaar/clamav/{signature}", tags=["Malware Bazaar"], status_code=200)
def mb_get_clamav(signature: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_clamav(signature, limit=limit)
    except Exception as e:
        _raise_http(e)

@app.get("/malwarebazaar/imphash/{imphash}", tags=["Malware Bazaar"], status_code=200)
def mb_get_imphash(imphash: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_imphash(imphash, limit=limit)
    except Exception as e:
        _raise_http(e)

@app.get("/malwarebazaar/tlsh/{tlsh}", tags=["Malware Bazaar"], status_code=200)
def mb_get_tlsh(tlsh: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_tlsh(tlsh, limit=limit)
    except Exception as e:
        _raise_http(e)

@app.get("/malwarebazaar/telfhash/{telfhash}", tags=["Malware Bazaar"], status_code=200)
def mb_get_tlsh(telfhash: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_tlsh(telfhash, limit=limit)
    except Exception as e:
        _raise_http(e)

@app.get("/malwarebazaar/gimphash/{gimphash}", tags=["Malware Bazaar"], status_code=200)
def mb_get_tlsh(gimphash: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_tlsh(gimphash, limit=limit)
    except Exception as e:
        _raise_http(e)

@app.get("/malwarebazaar/dhash_icon/{dhash_icon}", tags=["Malware Bazaar"], status_code=200)
def mb_get_tlsh(dhash_icon: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_tlsh(dhash_icon, limit=limit)
    except Exception as e:
        _raise_http(e)

@app.get("/malwarebazaar/yarainfo/{yara_rule}", tags=["Malware Bazaar"], status_code=200)
def mb_get_yarainfo(yara_rule: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_yarainfo(yara_rule, limit=limit)
    except Exception as e:
        _raise_http(e)

@app.get("/malwarebazaar/certs/issuer/{issuer_cn}", tags=["Malware Bazaar"], status_code=200)
def mb_get_issuerinfo(issuer_cn: str):
    try:
        client = MBClient()
        return client.get_issuerinfo(issuer_cn)
    except Exception as e:
        _raise_http(e)

@app.get("/malwarebazaar/certs/subject/{subject_cn}", tags=["Malware Bazaar"], status_code=200)
def mb_get_subjectinfo(subject_cn: str):
    try:
        client = MBClient()
        return client.get_subjectinfo(subject_cn)
    except Exception as e:
        _raise_http(e)

@app.get("/malwarebazaar/certs/serial/{serial_number}", tags=["Malware Bazaar"], status_code=200)
def mb_get_certificate(serial_number: str):
    try:
        client = MBClient()
        return client.get_certificate(serial_number)
    except Exception as e:
        _raise_http(e)

@app.get("/malwarebazaar/certs/cscb", tags=["Malware Bazaar"], status_code=200)
def mb_get_cscb():
    try:
        client = MBClient()
        return client.get_cscb()
    except Exception as e:
        _raise_http(e)

@app.post("/malwarebazaar/download/{sha256}", tags=["Malware Bazaar"], status_code=201)
def mb_download_sample(
    sha256: str = Path(...),
    filename: str | None = Query(None)
):
    dest_dir = settings.DOWNLOAD_DIR / "MalwareBazaar"
    dest_dir.mkdir(parents=True, exist_ok=True)

    try:
        client = MBClient()
        path = client.download_sample(
                sha256,
                dest_dir=dest_dir,
                filename=filename
                )

        return JSONResponse(
            content={
                "success": True,
                "data": {
                    "hash": sha256,
                    "provider": "MalwareBazaar",
                    "saved_path": str(path),
                },
                "message": "Sample successfully downloaded from MalwareBazaar."
            },
            status_code=200,
        )

    except Exception as e:
        _raise_http(e)

@app.post("/malwarebazaar/submit", tags=["Malware Bazaar"], status_code=201)
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
        response = client.submit_sample(
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
        return JSONResponse(content=response)
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON in references/context: {e}")
    except Exception as e:
        _raise_http(e)

###################################################################################################
