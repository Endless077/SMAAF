#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#      ______    ______    ________          _                         _                   
#    .' ____ \ .' ____ \  |_   __  |        / |_                      / |_                 
#    | (___ \_|| (___ \_|   | |_ \_| _   __`| |-'_ .--.  ,--.   .---.`| |-' .--.   _ .--.  
#     _.____`.  _.____`.    |  _| _ [ \ [  ]| | [ `/'`\]`'_\ : / /'`\]| | / .'`\ \[ `/'`\] 
#    | \____) || \____) |  _| |__/ | > '  < | |, | |    // | |,| \__. | |,| \__. | | |     
#     \______.' \______.' |________|[__]`\_]\__/[___]   \'-;__/'.___.'\__/ '.__.' [___]    
#                                                                                          


import logging
import argparse
from pathlib import Path
from typing import Any, Dict, List, Optional

from utilities.io import *
from utilities.yara_engine import *
from utilities.ioc_extractor import *
from utilities.string_extractor import *

from utilities.scoring_system import *

from utils.logger import setup_logging

###################################################################################################

def process_sample(
    sample_path: Path,
    metadata_dir: Path,
    min_length: int = 3,
    yara_dir: Optional[Path] = "/usr/yara/rules",
) -> Dict[str, Any]:
    """Process a malware sample: extract static info, strings, IOCs, YARA hits, and compute score."""
    logging.info("Processing sample: %s (extracted_dir=%s, yara_dir=%s).",
                 sample_path, metadata_dir, yara_dir)

    # 1) Load static analysis info and disassembly texts
    logging.info("Loading static info and disassembled texts.")
    static_info = load_static_info(metadata_dir)
    texts = read_text_files(metadata_dir, (".asm", ".c", ".txt", ".h"))

    # 2) Extract strings via native 'strings', Python and FLOSS
    logging.info("Extracting strings from binary.")
    s_strings = strings_native(sample_path, min_length)
    if not s_strings:
        logging.warning("Native 'strings' returned nothing, falling back to Python extractor.")
        s_strings = strings_python(sample_path, min_length)

    logging.info("Running FLOSS for string deobfuscation.")
    s_floss = floss(sample_path, min_length)

    # Include extra strings coming from static_info metadata
    logging.debug("Collecting strings from metadata.")
    json_strings: List[Dict[str, Any]] = []
    if isinstance(static_info, dict):
        for v in static_info.values():
            if isinstance(v, str):
                json_strings.append({"string": v, "source": "static_information", "offset": None})
            elif isinstance(v, list):
                for it in v:
                    json_strings.append({"string": str(it), "source": "static_information", "offset": None})

    # Deduplicate all strings
    combined_records = dedupe((s_floss or []) + (s_strings or []) + json_strings)
    plain_strings = [r["string"] for r in combined_records]
    logging.info("Collected %d unique strings", len(combined_records))

    # 3) Build text corpus for IOC extraction (strings + disassembled sources)
    all_lines: List[str] = []
    all_lines.extend(plain_strings)
    for content in (texts or {}).values():
        all_lines.extend(content.splitlines())
    logging.debug("Built corpus with %d lines for IOC extraction.", len(all_lines))

    # min_string_length) Extract IOCs
    logging.info("Extracting IOCs from strings and source texts.")
    iocs_sets = extract_iocs(all_lines)
    iocs_lists = to_sorted_lists(iocs_sets)

    # 5) Map IOC context inside disassembled files
    logging.info("Mapping IOC contexts into source files.")
    iocs_context = map_iocs_context(texts, iocs_lists, 2)

    # 6) YARA analysis: binary + text corpus
    logging.info("Compiling YARA rules (if provided).")
    rules = compile_path(yara_dir)
    yara_bin_matches: List[Dict[str, Any]] = scan_file(rules, sample_path) if rules else []
    combined_text = "\n".join(all_lines)
    yara_text_matches: List[Dict[str, Any]] = scan_text(rules, combined_text) if rules else []
    logging.info("YARA matches: %d on binary, %d on text corpus.",
                 len(yara_bin_matches), len(yara_text_matches))

    # 7) Compute advanced scoring
    logging.info("Starting final score computing.")
    score_detail = compute_score(
        iocs=iocs_lists,
        texts=texts,
        yara_bin=yara_bin_matches,
        yara_text=yara_text_matches,
        strings_records=combined_records,
        static_info=static_info
    )

    # 8) Build output dictionary
    logging.info("Processing complete for %s", sample_path)
    return {
        "file": str(sample_path),
        "static_info": static_info,
        "strings": combined_records,
        "iocs": iocs_lists,
        "iocs_context": iocs_context,
        "yara_matches_bin": yara_bin_matches,
        "yara_matches_text": yara_text_matches,
        "score": score_detail.get("score"),
        "score_detail": score_detail
    }

###################################################################################################

def _cli() -> None:
    parser = argparse.ArgumentParser(description="String & Signature Extractor (SS Extractor).")
    parser.add_argument("sample", help="Malware sample path.")
    parser.add_argument("metadata_dir", help="Metadata disassembler path.")
    parser.add_argument("out_json_dir", help="Path to output JSON file report.")
    parser.add_argument("min_length", default="/yara/rules", help="Minimum string length for retrieval.")
    parser.add_argument("yara_rules", nargs="?", default=None, help="Directory with .yar rules (optional).")
    args = parser.parse_args()

    setup_logging()
    
    logging.info("Starting SS Extractor pipeline...")

    result = process_sample(
        sample_path=Path(args.sample),
        metadata_dir=Path(args.metadata_dir),
        min_length=int(args.min_length),
        yara_dir=Path(args.yara_rules) if args.yara_rules else None,
    )

    logging.info("Writing results to %s", args.out_json_dir)

    write_json(Path(args.out_json_dir), result)

    logging.info("SS Extractor finished successfully.")

if __name__ == "__main__":
    _cli()

###################################################################################################
