````markdown
# APK Analyzer

A Python-based Android APK analysis tool that extracts APK metadata, resources, and generates a structured JSON report.

The analyzer can inspect APK files and collect information such as:

- Application name
- Package name
- Version information
- APK size
- Permissions
- CPU architectures
- Android SDK versions
- Signing certificate SHA256 fingerprint
- Launcher activity
- Framework detection
- Complete APK resource extraction

---

## Features

### APK Metadata Extraction

Extracts:

```json
{
    "name": "Application Name",
    "package": "com.example.app",
    "version": "1.0",
    "version_code": "1",
    "size": "50MB"
}
````

---

### Permission Analysis

Detects Android permissions:

Example:

```json
"permissions": [
    "INTERNET",
    "CAMERA",
    "RECORD_AUDIO"
]
```

---

### Architecture Detection

Supports:

* arm64-v8a
* armeabi-v7a
* x86
* x86_64

Example:

```json
"architecture": [
    "arm64-v8a"
]
```

---

### Framework Detection

Attempts to identify application frameworks:

Supported detection:

* Native Android
* Flutter
* Unity
* Xamarin

Example:

```json
"framework": "Native Android"
```

---

### Certificate Analysis

Extracts APK signing certificate fingerprint:

```json
"certificate_sha256": "xxxxxxxxxxxxxxxx"
```

Useful for:

* App verification
* Malware analysis
* APK comparison

---

### Resource Extraction

Extracts the complete APK contents:

```
Application_analysis/
│
├── metadata.json
│
└── resources/
    │
    ├── AndroidManifest.xml
    ├── classes.dex
    ├── resources.arsc
    │
    ├── lib/
    │   └── arm64-v8a/
    │       └── *.so
    │
    ├── res/
    │
    └── assets/
```

---

# Installation

## Requirements

* Python 3.12+
* pip
* Virtual environment recommended

---

## Clone Repository

```bash
git clone https://github.com/username/apk-analyzer.git

cd apk-analyzer
```

---

## Create Virtual Environment

Windows:

```bat
python -m venv .venv

.venv\Scripts\activate
```

Linux:

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

or:

```bash
pip install androguard
```

---

# Usage

Analyze an APK:

```bash
python apk_analyzer.py example.apk
```

Example:

```bash
python apk_analyzer.py Signal.apk
```

---

# Output

After analysis:

```
Signal_analysis/
│
├── metadata.json
│
└── resources/
```

---

## Example JSON Output

`metadata.json`

```json
{
    "name": "Signal",
    "package": "org.thoughtcrime.securesms",
    "version": "7.15",
    "version_code": "70150000",
    "size": "120MB",

    "permissions": [
        "INTERNET",
        "CAMERA",
        "RECORD_AUDIO"
    ],

    "architecture": [
        "arm64-v8a"
    ],

    "min_android": "26",
    "target_android": "35",

    "framework": "Native Android",

    "launcher_activity": "org.thoughtcrime.securesms.MainActivity",

    "certificate_sha256": "xxxxxxxx",

    "files_count": 3000
}
```

---

# Project Structure

```
apk-analyzer/
│
├── apk_analyzer.py
├── requirements.txt
├── README.md
│
└── examples/
    └── sample.apk
```

---

# Technologies

Built with:

* Python
* Androguard
* pathlib
* argparse
* hashlib
* JSON

---

# Use Cases

## Application Inventory

Create a database of installed APK information.

## Security Research

Analyze:

* Permissions
* Certificates
* Native libraries
* APK structure

## Developer Tools

Inspect:

* Build information
* Supported architectures
* Framework usage

## Malware Research

Collect APK intelligence before deeper analysis.

---

# Limitations

* Cannot determine whether an application is open source automatically.
* Framework detection is heuristic-based.
* Obfuscated applications may hide some information.
* Encrypted APK resources may require additional tools.

---

# License

MIT License

You are free to use, modify, and distribute this project.

---

# Author

Sabbir

GitHub:
[https://github.com/sabbir28](https://github.com/sabbir28)

```
```
