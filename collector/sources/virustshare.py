#     ____   ____  _                           ______   __                             
#    |_  _| |_  _|(_)                        .' ____ \ [  |                            
#      \ \   / /  __   _ .--.  __   _   .--. | (___ \_| | |--.   ,--.   _ .--.  .---.  
#       \ \ / /  [  | [ `/'`\][  | | | ( (`\] _.____`.  | .-. | `'_\ : [ `/'`\]/ /__\\ 
#        \ ' /    | |  | |     | \_/ |, `'.'.| \____) | | | | | // | |, | |    | \__., 
#         \_/    [___][___]    '.__.'_/[\__) )\______.'[___]|__]\'-;__/[___]    '.__.' 
#                                                                                      
"""
VirusShare API v2 Client for Static Malware Analysis Framework (SMAF)
https://virusshare.com/apiv2_reference

This module implements a thin Python client around the VirusShare v2 API.
It provides access to all documented endpoints, allowing retrieval of
malware metadata, quick classification status, crawler source history,
and password-protected sample downloads.

Implemented endpoints:
- /file      → Retrieve file report (metadata, VT summary, detection info).
- /quick     → Quick classification (0 unknown, 1 malware, 2 benign).
- /source    → Get crawler source info (URL history, SHA256 only).
- /download  → Download a sample ZIP (password: 'infected').

What is?
Large malware repository offering access to real-world samples and metadata for
research, correlation, and enrichment in malware analysis.
"""

# VirusShare
class VirusShareError(RuntimeError):
    pass

API_BASE = "https://virusshare.com/apiv2"

from collector.configs.config import settings

###

import json
import time
import requests

import sys

from pathlib import Path
from typing import Dict, Optional, Any

###################################################################################################

class VSClient:
    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        backoff: float = 3,
        timeout: Optional[int] = None,
        user_agent: Optional[str] = None,
    ) -> None:
        
        # Load VirusShar API key from argument or settings
        self.api_key = api_key or settings.VS_API_KEY
        if not self.api_key:
            raise VirusShareError("VirusShare API key not provided.")

        # Resolve request timeout (seconds)
        self.timeout = timeout or settings.TIMEOUT

        # Backoff delay between retries / rate-limits
        self.backoff = backoff

        # Compose a descriptive User-Agent for server-side diagnostics
        self.user_agent = (
            user_agent
            or f"VirusShareClient/1.0 requests/{requests.__version__} "
               f"Python/{sys.version_info.major}.{sys.version_info.minor}"
        )

        # Create a persistent HTTP session and set default headers
        self._session = requests.Session()
        self._session.headers.update({"User-Agent": self.user_agent})

###################################################################################################

    # ================= Context Manager =================
    def __enter__(self) -> "VSClient":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    # Close underlying resources
    def close(self) -> None:
        pass
            
    # ================= Helpers =================
    def _get(self, endpoint: str, *, hash_value: str, stream: bool = False) -> requests.Response:
        # Endpoint URL building
        url = f"{API_BASE}{endpoint}"
        
        # Attach API key and hash
        params = {"apikey": self.api_key, "hash": hash_value}
        try:
            # Issue request with optional streaming for downloads
            response = self._session.get(url, params=params, timeout=self.timeout, stream=stream)
        except requests.RequestException as e:
            raise VirusShareError(f"HTTP error about VirusShare: {e}") from e
        
        # Forbidden (403)
        if response.status_code == 403:
            raise VirusShareError("Forbidden (403): you don't have privileges to make this request.")
        # Not found (404)
        if response.status_code == 404:
            raise VirusShareError("Not found (404): the file you have requested could not be found.")
        # Bad request (400)
        if response.status_code == 400:
            raise VirusShareError("Bad request (400): your request was incorrect.")
        # Service unavailable (503)
        if response.status_code == 503:
            raise VirusShareError("Service unavailable (503): try again later.")
        # Internal server error (500)
        if response.status_code == 500:
            raise VirusShareError("Internal server error (500): internal server error.")
        # Request rate limit exceeded (204)
        if response.status_code == 204:
            time.sleep(self.backoff)
            raise VirusShareError("Request rate limit exceeded (204). you are making more requests than are allowed or have exceeded your quota.")
        
        # On success (or other handled 2xx), return the raw Response
        return response

###################################################################################################

    # ================= File Report =================
    def file_report(self, hash_value: str) -> Dict[str, Any]:
        """Full structured information retrive about a sample (JSON)."""
        r = self._get("/file", hash_value=hash_value)
        if r.status_code == 200:
            try:
                return r.json()
            except json.JSONDecodeError as e:
                raise VirusShareError("Non-JSON response for /file") from e
        raise VirusShareError(f"Unexpected status for /file: {r.status_code}")

    # ================= Quick Status =================
    def quick_status(self, hash_value: str) -> int:
        """Lightweight existence/classification check, returns integer code."""
        r = self._get("/quick", hash_value=hash_value)
        if r.status_code == 200:
            try:
                data = r.json()
                return int(data.get("response"))
            except Exception as e:
                raise VirusShareError("Invalid /quick response") from e
        raise VirusShareError(f"Unexpected status for /quick: {r.status_code}")

    # ================= Source Info =================
    def source_info(self, hash_value: str) -> Dict[str, Any]:
        """Retrieve provenance/source data for a sample."""
        r = self._get("/source", hash_value=hash_value)
        if r.status_code == 200:
            try:
                return r.json()
            except json.JSONDecodeError as e:
                raise VirusShareError("Non-JSON response for /source") from e
        raise VirusShareError(f"Unexpected status for /source: {r.status_code}")

    # ================= Download Samples =================
    def download_sample(
        self,
        hash_value: str,
        *,
        dest_dir: str | Path = None,
        filename: Optional[str] = None
    ) -> Path:
        """Download the sample as a ZIP (stream to disk to avoid large memory usage)."""
        # Pre-check sample classification to avoid benign downloads
        file_info = self.file_report(hash_value)
        if file_info.get("response") == 2:
            raise VirusShareError("Sample classified as benign — download not allowed.")

        # Ensure destination directory exists
        dest = Path(dest_dir or settings.DOWNLOAD_DIR)
        dest.mkdir(parents=True, exist_ok=True)
        
        # Prepare output filename (default <hash>.zip)
        out_name = filename or f"{hash_value}.zip"
        out_path = dest / out_name

        # Request streaming download
        r = self._get("/download", hash_value=hash_value, stream=True)

        # Explicit not found handling
        if r.status_code == 404:
            raise VirusShareError("Sample not found (404) for /download.")
        # Guard against unexpected statuses
        if r.status_code != 200:
            raise VirusShareError(f"Unexpected status for /download: {r.status_code}")

        # Validate content-type; handle API error payloads
        ctype = r.headers.get("Content-Type", "")
        if "application/zip" not in ctype and "application/octet-stream" not in ctype:
            try:
                data = r.json()
                raise VirusShareError(f"Download error: {data}")
            except Exception:
                raise VirusShareError(f"Unexpected content type for /download: {ctype}")

        # Stream chunks to disk to keep memory footprint low
        with out_path.open("wb") as fh:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    fh.write(chunk)

        # Return final path to the downloaded ZIP
        return out_path

###################################################################################################
