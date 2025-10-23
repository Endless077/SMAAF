#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#                          __                         _____   
#                         |  ]                       / ___ `. 
#     _ .--.  ,--.    .--.| |  ,--.   _ .--.  .---. |_/___) | 
#    [ `/'`\]`'_\ : / /'`\' | `'_\ : [ `/'`\]/ /__\\ .'____.' 
#     | |    // | |,| \__/  | // | |, | |    | \__.,/ /_____  
#    [___]   \'-;__/ '.__.;__]\'-;__/[___]    '.__.'|_______| 
#                    

from __future__ import annotations

import json
import logging
import argparse
from pathlib import Path
from datetime import datetime, timezone
from typing import List, Dict, Optional, Any

import r2pipe

from utils.logger import setup_logging

from utilities import *

###################################################################################################

# ================= Helpers =================
def _detect_basic_info(r2) -> Dict[str, Any]:
    """Extract and read binary/asm info via 'ij' (JSON)."""
    try:
        ij = json.loads(r2.cmd("ij"))
        bininfo = ij.get("bin", {}) or {}
        core = ij.get("core", {}) or {}
        asm = ij.get("asm", {}) or {}
        return {
            "arch": bininfo.get("arch"),
            "bits": bininfo.get("bits"),
            "endian": bininfo.get("endian"),
            "format": bininfo.get("bintype") or bininfo.get("format"),
            "os": bininfo.get("os"),
            "class": bininfo.get("class"),
            "machine": bininfo.get("machine"),
            "entrypoint": convert_hex(bininfo.get("entry")),
            "va": core.get("va"),
            "asm_syntax": asm.get("syntax"),
            "r2_version": core.get("version"),
        }
    except Exception as e:
        logging.warning("Failed to read basic info with 'ij': %s", e)
        return {}

def _list_functions(r2) -> List[Dict[str, Any]]:
    """Get functions via 'aflj', ordered by offset."""
    try:
        fun = json.loads(r2.cmd("aflj")) or []
        fun.sort(key=lambda f: f.get("offset", 0))
        return fun
    except Exception as e:
        logging.error("Failed to list functions with 'aflj': %s", e)
        return []

def _list_sections(r2) -> List[Dict[str, Any]]:
    """Get sections via 'iSj' (normalized)."""
    try:
        sec = json.loads(r2.cmd("iSj")) or []
        return [
            {
                "name": s.get("name"),
                "vaddr": convert_hex(s.get("vaddr")),
                "paddr": convert_hex(s.get("paddr")),
                "size": s.get("size"),
                "perm": s.get("perm"),
                "addralign": s.get("addralign"),
                "type": s.get("type"),
            }
            for s in sec
        ]
    except Exception as e:
        logging.warning("Failed to list sections with 'iSj': %s", e)
        return []

