![Wallpaper](https://github.com/Endless077/SMAF/blob/main/docs/logo.png)

# 🧰 Static Malware Analysis Automation Framework (SMAF)

The system analyzes malware binaries without execution, identifies indicators of compromise (IOCs), predicts behaviors, and generates actionable reports for security teams.


## ⚠️ Disclaimer

This framework handles **real malware samples**.  
Run it **only in isolated environments** (VMs or containers).  
Do **not** use untrusted sources for obtaining samples. Prefer official / reputable repositories and services, for example:

- **VirusTotal** — https://www.virustotal.com/  
- **VirusShare** — https://virusshare.com/  
- **MalwareBazaar** — https://bazaar.abuse.ch/
  
Do **not** execute samples directly - this framework performs *static* analysis only.


## 🔑 Key Features

- **📦 Sample Collection** — Automates the retrieval and organization of malware samples (PE, ELF, APK) from local or external sources.  
- **⚙️ Disassembly Automation** — Integrates tools like **Ghidra** and **Radare2** for headless disassembly and architecture detection.  
- **🔍 String & IOC Extraction** — Extracts readable and obfuscated strings using **FLOSS**, and identifies IOCs (URLs, IPs, registry keys).  
- **🧩 Signature Matching** — Applies **YARA** rules to detect known malware patterns and families.  
- **📄 Structured Output** — Generates standardized **JSON** files for integration with external analysis or reporting tools.


## 🚦 Project Status

| Component | Status | Description |
|------------|---------|-------------|
| 🧩 Malware Sample Collector | ✅ Implemented | Collects and tags samples (EXE, APK, ELF, etc.) |
| ⚙️ Disassembler Module | ✅ Implemented | Uses Ghidra, Radare2, or IDA for headless disassembly |
| 🔍 String & Signature Extractor | ✅ Implemented | Extracts strings, IOCs, and matches YARA rules |
| 🤖 Behavioral Predictor | ⚠️ Not Implemented | Planned ML module for behavioral prediction |
| 🧾 Reporting Engine | ⚠️ Not Implemented | Planned reporting engine (HTML, PDF, STIX/TAXII) |

> **Note:** Only the collector, disassembler, and extractor are functional at this stage.  
> The behavioral predictor and reporting engine are marked as **TODO**.


## 🛠️ Local Installation

> Example setup on Linux / WSL2 with Python 3.10+.

1. **Clone the repository**
```bash
git clone https://github.com/Endless077/Static-Malware-Framework.git
cd Static-Malware-Framework
```

2. **Create and activate a virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install external tools**
- **Java (JDK 17+)** — required runtime for Ghidra.
- **Ghidra** — required for disassembly (use headless mode).
- **Radare2** — alternative disassembly backend like Ghidra.
- **FLOSS** — for extracting obfuscated strings.
- **YARA** and **yara-python** — for signature-based detection.

 ⚠️ **Note:**  
> For installation, it is recommended to follow the **official documentation** of each tool to ensure compatibility with your operating system.
> If any of the required tools or dependencies are missing, the framework will automatically report the issue during runtime with a clear error message.  

5. **Configure paths and APIs in `config.py`**
```ini
VT_API_KEY: str = os.getenv("VT_API_KEY", "")
VS_API_KEY: str = os.getenv("VS_API_KEY", "")
MB_API_KEY: str = os.getenv("MB_API_KEY", "")
...
```

## 🐳 Docker Installation (Optional)

1. **Build the Docker image**

2. **Run the container**


## ⛏️ Modules Helpers

### 1. Malware Collector
```txt
python3 -m collector.main

[LOG] INFO - 2025-07-31 00:00:00 -  ________               _        _       _______  _____
[LOG] INFO - 2025-07-31 00:00:00 - |_   __  |             / |_     / \     |_   __ \|_   _|
[LOG] INFO - 2025-07-31 00:00:00 -   | |_ \_|,--.   .--. `| |-'   / _ \      | |__) | | |
[LOG] INFO - 2025-07-31 00:00:00 -   |  _|  `'_\ : ( (`\] | |    / ___ \     |  ___/  | |
[LOG] INFO - 2025-07-31 00:00:00 -  _| |_   // | |, `'.'. | |, _/ /   \ \_  _| |_    _| |_
[LOG] INFO - 2025-07-31 00:00:00 - |_____|  \'-;__/[\__) )\__/|____| |____||_____|  |_____|
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

