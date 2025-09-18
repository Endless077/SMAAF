#      ______                           _                     ______                   _                       
#    .' ____ \                         (_)                  .' ____ \                 / |_                     
#    | (___ \_| .---.   .--.   _ .--.  __   _ .--.   .--./) | (___ \_|  _   __  .--. `| |-'.---.  _ .--..--.   
#     _.____`. / /'`\]/ .'`\ \[ `/'`\][  | [ `.-. | / /'`\;  _.____`.  [ \ [  ]( (`\] | | / /__\\[ `.-. .-. |  
#    | \____) || \__. | \__. | | |     | |  | | | | \ \._// | \____) |  \ '/ /  `'.'. | |,| \__., | | | | | |  
#     \______.''.___.' '.__.' [___]   [___][___||__].',__`   \______.'[\_:  /  [\__) )\__/ '.__.'[___||__||__] 
#                                                  ( ( __))            \__.'                                   

from __future__ import annotations
import re
import math
import logging

from dataclasses import dataclass

from typing import List, Dict, Tuple, Set, Any

###################################################################################################

@dataclass(frozen=True)
class Config:
    WEIGHTS: Dict[str, int] = None
    CAPS: Dict[str, int] = None
    floss_min_count: int = 30
    floss_min_ratio: float = 0.30
    
    # For exponential normalization: lower => steeper curve
    norm_scale: float = 85.0  # ~raw score where you reach ~63% of 100

    def __post_init__(self):
        # Default weights and caps if not provided
        object.__setattr__(self, "WEIGHTS", self.WEIGHTS or {
            "yara_bin_base": 60,
            "yara_text_base": 15,
            "yara_family_bonus": 10,
            "yara_multi_bonus": 10,
            "url_per_item": 4,
            "ip_per_item": 3,
            "domain_per_item": 2,
            "registry_per_item": 5,
            "proc_inject": 12,
            "networking": 8,
            "persistence": 10,
            "cred_steal": 8,
            "evasion": 6,
            "obfuscation": 10,
        })
        object.__setattr__(self, "CAPS", self.CAPS or {
            "yara_bin_rules": 2,
            "yara_text_rules": 3,
            "urls": 10, "ips": 9, "domains": 10, "registry": 8,
        })

CFG = Config()

###################################################################################################

# Persistence-related registry keys
PERSISTENCE_KEYS = [
    r"\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
    r"\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce",
    r"\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\Run",
    r"\\Services\\",
    r"\\System\\CurrentControlSet\\Services\\",
    r"\\Software\\Microsoft\\Windows\\CurrentVersion\\Shell Folders",
    r"\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
]

PERSISTENCE_RE = re.compile("|".join(PERSISTENCE_KEYS), re.IGNORECASE)

# API keyword classes
API_CLASSES: Dict[str, List[str]] = {
    "proc_inject": [
        "VirtualAlloc", "VirtualAllocEx", "VirtualProtect", "WriteProcessMemory",
        "CreateRemoteThread", "QueueUserAPC", "NtWriteVirtualMemory", "SetThreadContext",
        "MapViewOfFile", "RtlCreateUserThread", "ZwMapViewOfSection"
    ],
    "networking": [
        "InternetOpen", "InternetConnect", "HttpOpenRequest", "WinHttpOpen",
        "WinHttpConnect", "WSAStartup", "connect", "send", "recv", "URLDownloadToFile"
    ],
    "persistence": [
        "RegSetValue", "RegSetValueEx", "CreateService", "ChangeServiceConfig",
        "StartService", "CoCreateInstance", "IScheduleService", "TaskScheduler",
        "schtasks.exe", "SetWindowsHookEx"
    ],
    "cred_steal": [
        "CredEnumerate", "CredRead", "CryptUnprotectData", "LogonUser",
        "LsaEnumerateLogonSessions", "Mimikatz"
    ],
    "evasion": [
        "IsDebuggerPresent", "CheckRemoteDebuggerPresent", "NtQueryInformationProcess",
        "OutputDebugString", "GetTickCount", "RDTSCP", "ZwSetInformationThread"
    ],
}

API_PATTERNS: Dict[str, List[re.Pattern]] = {
    cls: [re.compile(rf"\b{re.escape(k)}\b", re.IGNORECASE) for k in kws]
    for cls, kws in API_CLASSES.items()
}

