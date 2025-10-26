#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#       ______  __        _        __                 
#     .' ___  |[  |      (_)      |  ]                
#    / .'   \_| | |--.   __   .--.| |  _ .--.  ,--.   
#    | |   ____ | .-. | [  |/ /'`\' | [ `/'`\]`'_\ :  
#    \ `.___]  || | | |  | || \__/  |  | |    // | |, 
#     `._____.'[___]|__][___]'.__.;__][___]   \'-;__/ 
#                                                     

from __future__ import annotations

# ───────────────────────────────────────────────────────────────
# Local application imports
from disassembler.utilities import *
from utils.logger import setup_logging

# ───────────────────────────────────────────────────────────────
# Standard library
import argparse
import logging
import os
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

###################################################################################################

# ================= Helpers =================
def _resolve_analyze_headless(ghidra: str | None) -> str:
    """
    Resolve path to Ghidra's analyzeHeadless.
    """
    if ghidra:
        cand = Path(ghidra) / "support" / ("analyzeHeadless.bat" if os.name == "nt" else "analyzeHeadless")
        if cand.exists():
            return str(cand)
        raise FileNotFoundError(f"analyzeHeadless not found under: {ghidra}")
    
    # No path provided: must be in PATH
    exe = "analyzeHeadless"

    if shutil.which(exe) is None:
        raise FileNotFoundError("analyzeHeadless not found.")
    
    return exe

###################################################################################################

# ================= Disassemble =================
def disassemble_ghidra(
    file_path: str,
    ghidra: str | None = None,
    scripts: str | None = None,
    output: str = "disassembled",
    keep_project: bool = False
    ):
    """
    Run Ghidra in headless mode with 'script.py'.
    """
    src = Path(file_path).expanduser().resolve()
    if not src.exists() or not src.is_file():
        raise FileNotFoundError(f"File not found: {src}")

    # Create output tree: disassembled/<stem>/ghidra/
    base_dir, json_path, asm_dir, c_dir = make_ghidra_dirs(output, src)
    logging.info("Output directory prepared: %s", base_dir)

    # Script ghidra_extract.py must be alongside this file (or --scripts-dir)
    script_file = Path(scripts).expanduser().resolve() / "script.py" if scripts else Path(__file__).with_name("script.py")
    if not script_file.exists():
        raise FileNotFoundError(f"Ghidra script not found: {script_file}")

    # Prepare temporary project folder required by Ghidra
    tmp_proj_dir = base_dir / ".ghidra_project"
    tmp_proj_dir.mkdir(parents=True, exist_ok=True)
    proj_name = f"proj_{src.stem}"

    # Resolve analyzeHeadless
    analyze = _resolve_analyze_headless(ghidra)

    cmd = [
        analyze,
        str(tmp_proj_dir),
        proj_name,
        "-import", str(src),
        "-deleteProject",
        "-overwrite", 
        "-scriptPath", str(script_file.parent),
        "-postScript", script_file.name, str(base_dir)
    ]

    logging.info("Running Ghidra headless...")
    logging.debug("Command: %s", " ".join(shlex.quote(c) for c in cmd))

    try:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )

        for line in proc.stdout:
            sys.stdout.write(line)
            sys.stdout.flush()
            logging.debug(line.strip())

        proc.wait()

        if proc.returncode != 0:
            raise RuntimeError(f"Ghidra headless failed (code {proc.returncode})")
        
    finally:
        if not keep_project and tmp_proj_dir.exists():
            for p in sorted(tmp_proj_dir.rglob("*"), reverse=True):
                if p.is_file() or p.is_symlink():
                    p.unlink(missing_ok=True)
                else:
                    p.rmdir()
            tmp_proj_dir.rmdir()

    if not json_path.exists():
        raise FileNotFoundError(f"Ghidra script did not produce JSON: {json_path}")

    logging.info("Metadata JSON written: %s", json_path)

###################################################################################################

def _cli() -> None:
    """
    Command-line interface for Ghidra disassembly module.
    """
    parser = argparse.ArgumentParser(description="Extract metadata from disassembly (ghidra)")
    parser.add_argument("file", help="Target binary path to analyze.")
    parser.add_argument("--output", default="disassembled", help="Results output directory.")
    parser.add_argument("--ghidra", required=True, help="Path to Ghidra's home.")
    parser.add_argument("--scripts", required=True, help="Directory containing useful Ghidra scripts.")
    parser.add_argument("--keep-project", action="store_true", help="Do not delete temporary Ghidra project folder.")
    
    args = parser.parse_args()

    # Startup logs
    setup_logging()

    logging.info(f"Using Ghidra path: {args.ghidra}")
    logging.info(f"Using scripts directory: {args.scripts}")
    logging.info(f"Ghidra disassembly file: {args.file}")

    # Startup disassemble with Ghidra
    try:
        disassemble_ghidra(
            args.file,
            ghidra=args.ghidra,
            scripts=args.scripts,
            output=args.output,
            keep_project=args.keep_project
        )
        logging.info(f"Ghidra disassembly complete, results saved in: {args.output}")
    except Exception as e:
        logging.exception("Ghidra disassembly process failed: %s", e)
        sys.exit(1)

if __name__ == "__main__":
    _cli()

###################################################################################################