### 2. Disassembler (Headless)
```txt
python3 -m disassembler.ghidra --help
usage: ghidra.py [-h] --ghidra GHIDRA --scripts SCRIPTS [--output OUTPUT] [--keep-project] file

Extract metadata from disassembly (ghidra)

positional arguments:
  file               Target binary path to analyze.

options:
  -h, --help         show this help message and exit
  --ghidra GHIDRA    Path to Ghidra's home.
  --scripts SCRIPTS  Directory containing useful Ghidra scripts.
  --output OUTPUT    Results output directory.
  --keep-project     Do not delete temporary Ghidra project folder.
```
```txt
python3 -m disassembler.radare2 --help
usage: radare2.py [-h] [--output OUTPUT] [--deep] [--timeout TIMEOUT] file

Extract metadata and disassembly from binaries using radare2.

positional arguments:
  file               Target binary path to analyze.

options:
  -h, --help         show this help message and exit
  --output OUTPUT    Results output directory.
  --deep             Run full deep analysis (aaa) instead of fast (aa).
  --timeout TIMEOUT  Set timeout (in seconds) for radare2 analysis.
```

### 3. Extractor (Strings + YARA)
```txt
python3 -m extractor.main --help
usage: main.py [-h] -m METADATA [-o OUTPUT] [-l LENGTH] [-r RULES] sample

String & Signature Extractor (SS Extractor).

positional arguments:
  sample                Path to the malware sample.

options:
  -h, --help            show this help message and exit
  -m METADATA, --metadata METADATA
                        Path to disassembler metadata directory.
  -o OUTPUT, --output OUTPUT
                        Path to output JSON report.
  -l LENGTH, --length LENGTH
                        Minimum string length for extraction.
  -r RULES, --rules RULES
                        Directory containing YARA rules (optional).
```

## 📜 API Reference

You can view the API documentation using FastAPI by visiting the **/docs** endpoint of your server (i.e., [http://localhost:8000/docs](http://localhost:8000/docs)). This interactive interface provides a comprehensive list of available APIs, including details on each supported request, required parameters, allowed HTTP methods, and expected responses. It's an invaluable tool for quickly exploring and understanding the functionality offered by your APIs without the need to manually reference static documentation.

## 🙏 Acknowledgements

### FastAPI 🚀

FastAPI is a modern web framework for building APIs with Python 3.7+ based on standard Python type hints. It offers high performance with automatic interactive documentation (Swagger UI), WebSocket support, GraphQL integration, CORS middleware, OAuth2 authentication, and more.

[More information here](https://github.com/tiangolo/fastapi)

### Ghidra ⚙️

Ghidra is a free, open-source software reverse engineering (SRE) suite developed by the NSA. It provides disassembly, decompilation, program analysis, and scripting. SMAF uses **headless mode** (`analyzeHeadless`) to batch-disassemble binaries in automated pipelines.

[More information here](https://github.com/NationalSecurityAgency/ghidra)

### radare2 🛠️

radare2 (r2) is an open-source reverse engineering framework offering disassembly, debugging, binary analysis, and powerful scripting via **r2pipe**. It can be used as an alternative or complement to Ghidra for automated disassembly tasks.

[More information here](https://github.com/radareorg/radare2)

### YARA 🧩

YARA is a pattern-matching tool widely used in malware research to identify families and traits via **rules** that match byte patterns, strings, and metadata. SMAF leverages YARA (and `yara-python`) to detect known signatures and extract IOCs.

[More information here](https://github.com/VirusTotal/yara)


## 💾 License

This project is licensed under the GNU General Public License v3.0.

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)

![Static Badge](https://img.shields.io/badge/UniSA-MLTestSuite-red?style=plastic)


## 🖐 Authors

**Project Manager:**
- [Antonio Garofalo](https://github.com/Endless077)


## 🔔 Support

For support, email [antonio.garofalo125@gmail.com](mailto:antonio.garofalo125@gmail.com) or contact the project contributors.


## 📝 Documentation

See the documentation project **[here](https://github.com/Endless077/SMAF/blob/main/docs.pdf)**.