def _any_regex_hit(text: str, patterns: List[re.Pattern]) -> bool:
    """Return True if any regex matches the given text."""
    return any(p.search(text) for p in patterns)

###################################################################################################

# ================= Validators/Normalizers =================
IP_RE = re.compile(r"^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$")
URL_RE = re.compile(r"^(?:https?://)[^\s/$.?#].[^\s]*$", re.IGNORECASE)
DOMAIN_RE = re.compile(r"^(?=.{1,253}$)(?!-)[A-Za-z0-9-]{1,63}(?<!-)(?:\.[A-Za-z]{2,63})+$")

def _dedup_and_filter(items: List[str] | None, pattern: re.Pattern) -> List[str]:
    """Deduplicate, strip, and filter items against a regex pattern."""
    if not items:
        return []
    uniq: Set[str] = set()
    for x in items:
        if not isinstance(x, str):
            logging.debug("Skipping non-string IOC: %r", x)
            continue
        s = x.strip()
        if pattern.match(s):
            uniq.add(s)
    return list(uniq)

###################################################################################################

# ================= Scoring subroutines =================
def _score_iocs(iocs: Dict[str, List[str]]) -> Tuple[int, List[str]]:
    """Score based on IOCs: URLs, IPs, domains, registry keys."""
    W, C = CFG.WEIGHTS, CFG.CAPS
    score = 0
    reasons = []

    logging.info("Scoring IOCs...")
    urls = _dedup_and_filter(iocs.get("urls"), URL_RE)
    ips = _dedup_and_filter(iocs.get("ips"), IP_RE)
    domains = _dedup_and_filter(iocs.get("domains"), DOMAIN_RE)
    registry = list({x for x in (iocs.get("registry") or []) if isinstance(x, str) and x.strip()})

    u = min(len(urls), C["urls"])
    if u:
        inc = u * W["url_per_item"]
        score += inc
        reasons.append(f"Extracted URLs: {u} (+{inc}).")

    ip = min(len(ips), C["ips"])
    if ip:
        inc = ip * W["ip_per_item"]
        score += inc
        reasons.append(f"Extracted IPs: {ip} (+{inc}).")

    d = min(len(domains), C["domains"])
    if d:
        inc = d * W["domain_per_item"]
        score += inc
        reasons.append(f"Extracted domains: {d} (+{inc}).")

    if registry:
        k = min(len(registry), C["registry"])
        base_inc = k * W["registry_per_item"]
        score += base_inc
        reasons.append(f"Registry keys: {k} (+{base_inc}).")
        if any(PERSISTENCE_RE.search(x) for x in registry):
            score += W["persistence"]
            reasons.append(f"Registry suggests persistence (+{W['persistence']}).")

    return score, reasons

def _score_api_behaviors(texts: Dict[str, str]) -> Tuple[int, List[str]]:
    """Score based on suspicious API usage."""
    if not texts:
        logging.debug("No texts provided for API behavior scoring.")
        return 0, []
    corpus = "\n".join(texts.values())
    score = 0
    reasons = []
    for cls, pats in API_PATTERNS.items():
        if _any_regex_hit(corpus, pats):
            inc = CFG.WEIGHTS[cls]
            score += inc
            reasons.append(f"Behavioral cues: {cls} (+{inc}).")
    return score, reasons

def _score_obfuscation(strings_records: List[Dict[str, Any]]) -> Tuple[int, List[str]]:
    """Score based on FLOSS string deobfuscation ratio."""
    if not strings_records:
        logging.debug("No string records provided for obfuscation scoring.")
        return 0, []
    total = len(strings_records)
    floss_cnt = sum(1 for r in strings_records if (r.get("source") or "").lower() == "floss")
    ratio = floss_cnt / max(total, 1)
    score = 0
    reasons = []
    if floss_cnt >= CFG.floss_min_count and ratio >= CFG.floss_min_ratio:
        score += CFG.WEIGHTS["obfuscation"]
        reasons.append(
            f"High ratio of FLOSS deobfuscated strings ({floss_cnt}/{total}, {ratio:.0%}) (+{CFG.WEIGHTS['obfuscation']})."
        )
    return score, reasons

