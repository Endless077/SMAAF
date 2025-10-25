#     ________                __                   _            _          
#    |_   __  |              |  ]                 (_)          / |_        
#      | |_ \_| _ .--.   .--.| | _ .--.    .--.   __   _ .--. `| |-'.--.   
#      |  _| _ [ `.-. |/ /'`\' |[ '/'`\ \/ .'`\ \[  | [ `.-. | | | ( (`\]  
#     _| |__/ | | | | || \__/  | | \__/ || \__. | | |  | | | | | |, `'.'.  
#    |________|[___||__]'.__.;__]| ;.__/  '.__.' [___][___||__]\__/[\__) ) 
#                               [__|                                       for MalwareBazaar.

# ───────────────────────────────────────────────────────────────
# Third-party libraries
import requests
from fastapi import APIRouter, Body, File, Form, HTTPException, Path, Query, UploadFile
from fastapi.responses import JSONResponse

# ───────────────────────────────────────────────────────────────
# Local application imports
from collector.configs.config import settings
from collector.sources.malwarebazaar import MBClient, MalwareBazaarError

# ───────────────────────────────────────────────────────────────
# Standard library
import json
from pathlib import Path as SysPath

# ───────────────────────────────────────────────────────────────
# Router initialization
router = APIRouter()

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
@router.post("/malwarebazaar/query", tags=["Malware Bazaar"], status_code=200,
        summary="MalwareBazaar generic query route.",
        description="Send a generic query to MalwareBazaar.")
def mb_query(payload: dict = Body(..., examples={"query": "get_info", "hash": "…"})):
    if "query" not in payload:
        raise HTTPException(status_code=400, detail="Missing 'query' field.")
    q = payload.pop("query")
    try:
        client = MBClient()
        data = client.query(q, **payload)
        return JSONResponse(content=data)
    except Exception as e:
        _raise_http(e)

@router.get("/malwarebazaar/info/{hash_value}", tags=["Malware Bazaar"], status_code=200,
        summary="MalwareBazaar file info.",
        description="Retrieve detailed information about a file from MalwareBazaar using its hash.")
def mb_get_info(hash_value: str = Path(...)):
    try:
        client = MBClient()
        return client.get_info(hash_value)
    except Exception as e:
        _raise_http(e)

@router.get("/malwarebazaar/recent", tags=["Malware Bazaar"], status_code=200,
          summary="MalwareBazaar recent samples.",
         description="Retrieve the most recent samples from MalwareBazaar, filtered by selector.")