def _sections_focus(sections: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Summarize .text and .data if present (no code content)."""
    focus: Dict[str, Any] = {}
    for target in (".text", ".data"):
        match = next((s for s in sections if s.get("name") == target), None)
        if not match:
            match = next((s for s in sections if s.get("name") and target.strip(".") in s["name"]), None)
        if match:
            focus[target] = {
                "name": match.get("name"),
                "vaddr": match.get("vaddr"),
                "size": match.get("size"),
                "perm": match.get("perm"),
                "type": match.get("type"),
            }
    return focus

def _get_function_disasm_text(r2, addr: int) -> str:
    """Assembly text of the function via 'pdf' (print disasm function)."""
    try:
        return r2.cmd(f"pdf @ {addr}") or ""
    except Exception as e:
        logging.warning("Failed 'pdf' at 0x%x: %s", addr if isinstance(addr, int) else -1, e)
        return ""

def _decompile_text(r2, addr: int) -> Optional[str]:
    """Try to get C-like pseudocode using pdc (r2ghidra-dec) or pdd (r2dec)."""
    try:
        r2.cmd(f"s {addr}")
    except Exception:
        return None

    # Try r2ghidra-dec (pdc)
    try:
        out = r2.cmd(f"pdc @ {addr}")
        if out and "Unknown command" not in out and "Cannot find" not in out:
            return out
    except Exception:
        pass

    # Try to r2dec (pdd)
    try:
        out = r2.cmd(f"pdd @ {addr}")
        if out and "Unknown command" not in out and "Cannot find" not in out:
            return out
    except Exception:
        pass

    logging.debug("No decompiler output available at %s", convert_hex(addr))
    return None

###################################################################################################

# ================= Disassemble =================
def disassemble_radare2(
    file_path: str,
    output_root: str = "disassembled"
    ):
    """Disassemble via radare2 framework."""
    src = Path(file_path).expanduser().resolve()

    # Validate target file path
    if not src.exists():
        raise FileNotFoundError(f"File not found: {src}")
    if not src.is_file():
        raise IsADirectoryError(f"Target is not a file: {src}")

    # Prepare output tree
    base_dir, json_path, asm_dir, c_dir = make_radare_dirs(output_root, src)
    logging.info("Output directory prepared: %s", base_dir)

    # Open r2 in headless mode
    try:
        r2 = r2pipe.open(str(src), flags=["-2"])
    except FileNotFoundError as e:
        logging.error("radare2 not found.")
        raise SystemExit("Error: radare2 not found.") from e

    try:
        logging.info("Full deep radare2 analysis (aaa): %s", src.name)
        r2.cmd("e scr.color=false")
        r2.cmd("aaa")

        info = _detect_basic_info(r2)
        sections = _list_sections(r2)
        focus = _sections_focus(sections)

        funs = _list_functions(r2)
        if not funs:
            logging.warning("No functions detected by 'aflj'.")

        functions_meta: List[Dict[str, Any]] = []
        for idx, f in enumerate(funs, start=1):
            addr = f.get("offset")
            name = f.get("name") or "func"
            size = f.get("size")
            off_hex = convert_hex(addr) if addr is not None else None

            slug = slugify(name)
            idx_str = str(idx).zfill(5)
            off_tag = (off_hex or "0x0").replace("0x", "")

            # Dump assembly to file (if available)
            asm_file = asm_dir / f"{idx_str}_{off_tag}_{slug}.asm"
            asm_text = _get_function_disasm_text(r2, addr) if isinstance(addr, int) else ""
            asm_written = write_text(asm_file, asm_text)
            if asm_written:
                logging.debug("ASM written: %s", asm_written)
            else:
                logging.warning("Failed to write ASM file for function: %s", name)

            # Dump pseudocode (if available)
            c_written: Optional[str] = None
            pseudo = _decompile_text(r2, addr) if isinstance(addr, int) else None
            if pseudo:
                c_file = c_dir / f"{idx_str}_{off_tag}_{slug}.c"
                c_written = write_text(c_file, pseudo)
                if c_written:
                    logging.debug("C pseudocode written: %s", c_written)
                else:
                    logging.warning("Failed to write pseudocode file for function: %s", name)
            else:
                logging.info("No pseudocode available for: %s", name)

            functions_meta.append({
                "index": idx,
                "name": name,
                "offset": off_hex,
                "size": size,
                "asm_file": relative_path(base_dir, Path(asm_written)) if asm_written else None,
                "pseudocode_file": relative_path(base_dir, Path(c_written)) if c_written else None,
            })

        result: Dict[str, Any] = {
            "input_file": str(src),
            "output_base_dir": str(base_dir),
            "analysis_tool": "radare2",
            "basic_info": info,
            "sections": sections,
            "sections_focus": focus,
            "counts": {
                "functions": len(functions_meta),
                "asm_files": sum(1 for f in functions_meta if f.get("asm_file")),
                "pseudocode_files": sum(1 for f in functions_meta if f.get("pseudocode_file")),
            },
            "functions": functions_meta,
            "disassembled_at": datetime.now(timezone.utc).isoformat(),
            "notes": "Metadata produced by radare2 disassembly."
        }

        # Write JSON and return path
        json_result_path = write_json(json_path, result)
        logging.info("Metadata JSON written: %s", json_result_path)

    finally:
        try:
            r2.quit()
        except Exception:
            pass
        logging.info("radare2 session closed.")

###################################################################################################

def _cli() -> None:
    parser = argparse.ArgumentParser(description="Extract metadata from disassembly (radare2).")
    parser.add_argument("file", help="Target binary path to analyze.")
    parser.add_argument("--output", default="disassembled", help="Results output directory.")
    args = parser.parse_args()

    setup_logging()

    logging.info(f"radare2 disassembly file: {args.file}.")

    disassemble_radare2(args.file, output_root=args.output_root)

    logging.info(f"radare2 disassembly complete, results in: {args.output_root}.")

if __name__ == "__main__":
    _cli()

###################################################################################################
