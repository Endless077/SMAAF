"""
VirusShare API v2 client for Static Malware Analysis Framework (SMAF)

Implements all public endpoints documented at:
- https://virusshare.com/apiv2_reference

Endpoints used:
- /file      -> Retrieve file report (metadata, VT summary, etc.)
- /download  -> Download a sample (ZIP, password 'infected')
- /quick     -> Quick status (0 unknown, 1 malware, 2 benign)
- /source    -> Source info (URL crawl history) [sha256 only]

Notes:
- All requests: GET with query params: apikey=<key>, hash=<hash>
- Rate limiting returns HTTP 204; caller should backoff
- Downloads are returned as a password-protected ZIP; we do NOT unzip here
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

import json
import time
import requests

from configs.config import settings

API_BASE = "https://virusshare.com/apiv2"

class VirusShareError(RuntimeError):
    pass

@dataclass
class VSClient:
    api_key: Optional[str] = None
    timeout: Optional[int] = None
    backoff_seconds: float = 1.5
    user_agent: str = "SMAF/VSClient"

    def __post_init__(self) -> None:
        self.api_key = self.api_key or settings.VS_API_KEY
        if not self.api_key:
            raise VirusShareError("VirusShare API key not provided.")
        self.timeout = self.timeout or settings.TIMEOUT
        self._session = requests.Session()
        self._session.headers.update({"User-Agent": self.user_agent})

    # --------------------------- Core helpers ---------------------------------
    def _get(self, endpoint: str, *, hash_value: str, stream: bool = False) -> requests.Response:
        url = f"{API_BASE}{endpoint}"
        params = {"apikey": self.api_key, "hash": hash_value}
        try:
            resp = self._session.get(url, params=params, timeout=self.timeout, stream=stream)
        except requests.RequestException as e:
            raise VirusShareError(f"HTTP error contacting VirusShare: {e}") from e

        if resp.status_code == 204:
            # Rate limited — give the caller a hint and optional delay
            time.sleep(self.backoff_seconds)
            raise VirusShareError("Rate limit exceeded (204). Please backoff and retry.")
        if resp.status_code == 403:
            raise VirusShareError("Forbidden (403): invalid or unauthorized API key.")
        if resp.status_code == 400:
            raise VirusShareError("Bad request (400): missing or incorrect parameters.")
        if resp.status_code == 503:
            raise VirusShareError("Service unavailable (503): try again later.")
        # 404 is expected for missing downloads (not found), caller will handle
        return resp

    # --------------------------- API methods ----------------------------------
    def file_report(self, hash_value: str) -> Dict[str, Any]:
        """/file — Retrieve the JSON report for a given hash (md5/sha1/sha2* supported).

        Returns the full JSON dict as delivered by VirusShare, including 'response'.
        """
        r = self._get("/file", hash_value=hash_value)
        if r.status_code == 200:
            try:
                return r.json()
            except json.JSONDecodeError as e:
                raise VirusShareError("Non-JSON response for /file") from e
        raise VirusShareError(f"Unexpected status for /file: {r.status_code}")

    def quick_status(self, hash_value: str) -> int:
        """/quick — Return 0 (unknown), 1 (malware), or 2 (benign)."""
        r = self._get("/quick", hash_value=hash_value)
        if r.status_code == 200:
            try:
                data = r.json()
                return int(data.get("response"))
            except Exception as e:
                raise VirusShareError("Invalid /quick response") from e
        raise VirusShareError(f"Unexpected status for /quick: {r.status_code}")

    def source_info(self, sha256: str) -> Dict[str, Any]:
        """/source — Retrieve crawler URL/timestamp history for a SHA256.

        The API supports SHA256 only.
        """
        r = self._get("/source", hash_value=sha256)
        if r.status_code == 200:
            try:
                return r.json()
            except json.JSONDecodeError as e:
                raise VirusShareError("Non-JSON response for /source") from e
        raise VirusShareError(f"Unexpected status for /source: {r.status_code}")

    def download_sample(self, hash_value: str, *, dest_dir: str | Path = None, filename: Optional[str] = None) -> Path:
        """/download — Download sample ZIP (password 'infected'). Returns saved path.

        Benign (response=2) samples are not available for download.
        """
        dest = Path(dest_dir or settings.DOWNLOAD_DIR)
        dest.mkdir(parents=True, exist_ok=True)
        out_name = filename or f"{hash_value}.zip"
        out_path = dest / out_name

        r = self._get("/download", hash_value=hash_value, stream=True)
        if r.status_code == 404:
            raise VirusShareError("Sample not found (404) for /download.")
        if r.status_code != 200:
            raise VirusShareError(f"Unexpected status for /download: {r.status_code}")

        # Heuristically check content type: file is binary zip
        ctype = r.headers.get("Content-Type", "")
        if "application/zip" not in ctype and "application/octet-stream" not in ctype:
            # Might be an error JSON; try to parse
            try:
                data = r.json()
                raise VirusShareError(f"Download error: {data}")
            except Exception:
                raise VirusShareError(f"Unexpected content type for /download: {ctype}")

        with out_path.open("wb") as fh:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    fh.write(chunk)
        return out_path
