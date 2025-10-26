#     _____   ___      ______   ________          _                         _                   
#    |_   _|.'   `.  .' ___  | |_   __  |        / |_                      / |_                 
#      | | /  .-.  \/ .'   \_|   | |_ \_| _   __`| |-'_ .--.  ,--.   .---.`| |-' .--.   _ .--.  
#      | | | |   | || |          |  _| _ [ \ [  ]| | [ `/'`\]`'_\ : / /'`\]| | / .'`\ \[ `/'`\] 
#     _| |_\  `-'  /\ `.___.'\  _| |__/ | > '  < | |, | |    // | |,| \__. | |,| \__. | | |     
#    |_____|`.___.'  `.____ .' |________|[__]`\_]\__/[___]   \'-;__/'.___.'\__/ '.__.' [___]    
#                                                                                               

# ───────────────────────────────────────────────────────────────
# Third-party libraries
import idna

# ───────────────────────────────────────────────────────────────
# Standard library
import ipaddress
import logging
import re
from typing import Any, Dict, Iterable, List
from urllib.parse import urlparse

# ───────────────────────────────────────────────────────────────
# Regular expression patterns
EMAIL_RE = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    re.IGNORECASE,
)
DOMAIN_RE = re.compile(
    r"(?:(?<![A-Za-z0-9-])(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+[A-Za-z]{2,63})(?![A-Za-z0-9-])"
)
REG_RE = re.compile(
    r"(?:HKEY_[A-Z_]+|HKLM|HKCU|HKCR|HKU|HKCC)\\[^\s'\"\\]+",
    re.IGNORECASE,
)
URL_RE = re.compile(
    r"https?://[^\s'\"\\)<>]+",
    re.IGNORECASE,
)
IP_RE = re.compile(
    r"\b\d{1,3}(?:\.\d{1,3}){3}\b"
)
TRAILING_PUNCT_RE = re.compile(r"[)\]\}\>.,;:!?]+$")

###################################################################################################

# ================= Validators/Normalizers =================
def _valid_public_ipv4(ip_str: str) -> bool:
    """
    Return True if IPv4 is syntactically valid and publicly routable.
    """
    # Exclude private, loopback, multicast, reserved, link-local
    try:
        ip = ipaddress.IPv4Address(ip_str)
        valid = not (ip.is_private or ip.is_loopback or ip.is_multicast or ip.is_reserved or ip.is_link_local)
        if not valid:
            logging.debug("Ignoring non-public IPv4: %s", ip_str)
        return valid
    except ipaddress.AddressValueError:
        logging.debug("Invalid IPv4 address format: %s", ip_str)
        return False
    
def _domain_from_url(u: str) -> str | None:
    """
    Extract and normalize the hostname from a URL.
    """
    try:
        parse = urlparse(u)
        host = parse.hostname or ""
        if not host:
            logging.debug("URL has no hostname component: %s", u)
            return None
        dom = _normalize_domain(host)
        logging.debug("Extracted domain %s from URL %s", dom, u)
        return dom
    except Exception as e:
        logging.warning("Failed to parse URL %s: %s", u, e)
        return None

def _strip_trailing_punct(s: str) -> str:
    """
    Strip common trailing punctuation from a token-like string.
    """
    return TRAILING_PUNCT_RE.sub("", s.strip())

def _normalize_domain(d: str) -> str:
    """
    Normalize a domain to ASCII/IDNA and lowercase without surrounding dots.
    """
    d = d.strip().strip(".").lower()
    d = _strip_trailing_punct(d)
    try:
        # Normalize each label with IDNA; keeps punycode where needed
        labels = [idna.encode(lbl).decode("ascii") for lbl in d.split(".")]
        norm = ".".join(labels)
        logging.debug("Normalized domain '%s' -> '%s'", d, norm)
        return norm
    except Exception as e:
        # If IDNA fails, return best-effort lowercase version
        logging.warning("IDNA normalization failed for '%s': %s", d, e)
        return d

def _normalize_registry(key: str) -> str:
    """
    Canonicalize common Windows registry hive names to short forms.
    """
    k = key.strip()
    repl = {
        r"^HKEY_LOCAL_MACHINE": "HKLM",
        r"^HKEY_CURRENT_USER": "HKCU",
        r"^HKEY_CLASSES_ROOT": "HKCR",
        r"^HKEY_USERS": "HKU",
        r"^HKEY_CURRENT_CONFIG": "HKCC",
    }
    for pat, rep in repl.items():
        k = re.sub(pat, rep, k, flags=re.IGNORECASE)
    logging.debug("Normalized registry key -> %s", k)
    return k
    
