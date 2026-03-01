"""
test_login.py — Login screen test cases.

Tests:
  1. test_app_launches_to_login_screen
  2. test_login_screen_ui_elements
  3. test_login_with_valid_credentials
  4. test_login_with_invalid_credentials
  5. test_login_empty_fields_stays_on_screen
"""
from pages.login_page import LoginPage
from pages.home_page import HomePage


# ── Valid credentials (update to match your app) ─────────────
VALID_EMAIL = "anasaltafprojects@gmail.com"
VALID_PASSWORD = "Password@123"
INVALID_PASSWORD = "WrongPassword"


class TestLogin:
    """Test suite for the Login screen."""

    def test_app_launches_to_login_screen(self, driver):
        """TC-01: Verify the app launches and displays the login screen."""
        login_page = LoginPage(driver)

        assert login_page.is_login_screen_displayed(), \
            "App should launch and display the login screen with 'Log In' button"

    def test_login_screen_ui_elements(self, driver):
        """TC-02: Verify all UI elements are present on the login screen."""
        login_page = LoginPage(driver)

        assert login_page.is_email_label_displayed(), \
            "Email label should be visible"
        assert login_page.is_password_label_displayed(), \
            "Password label should be visible"
        assert login_page.is_login_screen_displayed(), \
            "Log In button should be visible"
        assert login_page.is_forgot_password_displayed(), \
            "Forgot Password link should be visible"
        assert login_page.is_terms_text_displayed(), \
            "Terms of Service text should be visible"

    def test_login_with_valid_credentials(self, driver):
        """TC-03: Verify that a user can log in with valid email and password."""
        login_page = LoginPage(driver)
        home_page = HomePage(driver)

        login_page.login(VALID_EMAIL, VALID_PASSWORD)

        assert home_page.is_home_screen_displayed(), \
            "Home screen should be displayed after successful login"

    def test_login_with_invalid_credentials(self, driver):
        """TC-04: Verify that login with wrong password keeps user on login screen."""
        login_page = LoginPage(driver)

        login_page.login(VALID_EMAIL, INVALID_PASSWORD)

        # After invalid login, user should remain on the login screen
        assert login_page.is_login_screen_displayed(), \
            "User should remain on login screen after invalid credentials"

    def test_login_empty_fields_stays_on_screen(self, driver):
        """TC-05: Verify that submitting empty fields keeps user on login screen."""
        login_page = LoginPage(driver)

        # Tap login without entering anything
        login_page.tap_login()

        assert login_page.is_login_screen_displayed(), \
            "User should stay on login screen when submitting empty fields"