def _score_yara(yara_bin: List[Dict[str, Any]], yara_text: List[Dict[str, Any]]) -> Tuple[int, List[str]]:
    """Score based on YARA matches (binary + text)."""
    W, C = CFG.WEIGHTS, CFG.CAPS
    score = 0
    reasons = []

    logging.info("Scoring YARA: %d binary matches, %d text matches", len(yara_bin or []), len(yara_text or []))
    bin_rules = list({m.get("rule") for m in (yara_bin or []) if m.get("rule")})
    txt_rules = list({m.get("rule") for m in (yara_text or []) if m.get("rule")})

    bin_count = min(len(bin_rules), C["yara_bin_rules"])
    if bin_count:
        add = bin_count * W["yara_bin_base"]
        score += add
        reasons.append(f"YARA (bin): {len(bin_rules)} rules (counted {bin_count}) (+{add}).")

    # Meta/family bonus if meta contains family/name/description
    family_hits = 0
    for m in (yara_bin or []):
        meta = m.get("meta") or {}
        if any((k in meta and str(meta.get(k) or "").strip()) for k in ("family", "name", "description")):
            family_hits += 1
    if family_hits:
        score += W["yara_family_bonus"]
        reasons.append(f"YARA meta indicates family/name (+{W['yara_family_bonus']}).")

    if len(bin_rules) >= 2:
        score += W["yara_multi_bonus"]
        reasons.append(f"Multiple YARA rules hit on binary (+{W['yara_multi_bonus']}).")

    txt_count = min(len(txt_rules), C["yara_text_rules"])
    if txt_count:
        add = txt_count * W["yara_text_base"]
        score += add
        reasons.append(f"YARA (text): {len(txt_rules)} rules (counted {txt_count}) (+{add}).")

    return score, reasons

###################################################################################################

def _confidence_from_evidence(total_norm: int, evidence_categories: int) -> str:
    """Estimate confidence based on normalized score and evidence variety."""
    if total_norm >= 80 and evidence_categories >= 3:
        return "high"
    if total_norm >= 50 and evidence_categories >= 2:
        return "medium"
    return "low"

def _normalize(total_score: float) -> int:
    """Normalize raw score into 0–100 with exponential soft cap."""
    norm = 100.0 * (1.0 - math.exp(-float(total_score) / CFG.norm_scale))
    return int(round(min(100.0, max(0.0, norm))))

###################################################################################################

# ================= Score =================
def compute_score(
    iocs: Dict[str, List[str]],
    texts: Dict[str, str],
    yara_bin: List[Dict[str, Any]],
    yara_text: List[Dict[str, Any]],
    strings_records: List[Dict[str, Any]],
    static_info: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    """Final Score Computing."""
    total_raw = 0
    reasons: List[str] = []
    categories_hit = 0

    logging.info("Computing score...")

    # YARA contributions
    s, r = _score_yara(yara_bin, yara_text)
    if s: categories_hit += 1
    total_raw += s; reasons += r

    # IOC contributions
    s, r = _score_iocs(iocs or {})
    if s: categories_hit += 1
    total_raw += s; reasons += r

    # API behavioral cues
    s, r = _score_api_behaviors(texts or {})
    if s: categories_hit += 1
    total_raw += s; reasons += r

    # Obfuscation via FLOSS
    s, r = _score_obfuscation(strings_records or [])
    if s: categories_hit += 1
    total_raw += s; reasons += r

    # Others static info (entropy/packer)
    if isinstance(static_info, dict):
        extra = 0
        ent = static_info.get("entropy")
        packer = static_info.get("packer") or static_info.get("packer_name")
        if isinstance(ent, (int, float)) and ent >= 7.0:
            extra += 5; reasons.append("High file entropy (>=7.0) (+5).")
        if packer:
            extra += 5; reasons.append(f"Packer detected: {packer} (+5).")
        if extra:
            categories_hit += 1
            total_raw += extra

    normalized = _normalize(total_raw)
    confidence = _confidence_from_evidence(normalized, categories_hit)

    logging.info("Final score=%d (raw=%d), confidence=%s, categories=%d",
             normalized, total_raw, confidence, categories_hit)

    return {
        "score": normalized,
        "confidence": confidence,
        "reasons": reasons[:25],
        "raw_score": total_raw,
        "evidence_categories": categories_hit
    }

###################################################################################################
