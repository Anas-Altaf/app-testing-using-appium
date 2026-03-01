from appium import webdriver
from appium.options.android import UiAutomator2Options
import os

def get_driver():
    # Absolute path to your APK
    apk_path = os.path.abspath("./apk.apk")

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554" # Change this to your device name or emulator ID
    options.automation_name = "UiAutomator2"
    options.app = apk_path   # Appium will auto-install this APK
    # setting timeout to 30 seconds, uiautomator2ServerInstallTimeout
    options.uiautomator2_server_install_timeout = 60000

    # Auto grant permissions
    options.auto_grant_permissions = True
    

    driver = webdriver.Remote("http://localhost:4723", options=options)
    return driver