###################################################################################################

# ================= Context Manager =================
def find_context(texts: Dict[str, str], token: str, ctx_lines: int) -> List[Dict[str, Any]]:
    """
    Find occurrences of a token and return surrounding line context.
    """
    logging.info("Searching for token '%s' with ±%d lines of context.", token, ctx_lines)
    res: List[Dict[str, Any]] = []
    tkn = token.lower()
    for path, content in texts.items():
        lines = content.splitlines()
        hits_before = len(res)
        for i, line in enumerate(lines):
            if tkn in line.lower():
                start, end = max(0, i-ctx_lines), min(len(lines), i+ctx_lines+1)
                res.append({"path": path, "line": i+1, "snippet": "\n".join(lines[start:end])})
        hits_after = len(res)
        if hits_after > hits_before:
            logging.debug("Found %d matches in %s", hits_after - hits_before, path)
    logging.info("Total matches for token '%s': %d", token, len(res))
    return res

def map_iocs_context(texts: Dict[str, str], iocs_lists: Dict[str, List[str]], ctx_lines: int) -> Dict[str, List[Dict[str, Any]]]:
    """
    Map each IOC token to its occurrences and context in a corpus.
    """
    logging.info("Mapping contexts for %d IOC kinds with ±%d lines", len(iocs_lists), ctx_lines)
    contexts: Dict[str, List[Dict[str, Any]]] = {k: [] for k in iocs_lists.keys()}
    for kind, toks in iocs_lists.items():
        logging.info("Processing IOC kind '%s' with %d tokens.", kind, len(toks))
        for t in toks:
            ctx = find_context(texts, t, ctx_lines)
            if ctx:
                contexts[kind].append({"token": t, "contexts": ctx})
                logging.debug("Token '%s' (%s) matched %d contexts.", t, kind, len(ctx))
    return contexts

###################################################################################################

# ================= Extractor =================
def extract_iocs(lines: Iterable[str]) -> Dict[str, set[str]]:
    """
    Extract IOCs (IPs, URLs, registry keys, emails, domains) from text lines.
    """
    logging.info("Starting IOC extraction...")
    iocs = {"ips": set(), "urls": set(), "registry": set(), "emails": set(), "domains": set()}

    for raw in lines:
        l = raw.strip()
        if not l:
            continue

        # Emails
        for e in EMAIL_RE.findall(l):
            e = _strip_trailing_punct(e)
            iocs["emails"].add(e.lower())
            at = e.rfind("@")
            if at > 0:
                iocs["domains"].add(_normalize_domain(e[at+1:]))

        # Domains (standalone)
        for d in DOMAIN_RE.findall(l):
            if any(c.isalpha() for c in d):
                iocs["domains"].add(_normalize_domain(d))

        # URLs
        for u in URL_RE.findall(l):
            u = _strip_trailing_punct(u)
            iocs["urls"].add(u)
            dom = _domain_from_url(u)
            if dom:
                iocs["domains"].add(dom)

        # Windows Registry Keys
        for r in REG_RE.findall(l):
            iocs["registry"].add(_normalize_registry(r))

        # IPv4 candidates
        for ip in IP_RE.findall(l):
            if _valid_public_ipv4(ip):
                iocs["ips"].add(ip)

    logging.info(
        "IOC extraction completed: %d domains, %d urls, %d emails, %d ips, %d registry keys.",
        len(iocs["domains"]), len(iocs["urls"]), len(iocs["emails"]), len(iocs["ips"]), len(iocs["registry"])
    )
    return iocs

def to_sorted_lists(iocs: Dict[str, set[str]]) -> Dict[str, List[str]]:
    """
    Convert IOC sets to sorted lists for stable output.
    """
    logging.info("Converting IOC sets to sorted lists...")
    sorted_iocs = {k: sorted(v) for k, v in iocs.items()}
    logging.debug(
        "Sorted IOC sizes: domains=%d, urls=%d, emails=%d, ips=%d, registry=%d",
        len(sorted_iocs.get("emails", [])),
        len(sorted_iocs.get("domains", [])),
        len(sorted_iocs.get("registry", [])),
        len(sorted_iocs.get("urls", [])),
        len(sorted_iocs.get("ips", []))
    )
    return sorted_iocs

###################################################################################################
