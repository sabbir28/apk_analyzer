
# APK Analyzer

A lightweight Python-based Android APK analysis tool that extracts application metadata, resources, certificates, architecture information, framework detection, and generates detailed reports.

Built with **Python** and **Androguard**.

---

## Features

### 📱 Application Information

Extracts:

- Application name
- Package name
- Version name
- Version code
- APK file size
- Launcher activity
- Minimum Android SDK
- Target Android SDK

---

### 🔐 Certificate Analysis

Generates:

- APK signing certificate SHA-256 fingerprint
- Certificate hash report

Useful for:

- APK verification
- App identity checking
- Security analysis

---

### 🖼️ Icon Extraction

Automatically extracts the application launcher icon.

Output:

```

icon.png

```

---

### 📂 APK Resource Extraction

Temporarily extracts APK contents:

```

resources/
├── AndroidManifest.xml
├── classes.dex
├── res/
├── assets/
└── lib/

````

After analysis, temporary files are removed automatically.

---

### 🏗️ Architecture Detection

Detects supported CPU architectures:

Supported:

- arm64-v8a
- armeabi-v7a
- x86
- x86_64

Example:

```json
"architecture": [
    "arm64-v8a",
    "armeabi-v7a"
]
````

---

### 🚀 Framework Detection

Automatically detects common Android frameworks:

Supported:

* Native Android
* Flutter
* Unity
* Xamarin
* React Native

Example:

```json
"framework": "Flutter"
```

---

### 🔑 Permission Analysis

Extracts requested Android permissions.

Example:

```json
[
    "INTERNET",
    "CAMERA",
    "ACCESS_FINE_LOCATION"
]
```

---

### 📊 Generated Reports

The analyzer creates an output directory:

Example:

```
app-debug_analysis/
│
├── metadata.json
├── info.txt
├── certificate.sha256
└── icon.png
```

---

## Installation

### Requirements

* Python 3.10+
* pip

Install dependencies:

```bash
pip install androguard
```

---

## Usage

Run:

```bash
python analyzer.py your_app.apk
```

Example:

```bash
python analyzer.py app-debug.apk
```

---

## Example Output

Terminal:

```
[+] Extracting resources...
[+] Analyzing APK...
[+] Cleaning temporary files...

[+] Completed

{
    "name": "Example App",
    "package": "com.example.app",
    "version": "1.0",
    "version_code": 1,
    "size": "25.34 MB",
    "framework": "Native Android",
    "architecture": [
        "arm64-v8a"
    ]
}

[+] Output: app-debug_analysis
```

---

## JSON Report Example

`metadata.json`

```json
{
    "name": "Example App",
    "package": "com.example.app",
    "version": "1.0",
    "version_code": 10,
    "size": "18.20 MB",
    "permissions": [
        "INTERNET",
        "CAMERA"
    ],
    "architecture": [
        "arm64-v8a"
    ],
    "min_android": "23",
    "target_android": "35",
    "framework": "Flutter",
    "launcher_activity": "com.example.MainActivity",
    "certificate_sha256": "xxxxxxxx",
    "files_count": 245
}
```

---

## Project Structure

```
apk_analyzer/
│
├── analyzer.py
├── README.md
└── sample.apk
```

---

## Use Cases

* Android application inspection
* APK metadata extraction
* Security research
* Malware analysis preparation
* App store automation
* APK catalog generation

---

## Limitations

* Does not perform full malware scanning
* Does not decompile DEX bytecode
* Framework detection is based on file signatures
* Some protected/obfuscated APKs may hide information

---

## Future Improvements

Possible upgrades:

* [ ] AndroidManifest XML parsing
* [ ] DEX class analysis
* [ ] API usage detection
* [ ] Malware behavior scoring
* [ ] VirusTotal API integration
* [ ] Web dashboard interface
* [ ] APK comparison system
* [ ] Automatic screenshot generation

---
