# 📱 Mobile Test Automation Framework

Automated mobile testing for the **Quick Alert** Android app using **Python**, **Appium**, and **pytest** with the **Page Object Model (POM)** design pattern.

---

## 👥 Contributors

- **Anas Altaf** (22F-3639)
- **Shaheera Malik** (22F-3699)

---

## 📌 Project Overview

This project implements a professional mobile test automation framework that validates the **Quick Alert** Android application (React Native). The framework follows the **Page Object Model** pattern to keep test logic clean and maintainable.

**Key highlights:**
- 10 automated functional test cases
- Page Object Model with `BasePage` inheritance
- Centralized configuration via `config/config.py` and `.env`
- GitHub Actions CI pipeline
- HTML & Allure report generation

---

## 🛠️ Tools & Technologies

| Tool                   | Purpose                              |
|------------------------|--------------------------------------|
| Python 3.9+            | Programming language                 |
| Appium 2.x             | Mobile automation server             |
| Appium Python Client   | Python bindings for Appium           |
| UiAutomator2           | Android automation engine            |
| pytest                 | Test runner & assertions             |
| pytest-html            | HTML test report generation          |
| pytest-xdist           | Parallel test execution (bonus)      |
| allure-pytest          | Allure report integration (bonus)    |
| flake8                 | Code quality / linting               |
| GitHub Actions         | Continuous Integration               |

---

## 📂 Folder Structure

```
app-testing-using-appium/
│
├── config/
│   ├── __init__.py
│   └── config.py               ← Centralized settings (device, timeouts, paths)
│
├── drivers/
│   └── app.apk                 ← Android APK under test (gitignored)
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py            ← Shared driver helper methods (BasePage)
│   ├── login_page.py           ← Login screen Page Object
│   ├── home_page.py            ← Home screen Page Object
│   └── settings_page.py        ← Settings screen Page Object
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py             ← pytest fixtures (driver setup/teardown)
│   ├── test_login.py           ← Login test cases (3 tests)
│   ├── test_home.py            ← Home & app launch tests (3 tests)
│   ├── test_navigation.py      ← Navigation test cases (2 tests)
│   └── test_settings.py        ← Settings & logout tests (2 tests)
│
├── utils/
│   ├── __init__.py
│   └── driver.py               ← Appium driver initialization
│
├── reports/                    ← Auto-generated test reports
│
├── .github/
│   └── workflows/
│       └── ci.yml              ← GitHub Actions CI pipeline
│
├── .gitignore
├── setup.cfg                   ← pytest + flake8 configuration
├── requirements.txt            ← Python dependencies
└── README.md
```

---

## ⚙️ Prerequisites

Ensure the following are installed:

- **Python** 3.9 or higher — [Download](https://www.python.org/downloads/)
- **Node.js** LTS — [Download](https://nodejs.org/)
- **Appium 2.x** — `npm install -g appium`
- **UiAutomator2 driver** — `appium driver install uiautomator2`
- **Android Studio** — SDK, Emulator, ADB — [Download](https://developer.android.com/studio)
- **ADB** — bundled with Android Studio, add to PATH

Set environment variables:
```
ANDROID_HOME = C:\Users\<you>\AppData\Local\Android\Sdk
PATH += %ANDROID_HOME%\platform-tools;%ANDROID_HOME%\emulator
```

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd app-testing-using-appium
```

### 2. Create & Activate Virtual Environment

```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Place the APK

Copy your Android APK into the `drivers/` folder and name it `app.apk`:
```
drivers/app.apk
```

### 5. (Optional) Create `.env` File

Create a `.env` file in the project root to override default settings:
```
APPIUM_HOST=127.0.0.1
APPIUM_PORT=4723
PLATFORM_VERSION=13.0
DEVICE_NAME=emulator-5554
```

### 6. Start Emulator & Appium

```bash
# Verify device
adb devices

# Start Appium server (in a separate terminal)
appium
```

---

## ▶️ How to Run Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run a specific test file
pytest tests/test_login.py

# Run a specific test function
pytest tests/test_login.py::TestLogin::test_login_with_valid_credentials

# Generate HTML report
pytest --html=reports/report.html --self-contained-html

# Run in parallel (bonus)
pytest -n auto

# Generate Allure report (bonus)
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

## 🔄 CI Workflow Explanation

The CI pipeline (`.github/workflows/ci.yml`) is triggered on:
- Every **push** to the `main` branch
- Every **Pull Request** targeting `main`

**Pipeline steps:**

| Step | Action |
|------|--------|
| 1 | Checkout source code |
| 2 | Set up Python 3.11 |
| 3 | Install dependencies from `requirements.txt` |
| 4 | Run **flake8** linting on all source folders |
| 5 | Validate project structure (check folders/files exist) |
| 6 | Collect tests with `pytest --collect-only` (validates without a device) |
| 7 | Generate and upload HTML report as a downloadable artifact |

> **Note:** Full end-to-end tests require an Android emulator. The CI pipeline validates structure and collects tests without running them on a device.

---

## 🌿 Git Workflow Used

### Branching Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Stable, production-ready code |
| `develop` | Integration branch |
| `feature/xxx` | Individual feature/test branches |

### Rules
- ❌ No direct commits to `main`
- ✅ All changes go through **Pull Requests**
- ✅ Each feature developed in a separate branch
- ✅ Use meaningful commit messages

### Commit Message Convention

| Prefix | Usage |
|--------|-------|
| `feat:` | New feature or test case |
| `fix:` | Bug fix |
| `refactor:` | Code restructure |
| `docs:` | Documentation updates |
| `ci:` | CI pipeline changes |
| `chore:` | Dependency/config updates |

### PR Workflow

1. Create a feature branch from `develop`
2. Make changes, commit with meaningful messages
3. Push and open a Pull Request
4. Request code review from partner
5. Merge after approval (Squash & Merge)
6. Delete the feature branch

---

## 📸 Screenshots

> Add screenshots here after test execution:
> - Terminal output of successful test run
> - pytest HTML report
> - GitHub Actions pipeline green status
