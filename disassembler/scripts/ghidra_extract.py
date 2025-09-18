#@category Disassembly.Export
# ghidra_extract.py
#
# Headless script for Ghidra: exports per-function ASM and C pseudocode,
# and writes metadata-only JSON at <base_dir>/static_information.json.

import json
import re
import os
from datetime import datetime

from ghidra.framework import Application
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

###################################################################################################

# ================= Helpers =================
def ensure_dir(path):
    """Ensure directory exists, create it if it does not exist."""
    if not os.path.isdir(path):
        os.makedirs(path)

def convert_hex(addr):
    """Convert integer or Ghidra Address to '0x...'."""
    try:
        if addr is None:
            return None
        if hasattr(addr, "getOffset"):
            return "0x%x" % addr.getOffset()
        return "0x%x" % int(addr)
    except Exception as e:
        printerr("[!] convert_hex error: %s" % str(e))
        return None

def slugify(name, maxlen=48):
    """Make a safe filename slug for function names."""
    if not name:
        name = "func"
    name = name.strip().replace(" ", "_")
    name = re.sub(r"[^A-Za-z0-9_\-\.]+", "", name)
    if not name:
        name = "func"
    return name[:maxlen]

def get_sections(program):
    """Approximate sections from memory blocks (.text, .data)."""
    mem = program.getMemory()
    secs = []
    for block in mem.getBlocks():
        try:
            secs.append({
                "name": block.getName(),
                "vaddr": convert_hex(block.getStart()),
                "size": int(block.getSize()),
                "perm": ("%s%s%s" % ("r" if block.isRead() else "-", "w" if block.isWrite() else "-", "x" if block.isExecute() else "-")),
                "type": "CODE" if block.isExecute() else ("DATA" if block.isWrite() else "OTHER"),
            })
        except Exception as e:
            printerr("[!] Skipping memory block due to error: %s" % str(e))
    return secs

def sections_focus(sections):
    """Pick concise info about .text and .data if present."""
    focus = {}
    for target in (".text", ".data"):
        match = None
        for s in sections:
            if s.get("name") == target:
                match = s
                break
        if not match:
            for s in sections:
                n = s.get("name") or ""
                if target.strip(".") in n:
                    match = s
                    break
        if match:
            focus[target] = {
                "name": match.get("name"),
                "vaddr": match.get("vaddr"),
                "size": match.get("size"),
                "perm": match.get("perm"),
                "type": match.get("type"),
            }
    return focus

def collect_basic_info(program):
    """Collect basic binary/environment information."""
    lang = program.getLanguage()
    try:
        ghidra_version = Application.getApplicationVersion()
    except Exception:
        ghidra_version = ""
    return {
        "arch": str(lang.getProcessor()),
        "bits": int(lang.getDefaultSpace().getPointerSize()) * 8,
        "endian": "little" if lang.isLittleEndian() else "big",
        "format": program.getExecutableFormat() or "",
        "machine": str(lang.getLanguageDescription().getLanguageID()),
        "entrypoint": convert_hex(program.getImageBase()),
        "asm_syntax": "ghidra",
        "ghidra_version": str(ghidra_version),
    }

def disasm_function_text(program, func):
    """Produce a simple textual disassembly by iterating instructions."""
    listing = program.getListing()
    lines = []
    try:
        it = listing.getInstructions(func.getBody(), True)
        while it.hasNext():
            insn = it.next()
            lines.append("%s: %s" % (convert_hex(insn.getAddress()), insn.toString()))
    except Exception as e:
        printerr("[!] Disassembly iteration failed for %s: %s" % (func.getName(), str(e)))
    return "\n".join(lines)

def decompile_function_text(decomp, func):
    """Return C-like pseudocode if decompiler is available, else None."""
    try:
        res = decomp.decompileFunction(func, 60, ConsoleTaskMonitor())
        if not res or not res.getDecompiledFunction():
            return None
        return res.getDecompiledFunction().getC()
    except Exception as e:
        printerr("[!] Decompile failed for %s: %s" % (func.getName(), str(e)))
        return None

