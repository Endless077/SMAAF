#!/usr/bin/env python3
# -*- coding: utf-8 -*-                                         

#     _____  _____  _    _   __    _   _    _                
#    |_   _||_   _|/ |_ (_) [  |  (_) / |_ (_)               
#      | |    | | `| |-'__   | |  __ `| |-'__  .---.  .--.   
#      | '    ' |  | | [  |  | | [  | | | [  |/ /__\\( (`\]  
#       \ \__/ /   | |, | |  | |  | | | |, | || \__., `'.'.  
#        `.__.'    \__/[___][___][___]\__/[___]'.__.'[\__) ) 
#                                                            

from __future__ import annotations

import re
import json
from pathlib import Path
from typing import Tuple, Dict, Optional, Any

###################################################################################################

# ================= Utilities =================
def convert_hex(n: Optional[int]) -> Optional[str]:
    """Convert integer to hexadecimal."""
    return None if n is None else f"0x{int(n):x}"

def slugify(name: str, maxlen: int = 48) -> str:
    """Set a safe filename."""
    name = (name or "").strip().replace(" ", "_")
    name = re.sub(r"[^A-Za-z0-9_\-\.]+", "", name)
    return (name or "func")[:maxlen]

def relative_path(base_dir: Path, target: Optional[Path]) -> Optional[str]:
    """Relative path to."""
    if target is None:
        return None
    try:
        return str(target.relative_to(base_dir))
    except Exception:
        return str(target)

def write_text(path: Path, text: str) -> Optional[str]:
    """Write a text file."""
    try:
        path.write_text(text or "", encoding="utf-8")
        return str(path)
    except Exception:
        return None
    
def write_json(path: Path, obj: Dict[str, Any]) -> str:
    """Write a json file."""
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(path)

###################################################################################################

# ================= Utilities (Ghidra) =================
def make_ghidra_dirs(output_root: str, src_path: Path) -> Tuple[Path, Path, Path, Path]:
    """Make Ghidra directories tree."""
    base_dir = Path(output_root) / src_path.stem / "ghidra"
    asm_dir = base_dir / "asm"
    c_dir = base_dir / "c"

    asm_dir.mkdir(parents=True, exist_ok=True)
    c_dir.mkdir(parents=True, exist_ok=True)

    json_path = base_dir / "disassembly_metadata.json"

    return base_dir, json_path, asm_dir, c_dir

###################################################################################################

# ================= Utilities (radare2) =================
def make_radare_dirs(output_root: str, src_path: Path) -> Tuple[Path, Path, Path, Path]:
    """Make radare2 directories tree."""
    base_dir = Path(output_root) / src_path.stem / "radare2"
    asm_dir = base_dir / "asm"
    c_dir = base_dir / "c"

    asm_dir.mkdir(parents=True, exist_ok=True)
    c_dir.mkdir(parents=True, exist_ok=True)

    json_path = base_dir / f"disassembly_metadata.json"

    return base_dir, json_path, asm_dir, c_dir

###################################################################################################