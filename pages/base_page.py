"""
BasePage — shared driver helper methods inherited by all Page Objects.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import EXPLICIT_WAIT


class BasePage:
    """Base class for all Page Objects. Provides common element interaction methods."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    # ── Element finders ──────────────────────────────────────────

    def find_element(self, locator):
        """Wait for a single element and return it."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Wait for multiple elements and return them."""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_element_visible(self, locator):
        """Wait until the element is visible on screen."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        """Wait until the element is clickable."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    # ── Actions ──────────────────────────────────────────────────

    def click(self, locator):
        """Wait for element to be clickable and tap it."""
        element = self.wait_for_element_clickable(locator)
        element.click()
        return element

    def type_text(self, locator, text):
        """Clear a field and type text into it."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return element

    def get_text(self, locator):
        """Return the text of the element."""
        return self.find_element(locator).text

    # ── Query helpers ────────────────────────────────────────────

    def is_element_displayed(self, locator, timeout=5):
        """Return True if the element is displayed, False otherwise."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def is_element_present(self, locator, timeout=5):
        """Return True if the element exists in the DOM."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    # ── Navigation helpers ───────────────────────────────────────

    def go_back(self):
        """Press the device back button."""
        self.driver.back()

    def hide_keyboard(self):
        """Hide the on-screen keyboard if visible."""
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass  # keyboard may not be visible

    def get_page_source(self):
        """Return the current page source (useful for debugging)."""
        return self.driver.page_source