###################################################################################################

# ================= Main =================
def run():
    """Ghidra main run script."""
    args = getScriptArgs()
    if not args:
        printerr("Usage: ghidra_extract.py <base_dir>")
        return

    base_dir = args[0]
    asm_dir = os.path.join(base_dir, "asm")
    c_dir = os.path.join(base_dir, "c")
    ensure_dir(asm_dir)
    ensure_dir(c_dir)

    program = currentProgram
    fm = program.getFunctionManager()

    print("[*] Ghidra extract started for: %s" % str(program.getExecutablePath()))

    info = collect_basic_info(program)
    sections = get_sections(program)
    focus = sections_focus(sections)

    # Initialize decompiler interface
    decomp = DecompInterface()
    decomp.openProgram(program)

    functions_meta = []
    asm_count = 0
    c_count = 0

    funs = list(fm.getFunctions(True))
    try:
        funs.sort(key=lambda f: f.getEntryPoint().getOffset())
    except Exception as e:
        printerr("[!] Function list sort failed: %s" % str(e))

    print("[*] Functions detected: %d" % len(funs))

    for idx, f in enumerate(funs, start=1):
        try:
            addr = f.getEntryPoint()
            name = f.getName() or "func"
            off_hex = convert_hex(addr)

            slug = slugify(name)
            idx_str = str(idx).zfill(5)
            off_tag = (off_hex or "0x0").replace("0x", "")

            # Dump assembly to file (if available)
            asm_file = os.path.join(asm_dir, "%s_%s_%s.asm" % (idx_str, off_tag, slug))
            asm_text = disasm_function_text(program, f)
            try:
                with open(asm_file, "w") as wf:
                    wf.write(asm_text or "")
                asm_rel = os.path.relpath(asm_file, base_dir)
                asm_count += 1
            except Exception as e:
                asm_rel = None
                printerr("[!] Failed to write ASM for %s: %s" % (name, str(e)))

            # Dump pseudocode (if available)
            c_rel = None
            c_text = decompile_function_text(decomp, f)
            if c_text:
                c_file = os.path.join(c_dir, "%s_%s_%s.c" % (idx_str, off_tag, slug))
                try:
                    with open(c_file, "w") as wf:
                        wf.write(c_text)
                    c_rel = os.path.relpath(c_file, base_dir)
                    c_count += 1
                except Exception as e:
                    c_rel = None
                    printerr("[!] Failed to write C pseudocode for %s: %s" % (name, str(e)))
            else:
                print("[i] No pseudocode for function: %s" % name)

            # Build the metadata struct
            functions_meta.append({
                "index": idx,
                "name": name,
                "offset": off_hex,
                "size": int(f.getBody().getNumAddresses()),
                "asm_file": asm_rel,
                "pseudocode_file": c_rel,
            })
        except Exception as e:
            try:
                fname = f.getName()
            except Exception:
                fname = "<unknown>"
            printerr("[!] Error exporting function %s: %s" % (fname, str(e)))

    result = {
        "input_file": str(program.getExecutablePath()),
        "output_base_dir": str(base_dir),
        "analysis_tool": "ghidra",
        "basic_info": info,
        "sections": sections,
        "sections_focus": focus,
        "counts": {
            "functions": len(functions_meta),
            "asm_files": asm_count,
            "pseudocode_files": c_count,
        },
        "functions": functions_meta,
        "notes": "Metadata produced by Ghidra headless disassembly.",
        "disassembled_at": datetime.utcnow().isoformat() + "Z",
    }

    out_json = os.path.join(base_dir, "static_information.json")
    try:
        with open(out_json, "w") as jf:
            json.dump(result, jf, indent=2)
        print("[*] JSON written at: %s" % out_json)
    except Exception as e:
        printerr("[!] Failed to write JSON: %s" % str(e))

    print("[*] Ghidra extract completed.")

# Execute
run()
