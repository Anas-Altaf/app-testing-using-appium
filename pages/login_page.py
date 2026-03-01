"""
LoginPage — Page Object for the Login / Sign-In screen.

Locators derived from the actual app XML hierarchy dump.
"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Encapsulates locators and actions for the Login screen."""

    # ── Locators ─────────────────────────────────────────────────
    EMAIL_LABEL = (AppiumBy.XPATH, '//android.widget.TextView[@text="Email"]')
    PASSWORD_LABEL = (AppiumBy.XPATH, '//android.widget.TextView[@text="Password"]')
    EMAIL_FIELD = (AppiumBy.CLASS_NAME, "android.widget.EditText")  # 1st EditText
    PASSWORD_FIELD = (AppiumBy.CLASS_NAME, "android.widget.EditText")  # 2nd EditText
    FORGOT_PASSWORD = (AppiumBy.ACCESSIBILITY_ID, "Forgot Password ?")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Log In")
    LOGIN_BUTTON_TEXT = (AppiumBy.XPATH, '//android.widget.TextView[@text="Log In"]')
    TERMS_TEXT = (AppiumBy.XPATH,
        '//android.widget.TextView[contains(@text, "By signing up")]')

    # ── Helpers ──────────────────────────────────────────────────

    def _get_input_fields(self):
        """Return all EditText fields on the login screen."""
        return self.find_elements(self.EMAIL_FIELD)

    # ── Actions ──────────────────────────────────────────────────

    def enter_email(self, email):
        """Type an email address into the email field (1st EditText)."""
        fields = self._get_input_fields()
        fields[0].clear()
        fields[0].send_keys(email)

    def enter_password(self, password):
        """Type a password into the password field (2nd EditText)."""
        fields = self._get_input_fields()
        fields[1].clear()
        fields[1].send_keys(password)

    def tap_login(self):
        """Tap the Log In button."""
        self.click(self.LOGIN_BUTTON)

    def tap_forgot_password(self):
        """Tap the Forgot Password link."""
        self.click(self.FORGOT_PASSWORD)

    def login(self, email, password):
        """Convenience method: fill credentials and tap Log In."""
        self.enter_email(email)
        self.enter_password(password)
        self.tap_login()

    # ── Queries ──────────────────────────────────────────────────

    def is_login_screen_displayed(self):
        """Return True if the login button is visible (indicating login screen)."""
        return self.is_element_displayed(self.LOGIN_BUTTON)

    def is_email_label_displayed(self):
        """Return True if the Email label is visible."""
        return self.is_element_displayed(self.EMAIL_LABEL)

    def is_password_label_displayed(self):
        """Return True if the Password label is visible."""
        return self.is_element_displayed(self.PASSWORD_LABEL)

    def is_forgot_password_displayed(self):
        """Return True if the Forgot Password link is visible."""
        return self.is_element_displayed(self.FORGOT_PASSWORD)

    def is_terms_text_displayed(self):
        """Return True if the Terms of Service text is visible."""
        return self.is_element_displayed(self.TERMS_TEXT)

    def get_email_field_text(self):
        """Return the current text of the email field."""
        fields = self._get_input_fields()
        return fields[0].text if fields else ""

    def get_password_field_text(self):
        """Return the current text of the password field."""
        fields = self._get_input_fields()
        return fields[1].text if len(fields) > 1 else ""
