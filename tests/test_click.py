import time
from selenium.webdriver.common.by import By

from utils.driver import get_driver

# 1. Launch app
driver = get_driver()

# 2. Wait a few seconds for app to load
time.sleep(2)  # You can replace with explicit waits later

# 3. Find button by text
# Example: In API Demos, there is a button with text "Accessibility"
button_text = "Accessibility"
button = driver.find_element(By.XPATH, f"//*[@text='{button_text}']")

# 4. Click the button
button.click()

# 5. Print success
print(f"Clicked button with text: {button_text}")

# 6. Close app
driver.quit()