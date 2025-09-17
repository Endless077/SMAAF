#      _____                                           
#     |_   _|                                          
#       | |       .--.   .--./)  .--./) .---.  _ .--.  
#       | |   _ / .'`\ \/ /'`\; / /'`\;/ /__\\[ `/'`\] 
#      _| |__/ || \__. |\ \._// \ \._//| \__., | |     
#     |________| '.__.' .',__`  .',__`  '.__.'[___]    
#                      ( ( __))( ( __))                

import os
import sys
import logging
from pathlib import Path
from typing import Union
from datetime import datetime

###################################################################################################

def setup_logging(
    file: Union[bool, str, None] = None,
    level: int = logging.INFO,
) -> str | None:
    """
    Initialize application logging.

    Args:
        file:
            - False/None -> force console only.
            - True  -> file with timestamp (.log).
            - str   -> custom file path (absolute path).

        level: logging level (default: INFO)

    Returns:
        The log file path if a file is used, otherwise None.
    """
    root = logging.getLogger()
    for h in list(root.handlers):
        root.removeHandler(h)

    log_filename: str | None = None
    handlers = [logging.StreamHandler(sys.stdout)]

    if file:
        logs_dir = Path("logs")
        os.makedirs(logs_dir, exist_ok=True)

        if isinstance(file, str):
            log_filename = file
        else:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_filename = str(logs_dir / f"log_{timestamp}.log")

        handlers.append(logging.FileHandler(log_filename, encoding="utf-8"))

    logging.basicConfig(
        level=level,
        format='[LOG] %(levelname)s - %(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=handlers,
    )

    if log_filename:
        logging.info(f"Logging configured with file: {log_filename}")
    else:
        logging.info("Logging configured to console only.")

    return log_filename

###################################################################################################
