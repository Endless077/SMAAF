#       ______                     ___  _          
#     .' ___  |                  .' ..](_)         
#    / .'   \_|  .--.   _ .--.  _| |_  __   .--./) 
#    | |       / .'`\ \[ `.-. |'-| |-'[  | / /'`\; 
#    \ `.___.'\| \__. | | | | |  | |   | | \ \._// 
#     `.____ .' '.__.' [___||__][___] [___].',__`  
#                                         ( ( __)) 

"""
This module centralizes API keys, directories, and global settings
for providers like VirusTotal, MalwareBazaar, VirusShare, Hybrid-Analysis.

Usage example:

    from config import settings
    print(settings.VT_API_KEY)

All configuration values can be overridden via environment variables and
this ensures secrets are not hardcoded in the source.
"""
import os
from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    # External Providers API Keys
    VT_API_KEY: str = os.getenv("VT_API_KEY", "")
    VS_API_KEY: str = os.getenv("VS_API_KEY", "")
    MB_API_KEY: str = os.getenv("MB_API_KEY", "")

    PROVIDERS = {"virustotal", "virusshare", "malwarebazaar"}

    # Project Directoires
    BASE_DIR: Path = Path(os.getenv("SMAF_BASE_DIR", Path.cwd()))
    DOWNLOAD_DIR: Path = BASE_DIR / os.getenv("SMAF_DOWNLOAD_DIR", "download")
    SAMPLES_DIR: Path = BASE_DIR / os.getenv("SMAF_STORAGE_DIR", "samples")

# Global settings object
settings = Settings()

# Setup directories
settings.DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
settings.SAMPLES_DIR.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    import json
    print(json.dumps(settings.__dict__, indent=2, default=str))