def mb_get_recent(selector: str = Query("time"), limit: int = Query(10, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_recent(selector=selector, limit=limit)
    except Exception as e:
        _raise_http(e)

@router.get("/malwarebazaar/tag/{tag}", tags=["Malware Bazaar"], status_code=200,
        summary="Malware Bazaar samples by tag.",
        description="Retrieve samples from MalwareBazaar associated with a specific tag.")
def mb_get_taginfo(tag: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_taginfo(tag, limit=limit)
    except Exception as e:
        _raise_http(e)

@router.get("/malwarebazaar/signature/{signature}", tags=["Malware Bazaar"], status_code=200,
        summary="Malware Bazaar samples by signature.",
        description="Retrieve samples from MalwareBazaar that match a given malware signature.")
def mb_get_siginfo(signature: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_siginfo(signature, limit=limit)
    except Exception as e:
        _raise_http(e)

@router.get("/malwarebazaar/filetype/{filetype}", tags=["Malware Bazaar"], status_code=200,
        summary="Malware Bazaar samples by file type",
        description="Retrieve samples from MalwareBazaar that match a specific file type.")
def mb_get_taginfo(filetype: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_filetype(filetype, limit=limit)
    except Exception as e:
        _raise_http(e)

@router.get("/malwarebazaar/clamav/{signature}", tags=["Malware Bazaar"], status_code=200,
        summary="Malware Bazaar samples by ClamAV signature",
        description="Retrieve samples from MalwareBazaar detected by a given ClamAV signature.")
def mb_get_clamav(signature: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_clamav(signature, limit=limit)
    except Exception as e:
        _raise_http(e)

@router.get("/malwarebazaar/imphash/{imphash}", tags=["Malware Bazaar"], status_code=200,
        summary="Malware Bazaar samples by imphash.",
        description="Retrieve samples from MalwareBazaar matching a given imphash.")
def mb_get_imphash(imphash: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_imphash(imphash, limit=limit)
    except Exception as e:
        _raise_http(e)

@router.get("/malwarebazaar/tlsh/{tlsh}", tags=["Malware Bazaar"], status_code=200,
        summary="Malware Bazaar samples by TLSH",
        description="Retrieve samples from MalwareBazaar matching a given TLSH hash.")
def mb_get_tlsh(tlsh: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_tlsh(tlsh, limit=limit)
    except Exception as e:
        _raise_http(e)

@router.get("/malwarebazaar/telfhash/{telfhash}", tags=["Malware Bazaar"], status_code=200,
        summary="Malware Bazaar samples by telfhash.",
        description="Retrieve samples from MalwareBazaar matching a given telfhash.")
def mb_get_telfhash(telfhash: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_tlsh(telfhash, limit=limit)
    except Exception as e:
        _raise_http(e)

@router.get("/malwarebazaar/gimphash/{gimphash}", tags=["Malware Bazaar"], status_code=200,
        summary="Malware Bazaar samples by gimphash.",
        description="Retrieve samples from MalwareBazaar matching a given gimphash.")
def mb_get_gimphash(gimphash: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_tlsh(gimphash, limit=limit)
    except Exception as e:
        _raise_http(e)

@router.get("/malwarebazaar/dhash_icon/{dhash_icon}", tags=["Malware Bazaar"], status_code=200,
        summary="Malware Bazaar samples by dhash icon.",
        description="Retrieve samples from MalwareBazaar with a matching dhash of the file's icon.")
def mb_get_dhash(dhash_icon: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_tlsh(dhash_icon, limit=limit)
    except Exception as e:
        _raise_http(e)

@router.get("/malwarebazaar/yarainfo/{yara_rule}", tags=["Malware Bazaar"], status_code=200,
        summary="Malware Bazaar samples by YARA rule.",
        description="Retrieve samples from MalwareBazaar that match a given YARA rule.")
def mb_get_yarainfo(yara_rule: str, limit: int = Query(100, ge=1, le=1000)):
    try:
        client = MBClient()
        return client.get_yarainfo(yara_rule, limit=limit)
    except Exception as e:
        _raise_http(e)

@router.get("/malwarebazaar/certs/issuer/{issuer_cn}", tags=["Malware Bazaar"], status_code=200,
        summary="Malware Bazaar samples by certificate issuer.",
        description="Retrieve samples from MalwareBazaar signed with a certificate from a specific issuer CN.")
def mb_get_issuerinfo(issuer_cn: str):
    try:
        client = MBClient()
        return client.get_issuerinfo(issuer_cn)
    except Exception as e:
        _raise_http(e)

@router.get("/malwarebazaar/certs/subject/{subject_cn}", tags=["Malware Bazaar"], status_code=200,
        summary="Malware Bazaar samples by certificate subject.",
        description="Retrieve samples from MalwareBazaar signed with a certificate for a specific subject CN.")
def mb_get_subjectinfo(subject_cn: str):
    try:
        client = MBClient()
        return client.get_subjectinfo(subject_cn)
    except Exception as e:
        _raise_http(e)

@router.get("/malwarebazaar/certs/serial/{serial_number}", tags=["Malware Bazaar"], status_code=200,
        summary="Malware Bazaar samples by certificate serial.",
        description="Retrieve samples from MalwareBazaar signed with a certificate that has the given serial number.")
def mb_get_certificate(serial_number: str):
    try:
        client = MBClient()
        return client.get_certificate(serial_number)
    except Exception as e:
        _raise_http(e)

@router.get("/malwarebazaar/certs/cscb", tags=["Malware Bazaar"], status_code=200,
        summary="Malware Bazaar Code Signing Certificate Blocklist.",
        description="Retrieve the current Code Signing Certificate Blocklist (CSCB) from MalwareBazaar.")
def mb_get_cscb():
    try:
        client = MBClient()
        return client.get_cscb()
    except Exception as e:
        _raise_http(e)

@router.post("/malwarebazaar/download/{sha256}", tags=["Malware Bazaar"], status_code=201,
        summary="Malware Bazaar download sample.",
        description="Download a malware sample from MalwareBazaar using its SHA-256 hash. Optionally specify a custom filename.")
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

@router.post("/malwarebazaar/submit", tags=["Malware Bazaar"], status_code=201,
        summary="Malware Bazaar submit a sample.",
        description="Submit a new malware sample to MalwareBazaar. Supports optional metadata such as tags, references, and context information.")
async def mb_submit_sample(
    file: UploadFile = File(...),
    anonymous: int = Form(0),
    tags: str | None = Form(None),
    references: str | None = Form(None),
    context: str | None = Form(None),
    delivery_method: str | None = Form(None),
):
    try:
        tmp_dir = SysPath("/tmp"); tmp_dir.mkdir(parents=True, exist_ok=True)
        tmp_path = tmp_dir / file.filename
        tmp_path.write_bytes(await file.read())

        tag_list = [t.strip() for t in tags.split(",")] if tags else None
        refs = json.loads(references) if references else None
        ctx = json.loads(context) if context else None

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
