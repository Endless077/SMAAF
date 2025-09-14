#     ____  ____          __                 _        __           _                       __                    _          
#    |_   ||   _|        [  |               (_)      |  ]         / \                     [  |                  (_)         
#      | |__| |    _   __ | |.--.   _ .--.  __   .--.| | ______  / _ \     _ .--.   ,--.   | |   _   __  .--.   __   .--.   
#      |  __  |   [ \ [  ]| '/'`\ \[ `/'`\][  |/ /'`\' ||______|/ ___ \   [ `.-. | `'_\ :  | |  [ \ [  ]( (`\] [  | ( (`\]  
#     _| |  | |_   \ '/ / |  \__/ | | |     | || \__/  |      _/ /   \ \_  | | | | // | |, | |   \ '/ /  `'.'.  | |  `'.'.  
#    |____||____|[\_:  / [__;.__.' [___]   [___]'.__.;__]    |____| |____|[___||__]\'-;__/[___][\_:  /  [\__) )[___][\__) ) 
#                 \__.'                                                                         \__.'                       

"""
Hybrid Analysis API Helper Module for Static Malware Analysis Framework (SMAF)
https://hybrid-analysis.com/docs/api/v2

This module provides helper functions to interact with the Hybrid Analysis (CrowdStrike Falcon Sandbox) API:
- Submit files and URLs to sandbox environments (e.g., Windows, Linux, Android).
- Query report summaries, behavior trees, and extracted artifacts.
- Search by hashes (SHA256/MD5), verdicts, signatures, and Tags.
- Download IOC sets (domains, IPs, mutexes, registry keys, dropped files).
- Access raw JSON for downstream processing.

What is?
Cloud sandbox and threat analysis service (by CrowdStrike) that executes suspicious files/URLs in
virtual environmentsto extract dynamic behavior, IOCs, and signatures.
"""
