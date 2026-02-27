# 📱 Appium Testing Project

Automated mobile application testing using **Appium**, **Python**, and **PyTest**.

---

## 📑 Table of Contents

- [👥 Contributors](#-contributors)
- [📌 Project Overview](#-project-overview)
- [⚙️ Requirements](#️-requirements)
- [🚀 Setup Guide](#-setup-guide)
- [▶️ Running Tests](#️-running-tests)
- [📂 Project Structure](#-project-structure)
- [📦 APK Details](#-apk-details)
- [🧪 Writing Tests](#-writing-tests)
- [🛠️ Troubleshooting](#️-troubleshooting)
- [📝 Notes](#-notes)

---

## 👥 Contributors

- **Anas Altaf** (22F-3639)
- **Shaheera Malik** (22F-3699)

---

## 📌 Project Overview

This project demonstrates **mobile app automation testing** using:

- **Appium** for mobile automation
- **Python** as the programming language
- **PyTest** as the testing framework

The application under test is an Android APK built using **React Native**.

---

## ⚙️ Requirements

Make sure the following tools are installed:

- Python (>= 3.8)
- Node.js (>= 16)
- Java JDK (>= 8)
- Android Studio (SDK + Emulator)
- Appium Server
- Appium Inspector (Optional but recommended)

---

## 🚀 Setup Guide

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

---

### 3. Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

---

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Install Appium

```bash
npm install -g appium
```

Verify installation:

```bash
appium -v
```

---

### 6. Install Appium Drivers

```bash
appium driver install uiautomator2
```

List installed drivers:

```bash
appium driver list --installed
```

---

### 7. Start Appium Server

```bash
appium
```

By default, Appium runs on:

```
http://127.0.0.1:4723
```

---

### 8. Setup Android Device / Emulator

- Open **Android Studio**
- Start an emulator OR connect a physical device

Verify device:

```bash
adb devices
```

---

### 9. (Optional) Install Appium Inspector

Download and use Appium Inspector to locate UI elements easily.

---

## ▶️ Running Tests

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest .\tests\test_click.py
```

Run with verbose output:

```bash
pytest -v
```

Run with logs:

```bash
pytest -s
```

---

## 📂 Project Structure

```
.
├── apk.apk
├── requirements.txt
├── tests/
│   ├── test_click.py
│   └── ...
├── utils/
├── pages/
└── README.md
```

---

## 📦 APK Details

- File: `apk.apk`
- App Name: **Quick Alert**
- Framework: **React Native**

---

## 🧪 Writing Tests

Example test:

```python
def test_example(driver):
    element = driver.find_element("id", "example_id")
    element.click()
```

Use **Appium Inspector** to find:

- Element IDs
- XPath
- Accessibility IDs

---

## 🛠️ Troubleshooting

### Appium not recognized

```bash
npm install -g appium
```

---

### No device detected

```bash
adb devices
```

---

### Driver not installed

```bash
appium driver install uiautomator2
```

---

### Permission issues (Linux/macOS)

```bash
sudo npm install -g appium
```

---

### Port already in use

```bash
appium --port 4725
```

---

## 📝 Notes

- Ensure Appium server is running before executing tests
- Make sure emulator/device is connected
- Use Appium Inspector for better element selection
- Update desired capabilities according to your device
