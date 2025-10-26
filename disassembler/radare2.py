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

# ───────────────────────────────────────────────────────────────
# Third-party libraries
import r2pipe

# ───────────────────────────────────────────────────────────────
# Local application imports
from disassembler.utilities import *
from utils.logger import setup_logging

# ───────────────────────────────────────────────────────────────
# Standard library
import argparse
import json
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

###################################################################################################

# ================= Helpers =================
def _detect_basic_info(r2) -> Dict[str, Any]:
    """
    Extract and normalize basic binary information using 'ij' in radare2.
    """
    try:
        logging.info("Extracting basic binary information via 'ij'.")

        output = r2.cmd("ij")
        if not output.strip():
            logging.warning("Empty output from 'ij', could not read binary info.")
            return {}

        try:
            ij = json.loads(output)
        except json.JSONDecodeError as e:
            logging.error("Failed to parse 'ij' output as JSON: %s", e)
            logging.debug("Raw output from 'ij':\n%s", output)
            return {}

        bininfo = ij.get("bin", {}) or {}
        core = ij.get("core", {}) or {}
        asm  = ij.get("asm", {}) or {}

        # Entrypoint with robust fallbacks
        entry_val = bininfo.get("entry") or core.get("seek")

        # Image header info (radare2-like heuristic)
        if not entry_val:
            try:
                iIj = r2.cmdj("iIj") or {}
                entry_val = iIj.get("entry") or entry_val
                if entry_val:
                    logging.debug("Entrypoint resolved via 'iIj': %s", convert_hex(entry_val))
            except Exception:
                pass

        # Binary base address (Ghidra-like heuristic)
        if not entry_val:
            baddr = bininfo.get("baddr") or 0
            if baddr:
                entry_val = baddr
                logging.debug("Entrypoint inferred from binary base address: %s", convert_hex(baddr))

        # First Function Offset (UNIX-like heuristic)
        if not entry_val:
            try:
                funcs = r2.cmdj("aflj") or []
                if funcs and isinstance(funcs, list):
                    entry_val = funcs[0].get("offset")
                    logging.debug("Entrypoint inferred from first function offset: %s", convert_hex(entry_val))
            except Exception:
                pass

        entry_hex = convert_hex(entry_val) if entry_val else None

        # ── VA (virtual addressing)
        va = core.get("va")

        if va is None:
            # Query radare2 directly for the current VA mode
            try:
                eva_raw = r2.cmd("e io.va").strip().lower()
                if eva_raw in ("true", "false"):
                    va = (eva_raw == "true")
                elif eva_raw.isdigit():
                    va = (eva_raw != "0")
                elif eva_raw == "yes":
                    va = True
                elif eva_raw == "no":
                    va = False
                else:
                    # Unknown output
                    va = True  # Default to True for disassembly accuracy
                    logging.warning("Unable to parse 'e io.va' output (%s), defaulting to True.", eva_raw)
                logging.debug("VA mode resolved via 'e io.va': %s", va)
            except Exception as e:
                logging.warning("Failed to read 'e io.va': %s — defaulting to True", e)
                va = True

        # Guarantee a boolean result
        if not isinstance(va, bool):
            va = bool(va)

        basic_info = {
            "arch":         bininfo.get("arch"),
            "bits":         bininfo.get("bits"),
            "endian":       bininfo.get("endian"),
            "format":       bininfo.get("bintype") or bininfo.get("format"),
            "os":           bininfo.get("os"),
            "class":        bininfo.get("class"),
            "machine":      bininfo.get("machine"),
            "entrypoint":   entry_hex,
            "va":           va,
            "asm_syntax":   asm.get("syntax") or r2.cmd("e asm.syntax").strip() or None,
            "r2_version":   core.get("version") or r2.cmd("?V").strip(),
        }

        logging.info(
            "Binary info: arch=%s, bits=%s, format=%s, os=%s, endian=%s, entry=%s, va=%s",
            basic_info.get("arch"),
            basic_info.get("bits"),
            basic_info.get("format"),
            basic_info.get("os"),
            basic_info.get("endian"),
            basic_info.get("entrypoint"),
            basic_info.get("va"),
        )

        if not basic_info.get("entrypoint"):
            logging.warning("Entrypoint still missing - trying Ghidra-like fallbacks may help on PIE/stripped binaries.")

        return basic_info

    except Exception as e:
        logging.exception("Failed to extract basic binary info with 'ij': %s", e)
        return {}

