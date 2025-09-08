"""
VirusTotal helper functions for Static Malware Analysis Framework (SMAF)

Implements:
1) Get info about a file (full JSON)
2) Get info about a URL (full JSON)
3) Scan a file (optionally wait until completed) and return analysis JSON
4) Scan a URL (optionally wait until completed) and return analysis JSON
5) Download a file by hash into ./download (uses meaningful name when available)

Usage example:

    from virustotal_client import VTClient

    with VTClient(api_key="<YOUR_API_KEY>") as vtcli:
        info = vtcli.get_file_info("44d88612fea8a8f36de82e1278abb02f")
        print(info)

        url_info = vtcli.get_url_info("http://www.virustotal.com")
        print(url_info)

        analysis = vtcli.scan_file("/path/to/file.bin", wait=True)
        print(analysis)

        analysis_url = vtcli.scan_url("https://example.org", wait=True)
        print(analysis_url)

        saved_path = vtcli.download_file("44d88612fea8a8f36de82e1278abb02f")
        print(f"Saved to {saved_path}")

Notes:
- Downloading files requires VirusTotal Premium access.
- All returned objects are plain Python dicts suitable for JSON serialization.
"""
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Dict, Optional

import vt
from vt.error import APIError

from configs.config import settings


class VTClient:
    """Thin wrapper around vt.Client with convenience methods."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        agent: str = "SMAF/VTClient",
        timeout: Optional[int] = None,
        verify_ssl: bool = True,
    ) -> None:
        self.api_key = api_key or settings.VT_API_KEY
        if not self.api_key:
            raise ValueError("VirusTotal API key not provided.")

        client_kwargs = {"apikey": self.api_key, "agent": agent, "verify_ssl": verify_ssl}
        if timeout is not None:
            client_kwargs["timeout"] = timeout
        else:
            client_kwargs["timeout"] = settings.TIMEOUT  # puoi usare anche TIMEOUT da config
        self._client = vt.Client(**client_kwargs)

    # Context manager support -------------------------------------------------
    def __enter__(self) -> "VTClient":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    def close(self) -> None:
        if self._client:
            self._client.close()

    # Helpers -----------------------------------------------------------------
    @staticmethod
    def _obj_to_dict(obj: vt.Object) -> Dict[str, Any]:
        """Return the full object as a dict in VirusTotal API shape."""
        return obj.to_dict()

    def _poll_analysis(self, analysis_id: str, *, interval: int = 10, max_wait: Optional[int] = None) -> Dict[str, Any]:
        """Poll an analysis object until status == 'completed'.

        Parameters
        ----------
        analysis_id : str
            The ID returned by scan_file/scan_url.
        interval : int
            Seconds to wait between polls.
        max_wait : int | None
            Optional maximum seconds to wait; if exceeded, the latest state is returned.
        """
        start = time.time()
        while True:
            analysis = self._client.get_object("/analyses/{}", analysis_id)
            status = analysis.get("status")
            if status == "completed":
                return self._obj_to_dict(analysis)
            if max_wait is not None and (time.time() - start) >= max_wait:
                return self._obj_to_dict(analysis)
            time.sleep(interval)

    # 1) Get information about a file ----------------------------------------
    def get_file_info(self, file_id: str) -> Dict[str, Any]:
        """Return full JSON for a file object by hash or ID.

        `file_id` can be a SHA-256, SHA-1, or MD5 of the file.
        """
        try:
            file_obj = self._client.get_object("/files/{}", file_id)
            return self._obj_to_dict(file_obj)
        except APIError as e:
            raise RuntimeError(f"VirusTotal API error (get_file_info): {e}") from e

    # 2) Get information about a URL -----------------------------------------
    def get_url_info(self, url: str) -> Dict[str, Any]:
        """Return full JSON for a URL object.

        Uses vt.url_id(url) as required by the API.
        """
        try:
            url_id = vt.url_id(url)
            url_obj = self._client.get_object("/urls/{}", url_id)
            return self._obj_to_dict(url_obj)
        except APIError as e:
            raise RuntimeError(f"VirusTotal API error (get_url_info): {e}") from e

    # 3) Scan a file ----------------------------------------------------------
    def scan_file(
        self,
        filepath: str | Path,
        *,
        wait: bool = True,
        poll_interval: int = 10,
        max_wait: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Upload & scan a file. Returns the analysis object as dict.

        If `wait` is True, waits until analysis completes and returns final state.
        Otherwise returns the initial analysis object (likely without attributes).
        """
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

    # 4) Scan a URL -----------------------------------------------------------
    def scan_url(
        self,
        url: str,
        *,
        wait: bool = True,
        poll_interval: int = 10,
        max_wait: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Submit a URL for scanning. Returns the analysis object as dict."""
        try:
            analysis = self._client.scan_url(url)
            analysis_id = analysis.id
            if wait:
                return self._poll_analysis(analysis_id, interval=poll_interval, max_wait=max_wait)
            return self._obj_to_dict(analysis)
        except APIError as e:
            raise RuntimeError(f"VirusTotal API error (scan_url): {e}") from e

    # 5) Download a file ------------------------------------------------------
    def download_file(self, file_hash: str, *, dest_dir: str | Path = None) -> str:
        """Download a file by hash into `dest_dir` (default: settings.DOWNLOAD_DIR)."""
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