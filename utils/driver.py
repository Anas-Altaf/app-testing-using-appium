from appium import webdriver
from appium.options.android import UiAutomator2Options
import os

def get_driver():
    # Absolute path to your APK
    apk_path = os.path.abspath("../bikex.apk")

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "RF8M50CQK5H"
    options.automation_name = "UiAutomator2"
    options.app = apk_path   # Appium will auto-install this APK

    driver = webdriver.Remote("http://localhost:4723", options=options)
    return driver