def _list_functions(r2) -> List[Dict[str, Any]]:
    """
    Retrieve all detected functions using 'aflj' from radare2.
    """
    try:
        logging.info("Fetching function list from radare2 using 'aflj'.")

        # Run the radare2 command that lists all analyzed functions (JSON)
        output = r2.cmd("aflj")

        if not output.strip():
            logging.warning("Empty output from 'aflj', no functions detected or analysis not performed.")
            return []

        try:
            fun_list = json.loads(output)
        except json.JSONDecodeError as e:
            logging.error("Failed to parse 'aflj' output as JSON: %s", e)
            logging.debug("Raw output:\n%s", output)
            return []

        if not isinstance(fun_list, list):
            logging.error("Unexpected data format from 'aflj': expected a list, got %s", type(fun_list))
            return []

        # Sort functions by their offset (address)
        fun_list.sort(key=lambda f: f.get("offset", 0) or 0)

        logging.info("Total functions parsed: %d", len(fun_list))
        if len(fun_list) == 0:
            logging.warning("No functions found.")
        elif len(fun_list) < 5:
            logging.debug("Only a few functions detected, binary may be stripped or minimal.")

        # Optional: log first few function names for debugging
        for f in fun_list[:5]:
            name = f.get("name", "<unnamed>")
            offset = convert_hex(f.get("offset", 0))
            logging.debug("Function detected: %s at %s", name, offset)

        return fun_list

    except Exception as e:
        logging.exception("Unexpected error while listing functions with 'aflj': %s", e)
        return []

def _list_sections(r2) -> List[Dict[str, Any]]:
    """
    Retrieve binary sections using 'iSj' from radare2 (JSON output).
    """
    try:
        logging.info("Fetching sections list using 'iSj'.")

        # Execute the radare2 command
        sec_json = r2.cmd("iSj")
        if not sec_json.strip():
            logging.warning("Empty output from 'iSj', no sections were found.")
            return []

        # Parse JSON output from radare2
        try:
            sections = json.loads(sec_json)
        except json.JSONDecodeError as e:
            logging.error("Failed to parse 'iSj' output as JSON: %s", e)
            logging.debug("Raw 'iSj' output:\n%s", sec_json)
            return []

        if not isinstance(sections, list):
            logging.error("Unexpected output type from 'iSj': %s", type(sections))
            return []

        result = []
        for s in sections:
            name = s.get("name", "")
            if not name.strip():
                # Skip invalid or unnamed section entries
                logging.debug("Skipping unnamed/invalid section entry: %s", s)
                continue

            vaddr = convert_hex(s.get("vaddr"))
            paddr = convert_hex(s.get("paddr"))
            perm = s.get("perm") or "----"
            size = s.get("size", 0)

            # Infer section type based on permissions (if missing)
            if "x" in perm:
                sec_type = "CODE"
            elif "w" in perm:
                sec_type = "DATA"
            else:
                sec_type = "OTHER"

            # Add section data
            result.append({
                "name": name,
                "vaddr": vaddr,
                "paddr": paddr,
                "size": size,
                "perm": perm,
                "addralign": s.get("addralign", 0),
                "type": s.get("type") or sec_type,
            })

        logging.info("Total sections parsed: %d", len(result))
        if len(result) < 3:
            logging.warning("Few sections detected, binary might be packed or stripped.")

        return result

    except Exception as e:
        logging.exception("Unexpected error while listing sections with 'iSj': %s", e)
        return []


