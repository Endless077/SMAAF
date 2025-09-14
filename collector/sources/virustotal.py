#     ____   ____  _                         _________        _          __   
#    |_  _| |_  _|(_)                       |  _   _  |      / |_       [  |  
#      \ \   / /  __   _ .--.  __   _   .--.|_/ | | \_|.--. `| |-',--.   | |  
#       \ \ / /  [  | [ `/'`\][  | | | ( (`\]   | |  / .'`\ \| | `'_\ :  | |  
#        \ ' /    | |  | |     | \_/ |, `'.'.  _| |_ | \__. || |,// | |, | |  
#         \_/    [___][___]    '.__.'_/[\__) )|_____| '.__.' \__/\'-;__/[___] 
#                                                                             

"""
VirusTotal API Helper Module for Static Malware Analysis Framework (SMAF)
https://docs.virustotal.com/reference/overview

This module provides helper functions to interact with the VirusTotal API:
- Retrieve information about suspicious files via APIs.
- Retrieve information about suspicious URLs via APIs.
- Submit files or urls for a local APIs scanning.
- Download malware samples (premium only).

What is?
Online malware intelligence platform that aggregates antivirus engines, sandbox data,
and community contributions to provide file, URL, domain, and IP reputation.
"""

# VirusTotal
import vt
from vt.error import APIError

from configs.config import settings

###

import time
from pathlib import Path
from typing import Dict, Optional, Any

###################################################################################################

class VTClient:
    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        agent: str = "SMAF/VTClient",
        timeout: Optional[int] = None,
        verify_ssl: bool = True,
    ) -> None:
        
        # VirusTotal API Key
        self.api_key = api_key or settings.VT_API_KEY
        if not self.api_key:
            raise ValueError("VirusTotal API key not provided.")

        client_kwargs = {"apikey": self.api_key, "agent": agent, "verify_ssl": verify_ssl}
        
        # Timeout
        if timeout is not None:
            client_kwargs["timeout"] = timeout
        else:
            client_kwargs["timeout"] = settings.TIMEOUT
       
        # Open a VirusTotal Client
        self._client = vt.Client(**client_kwargs)

###################################################################################################

    # ================= Context Manager =================
    def __enter__(self) -> "VTClient":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    def close(self) -> None:
        if self._client:
            self._client.close()

    # ================= Helpers =================
    @staticmethod
    def _obj_to_dict(obj: vt.Object) -> Dict[str, Any]:
        return obj.to_dict()

    def _poll_analysis(self, analysis_id: str, *, interval: int = 10, max_wait: Optional[int] = None) -> Dict[str, Any]:
        start = time.time()
        while True:
            analysis = self._client.get_object("/analyses/{}", analysis_id)
            status = analysis.get("status")
            if status == "completed":
                return self._obj_to_dict(analysis)
            if max_wait is not None and (time.time() - start) >= max_wait:
                return self._obj_to_dict(analysis)
            time.sleep(interval)

###################################################################################################

    # ================= File Information =================
    def get_file_info(self, file_id: str) -> Dict[str, Any]:
        try:
            file_obj = self._client.get_object("/files/{}", file_id)
            return self._obj_to_dict(file_obj)
        except APIError as e:
            raise RuntimeError(f"VirusTotal API error (get_file_info): {e}") from e

    # ================= URL Information =================
    def get_url_info(self, url: str) -> Dict[str, Any]:
        try:
            url_id = vt.url_id(url)
            url_obj = self._client.get_object("/urls/{}", url_id)
            return self._obj_to_dict(url_obj)
        except APIError as e:
            raise RuntimeError(f"VirusTotal API error (get_url_info): {e}") from e

    # ================= Scan File =================
    def scan_file(
        self,
        filepath: str | Path,
        *,
        wait: bool = True,
        poll_interval: int = 10,
        max_wait: Optional[int] = None,
    ) -> Dict[str, Any]:
        path = Path(filepath)
        if not path.is_file():
            raise FileNotFoundError(f"File not found: {path}")
        try:
            with path.open("rb") as f:
                analysis = self._client.scan_file(f, wait_for_completion=False)
            analysis_id = analysis.id
            if wait:
                return self._poll_analysis(analysis_id, interval=poll_interval, max_wait=max_wait)
            return self._obj_to_dict(analysis)
        except APIError as e:
            raise RuntimeError(f"VirusTotal API error (scan_file): {e}") from e

    # ================= Scan URL =================
    def scan_url(
        self,
        url: str,
        *,
        wait: bool = True,
        poll_interval: int = 10,
        max_wait: Optional[int] = None,
    ) -> Dict[str, Any]:
        try:
            analysis = self._client.scan_url(url)
            analysis_id = analysis.id
            if wait:
                return self._poll_analysis(analysis_id, interval=poll_interval, max_wait=max_wait)
            return self._obj_to_dict(analysis)
        except APIError as e:
            raise RuntimeError(f"VirusTotal API error (scan_url): {e}") from e

    # # ================= Download File =================
    def download_file(self, file_hash: str, *, dest_dir: str | Path = None) -> str:
        dest = Path(dest_dir or settings.DOWNLOAD_DIR)
        dest.mkdir(parents=True, exist_ok=True)

        filename = None
        try:
            file_obj = self._client.get_object("/files/{}", file_hash)
            name = file_obj.get("meaningful_name") or (file_obj.get("names") or [None])[0]
            if name:
                filename = Path(name).name
        except APIError:
            pass
        if not filename:
            filename = f"{file_hash}.bin"

        out_path = dest / filename
        try:
            with out_path.open("wb") as fh:
                self._client.download_file(file_hash, fh)
        except APIError as e:
            if out_path.exists():
                try:
                    out_path.unlink()
                except OSError:
                    pass
            raise RuntimeError(f"VirusTotal API error (download_file): {e}") from e

        return str(out_path)

###################################################################################################
