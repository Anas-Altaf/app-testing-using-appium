"""
Centralized configuration for the Appium test framework.
All settings can be overridden via a .env file in the project root.
"""
import os
from dotenv import load_dotenv

# Load .env file if it exists
load_dotenv()

# Appium Server
APPIUM_HOST = os.getenv("APPIUM_HOST", "127.0.0.1")
APPIUM_PORT = os.getenv("APPIUM_PORT", "4723")
APPIUM_URL = f"http://{APPIUM_HOST}:{APPIUM_PORT}"

# Device / Emulator
PLATFORM_NAME = "Android"
PLATFORM_VERSION = os.getenv("PLATFORM_VERSION", "13.0")
DEVICE_NAME = os.getenv("DEVICE_NAME", "emulator-5554")
AUTOMATION_NAME = "UiAutomator2"

# APK Path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APK_PATH = os.path.join(BASE_DIR, "drivers", "app.apk")

# Timeouts (seconds)
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "20"))

# Appium UiAutomator2 server install timeout (ms)
UIAUTOMATOR2_INSTALL_TIMEOUT = int(os.getenv("UIAUTOMATOR2_INSTALL_TIMEOUT", "60000"))
