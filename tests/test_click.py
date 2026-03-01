from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import get_driver
import time


def test_sign_in_success():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)


    # Wait for fields
    fields = wait.until(
        EC.presence_of_all_elements_located(
            (AppiumBy.CLASS_NAME, "android.widget.EditText")
        )
    )

    print("Fields found:", len(fields))

    email_field = fields[0]
    password_field = fields[1]

    # Enter data
    # email_field.click()
    email_field.clear()
    email_field.send_keys("anasaltafprojects@gmail.com")

    # password_field.click()
    password_field.clear()
    password_field.send_keys("Password@123")

    # Click login
    login_button = wait.until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Log In"))
    )
    login_button.click()
    time.sleep(5)  # Wait for login to process

    driver.quit()