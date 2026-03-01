"""
Driver Manager — Appium WebDriver initialization.
All capabilities are pulled from config.config.
"""
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config import config


def get_driver():
    """Create and return a configured Appium WebDriver instance."""
    options = UiAutomator2Options()
    options.platform_name = config.PLATFORM_NAME
    options.device_name = config.DEVICE_NAME
    options.automation_name = config.AUTOMATION_NAME
    options.app = config.APK_PATH
    # Package and activity can be set if needed, e.g.:
    # options.app_package = "com.quick_alert"
    # options.app_activity = "com.quick_alert.MainActivity"
    options.uiautomator2_server_install_timeout = config.UIAUTOMATOR2_INSTALL_TIMEOUT
    options.auto_grant_permissions = True
# No reset
    # options.no_reset = True

    driver = webdriver.Remote(config.APPIUM_URL, options=options)
    driver.implicitly_wait(config.IMPLICIT_WAIT)
    return driver