def _sections_focus(sections: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Summarize key information about the .text and .data sections if present.
    """
    logging.info("Extracting focused summary for .text and .data sections.")
    focus: Dict[str, Any] = {}

    for target in (".text", ".data"):
        # Try to find section by exact name or partial match
        match = next((s for s in sections if s.get("name") == target), None)
        if not match:
            match = next(
                (s for s in sections if s.get("name") and target.strip(".") in s["name"]),
                None,
            )

        if match:
            focus[target] = {
                "name": match.get("name"),
                "vaddr": match.get("vaddr"),
                "size": match.get("size"),
                "perm": match.get("perm"),
                "type": match.get("type"),
            }
            logging.debug("Section focus added: %s -> %s", target, match.get("name"))
        else:
            logging.debug("Section %s not found in list.", target)

    logging.info("Focused summary extracted: %d sections.", len(focus))
    return focus

def _get_function_disasm_text(r2, addr: int) -> str:
    """
    Get the assembly listing for a function using 'pdf' (print disassembly function).
    """
    try:
        if not isinstance(addr, int):
            logging.error("Invalid address type for disassembly: %r", addr)
            return ""

        logging.debug("Disassembling function at address 0x%x using 'pdf'.", addr)
        output = r2.cmd(f"pdf @ {addr}")

        if not output.strip():
            logging.warning("Empty disassembly output at 0x%x (possibly invalid address).", addr)
            return ""

        return output

    except Exception as e:
        logging.warning("Failed to disassemble function at 0x%x: %s", addr if isinstance(addr, int) else -1, e)
        return ""

def _decompile_text(r2, addr: int) -> Optional[str]:
    """
    Try to decompile a function to C-like pseudocode
    using r2ghidra-dec (pdc) or r2dec (pdd) as a fallback.
    """
    try:
        if not isinstance(addr, int):
            logging.error("Invalid address passed to _decompile_text: %r", addr)
            return None

        # Move seek to the function address
        r2.cmd(f"s {addr}")

        # r2ghidra-dec (pdc)
        logging.debug("Attempting decompilation with r2ghidra-dec at 0x%x.", addr)
        try:
            out = r2.cmd(f"pdc @ {addr}")
            if out and "Unknown command" not in out and "Cannot find" not in out:
                logging.info("Decompilation successful with r2ghidra-dec at: 0x%x", addr)
                return out
        except Exception as e:
            logging.debug("r2ghidra-dec failed at 0x%x: %s", addr, e)

        # r2dec (pdd)
        logging.debug("Attempting decompilation with r2dec at: 0x%x", addr)
        try:
            out = r2.cmd(f"pdd @ {addr}")
            if out and "Unknown command" not in out and "Cannot find" not in out:
                logging.info("Decompilation successful with r2dec at: 0x%x", addr)
                return out
        except Exception as e:
            logging.debug("r2dec failed at 0x%x: %s", addr, e)

        logging.debug("No decompiler output available for function at: %s", convert_hex(addr))
        return None

    except Exception as e:
        logging.exception("Unexpected error during decompilation at %s: %s", convert_hex(addr), e)
        return None


###################################################################################################

# ================= Disassemble =================
def disassemble_radare2(
    file_path: str,
    output: str = "disassembled",
    deep: bool = False,
    timeout: int = 300,
):
    """
    Perform static disassembly and metadata extraction using radare2.
    Generates assembly and pseudocode files for each function.
    """
    src = Path(file_path).expanduser().resolve()

    # Validate target file path
    if not src.exists():
        logging.error("Input file not found: %s", src)
        raise FileNotFoundError(f"File not found: {src}")
    if not src.is_file():
        logging.error("Target is not a valid file: %s", src)
        raise IsADirectoryError(f"Target is not a file: {src}")

    # Prepare output directory structure
    base_dir, json_path, asm_dir, c_dir = make_radare_dirs(output, src)
    logging.info("Output directory prepared: %s", base_dir)

    # Initialize radare2 in headless mode
    try:
        r2 = r2pipe.open(str(src), flags=["-2"])
        logging.info("radare2 session started for: %s", src.name)
    except FileNotFoundError as e:
        logging.error("radare2 binary not found in PATH.")
        raise SystemExit("Error: radare2 not found.") from e
    except Exception as e:
        logging.exception("Failed to start radare2 session: %s", e)
        raise

    try:
        # Set analysis options
        r2.cmd(f"e anal.timeout = {timeout}")
        r2.cmd("e scr.color=false")
        r2.cmd("e io.va=true")

        # Run analysis
        if deep:
            logging.info("Running full deep radare2 analysis (aaa) for: %s", src.name)
            r2.cmd("aaa")
        else:
            logging.info("Running fast radare2 analysis (aa) for: %s", src.name)
            r2.cmd("aa")

        # Extract metadata
        logging.debug("Extracting binary metadata (basic info, sections, functions).")
        info = _detect_basic_info(r2)
        sections = _list_sections(r2)
        focus = _sections_focus(sections)
        funs = _list_functions(r2)

        if not funs:
            logging.warning("No functions detected by 'aflj' — binary may be stripped or not executable.")
        else:
            logging.info("Detected %d functions in total.", len(funs))

        # Process each function
        functions_meta: List[Dict[str, Any]] = []
        for idx, f in enumerate(funs, start=1):
            addr = f.get("offset")
            name = f.get("name") or f"func_{idx}"
            size = f.get("size", 0)
            off_hex = convert_hex(addr) if addr is not None else "0x0"

            slug = slugify(name)
            idx_str = str(idx).zfill(5)
            off_tag = off_hex.replace("0x", "")

            # Assembly output
            asm_file = asm_dir / f"{idx_str}_{off_tag}_{slug}.asm"
            asm_text = _get_function_disasm_text(r2, addr) if isinstance(addr, int) else ""
            asm_written = write_text(asm_file, asm_text)
            if asm_written:
                logging.debug("ASM file written for %s: %s", name, asm_written)
            else:
                logging.warning("Failed to write ASM file for function: %s", name)

            # Pseudocode output (try both pdc/pdd)
            pseudo = _decompile_text(r2, addr) if isinstance(addr, int) else None
            c_written: Optional[str] = None
            if pseudo:
                c_file = c_dir / f"{idx_str}_{off_tag}_{slug}.c"
                c_written = write_text(c_file, pseudo)
                if c_written:
                    logging.debug("Pseudocode file written for %s: %s", name, c_written)
                else:
                    logging.warning("Failed to write pseudocode for: %s", name)
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

        # Build and save metadata JSON
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
            "notes": "Metadata produced by radare2 disassembly.",
        }

        json_result_path = write_json(json_path, result)
        logging.info("Metadata JSON successfully written: %s", json_result_path)

    except Exception as e:
        logging.exception("Error during radare2 disassembly: %s", e)
        raise
    finally:
        try:
            r2.quit()
            logging.info("radare2 session closed for: %s", src.name)
        except Exception:
            logging.debug("Failed to gracefully close radare2 session.")


###################################################################################################

def _cli() -> None:
    """
    Command-line interface for radare2 disassembly module.
    """
    parser = argparse.ArgumentParser(description="Extract metadata and disassembly from binaries using radare2.")
    parser.add_argument("file", help="Target binary path to analyze.")
    parser.add_argument("--output", default="disassembled", help="Results output directory.")
    parser.add_argument("--deep", action="store_true", help="Run full deep analysis (aaa) instead of fast (aa).")
    parser.add_argument("--timeout", type=int, default=300, help="Set timeout (in seconds) for radare2 analysis.")
    args = parser.parse_args()

    # Startup logs
    setup_logging()

    logging.info(f"Using radare2 scan mode deep: {args.deep}")
    logging.info(f"Using radare2 tiimeout: {args.timeout}")
    logging.info(f"radare2 disassembly file: {args.file}")

    # Validate input path early
    target = Path(args.file).expanduser().resolve()
    if not target.exists() or not target.is_file():
        logging.error("File not found or invalid: %s", target)
        sys.exit(1)

    # Startup disassemble with radare2
    try:
        disassemble_radare2(
            args.file,
            output=args.output,
            deep=args.deep,
            timeout=args.timeout
        )
        logging.info("radare2 disassembly complete, results saved under: %s", args.output)
    except Exception as e:
        logging.exception("radare2 disassembly process failed: %s", e)
        sys.exit(1)


if __name__ == "__main__":
    _cli()

###################################################################################################
