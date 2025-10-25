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

# ───────────────────────────────────────────────────────────────
# Third-party libraries
import requests
import vt
from vt.error import APIError

# ───────────────────────────────────────────────────────────────
# Local application imports
from collector.configs.config import settings

# ───────────────────────────────────────────────────────────────
# Standard library
import asyncio
import sys
import time
from pathlib import Path
from typing import Any, Dict, Optional

###################################################################################################

class VTClient:
    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        timeout: Optional[int] = None,
        user_agent: Optional[str] = None,
    ) -> None:
        # Load VirusTotal API key
        self.api_key = api_key or settings.VT_API_KEY
        if not self.api_key:
            raise ValueError("VirusTotal API key not provided.")

        # Store optional user agent
        self.user_agent = (
            user_agent
            or f"SMAF-VTClient/1.0 requests/{requests.__version__} "
               f"Python/{sys.version_info.major}.{sys.version_info.minor}"
        )

        # Optional timeout
        self.timeout = timeout or settings.TIMEOUT
        
        # Initialize VirusTotal client
        self._client = vt.Client(self.api_key)

###################################################################################################

    # ================= Context Manager =================
    async def __enter__(self) -> "VTClient":
        return self

    async def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    # Close underlying resources
    def close(self):
        try:
            if hasattr(self._client, "close_async") and callable(self._client.close_async):
                # Loop detected, start the async safe close
                # Schedule async close if loop is running
                try:
                    loop = asyncio.get_running_loop()
                    loop.create_task(self._client.close_async())
                except RuntimeError:
                    # No running loop: run it synchronously
                    asyncio.run(self._client.close_async())
            elif hasattr(self._client, "close"):
                self._client.close()
        except Exception:
            pass

    # ================= Helpers =================
    # Convert VT Object to dictionary
    @staticmethod
    def _obj_to_dict(obj: vt.Object) -> Dict[str, Any]:
        return obj.to_dict()

    # Poll an analysis until completion or timeout
    async def _poll_analysis(
        self, analysis_id: str, *, interval: int = 10, max_wait: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Poll until VirusTotal analysis completes.
        """
        start = time.time()
        while True:
            analysis = await self._client.get_object_async(f"/analyses/{analysis_id}")
            status = analysis.get("status")
            if status == "completed":
                return self._obj_to_dict(analysis)
            if max_wait is not None and (time.time() - start) >= max_wait:
                return self._obj_to_dict(analysis)
            await asyncio.sleep(interval)

###################################################################################################

    # ================= File Information =================
    async def get_file_info(self, sample: str) -> Dict[str, Any]:
        """
        Retrieve detailed information about a file by hash.
        """
        try:
            file_obj = await self._client.get_object_async(f"/files/{sample}")
            return self._obj_to_dict(file_obj)
        except APIError as e:
            raise RuntimeError(f"VirusTotal API error (get_file_info): {e}") from e

    # ================= URL Information =================
    async def get_url_info(self, url: str) -> Dict[str, Any]:
        """
        Retrieve detailed information about a URL.
        """
        try:
            url_id = vt.url_id(url)
            url_obj = await self._client.get_object_async(f"/urls/{url_id}")
            return self._obj_to_dict(url_obj)
        except APIError as e:
            raise RuntimeError(f"VirusTotal API error (get_url_info): {e}") from e

    # ================= Scan File =================
    async def scan_file(
        self,
        filepath: str | Path,
        *,
        wait: bool = True,
        poll_interval: int = 10,
        max_wait: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Submit and scan a file, optionally wait for completion.
        """
        path = Path(filepath)
        if not path.is_file():
            raise FileNotFoundError(f"File not found: {path}")
        try:
            async with path.open("rb") as f:
                analysis = await self._client.scan_file_async(f)
            analysis_id = analysis.id
            if wait:
                return await self._poll_analysis(analysis_id, interval=poll_interval, max_wait=max_wait)
            return self._obj_to_dict(analysis)
        except APIError as e:
            raise RuntimeError(f"VirusTotal API error (scan_file): {e}") from e

    # ================= Scan URL =================
    async def scan_url(
        self,
        url: str,
        *,
        wait: bool = True,
        poll_interval: int = 10,
        max_wait: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Submit and scan a URL, optionally wait for completion.
        """
        try:
            analysis = await self._client.scan_url_async(url)
            analysis_id = analysis.id
            if wait:
                return await self._poll_analysis(analysis_id, interval=poll_interval, max_wait=max_wait)
            return self._obj_to_dict(analysis)
        except APIError as e:
            raise RuntimeError(f"VirusTotal API error (scan_url): {e}") from e

    # ================= Download File =================
    async def download_file(self, file_hash: str, *, dest_dir: str | Path = None) -> str:
        """
        Download a file by hash and save it locally.
        """
        dest = Path(dest_dir or settings.DOWNLOAD_DIR)
        dest.mkdir(parents=True, exist_ok=True)

        # 1) Filename recovery
        filename: Optional[str] = None
        try:
            file_obj = await self._client.get_object_async(f"/files/{file_hash}")
            name = file_obj.get("meaningful_name") or (file_obj.get("names") or [None])[0]
            if name:
                filename = Path(name).name
        except APIError:
            pass
        if not filename:
            filename = f"{file_hash}.bin"

        out_path = dest / filename

        # 2) Synchronous download to threadpool to not block the loop
        async def _download_sync():
            try:
                with vt.Client(self.api_key, timeout=self.timeout) as c:
                    with out_path.open("wb") as fh:
                        c.download_file(file_hash, fh)
            except APIError as e:
                # Partial cleanup on error
                if out_path.exists():
                    try:
                        out_path.unlink()
                    except OSError:
                        pass
                raise RuntimeError(f"VirusTotal API error (download_file): {e}") from e

        await asyncio.to_thread(_download_sync)

        return str(out_path)
        
###################################################################################################
