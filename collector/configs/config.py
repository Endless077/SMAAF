#       ______                     ___  _          
#     .' ___  |                  .' ..](_)         
#    / .'   \_|  .--.   _ .--.  _| |_  __   .--./) 
#    | |       / .'`\ \[ `.-. |'-| |-'[  | / /'`\; 
#    \ `.___.'\| \__. | | | | |  | |   | | \ \._// 
#     `.____ .' '.__.' [___||__][___] [___].',__`  
#                                         ( ( __)) 

"""
This module centralizes API keys, directories, and global settings.

All configuration values can be overridden via environment variables and
this ensures secrets are not hardcoded in the source.
"""

import json
import os

from enum import Enum
from typing import Dict
from pathlib import Path
from datetime import datetime

from dataclasses import dataclass, field

from utils.logger import setup_logging

###################################################################################################

class Providers(str, Enum):
    virustotal = "VirusTotal"
    virusshare = "VirusShare"
    malwarebazaar = "MalwareBazaar"

###################################################################################################


# Init Logging
def init_logging(file=None, level=None):
    """
    Initialize logging using a project-wide logs directory.

    Args:
        file:
            - False/None -> force console only.
            - True  -> file with timestamp (.log).
            - str   -> custom file path (absolute path).
        level: logging level (default: INFO)
    """
    log_path_str = None

    if file:
        if file is True:
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_path = settings.LOGS_DIR / f"log_{ts}.log"
        elif isinstance(file, str):
            p = Path(file)
            log_path = p if p.is_absolute() else settings.LOGS_DIR / p
        else:
            log_path = None

        if log_path is not None:
            log_path.parent.mkdir(parents=True, exist_ok=True)
            log_path_str = str(log_path)

    kwargs = {}
    if level is not None:
        kwargs["level"] = level

    return setup_logging(file=log_path_str if log_path_str else file, **kwargs)

###################################################################################################

@dataclass(frozen=True)
class Settings:
    # External Providers API Keys
    VT_API_KEY: str = os.getenv("VT_API_KEY", "")
    VS_API_KEY: str = os.getenv("VS_API_KEY", "")
    MB_API_KEY: str = os.getenv("MB_API_KEY", "")

    # Providers and their storage directories
    PROVIDER_DIR_MAP: Dict[str, str] = field(default_factory=lambda: {
        "VirusTotal": "virustotal",
        "VirusShare": "virusshare",
        "MalwareBazaar": "malwarebazaar",
    })

    # Networking
    TIMEOUT: int = 300

    # Project Directories
    BASE_DIR: Path = Path(os.getenv("SMAF_BASE_DIR", Path.cwd()))
    LOGS_DIR: Path = BASE_DIR / os.getenv("SMAF_LOG_DIR", "logs")
    SAMPLES_DIR: Path = BASE_DIR / os.getenv("SMAF_STORAGE_DIR", "samples")
    DOWNLOAD_DIR: Path = BASE_DIR / os.getenv("SMAF_DOWNLOAD_DIR", "download")

    VIRUSTOTAL_DL_DIR: Path = BASE_DIR / os.getenv("VT_DOWNLOAD_DIR", "download/virustotal")
    VIRUSSHARE_DL_DIR: Path = BASE_DIR / os.getenv("VS_DOWNLOAD_DIR", "download/virusshare")
    MALWAREBAZAAR_DL_DIR: Path = BASE_DIR / os.getenv("MB_DOWNLOAD_DIR", "download/malwarebazaar")

# Global settings object
settings = Settings()

# Ensure directories exist
settings.LOGS_DIR.mkdir(parents=True, exist_ok=True)
settings.SAMPLES_DIR.mkdir(parents=True, exist_ok=True)
settings.DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
settings.VIRUSTOTAL_DL_DIR.mkdir(parents=True, exist_ok=True)
settings.VIRUSSHARE_DL_DIR.mkdir(parents=True, exist_ok=True)
settings.MALWAREBAZAAR_DL_DIR.mkdir(parents=True, exist_ok=True)

os.chmod(settings.LOGS_DIR, 0o770)
os.chmod(settings.SAMPLES_DIR, 0o770)
os.chmod(settings.DOWNLOAD_DIR, 0o770)

###################################################################################################

# Testing Main
if __name__ == "__main__":
    # Logging initialization
    init_logging()

    # Print the config class
    print(json.dumps(settings.__dict__, indent=2, default=str))
