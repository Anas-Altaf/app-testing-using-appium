from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import get_driver
import time

def test_sign_in_success():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)

    # Locate fields
    email_field = wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.EditText[@hint='Username']"))
    )
    password_field = driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@hint='Password']")

    # Enter credentials
    email_field.send_keys("test@example.com")
    password_field.send_keys("123456")

    # Click Sign In
    sign_in_button = wait.until(
    EC.element_to_be_clickable(
        (AppiumBy.XPATH, "//*[contains(@text,'Login')]")
    )
    )

    # # Wait 2–3 seconds for the next screen
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Welcome to BikeX"))
    # )


    time.sleep(10)

    driver.quit()