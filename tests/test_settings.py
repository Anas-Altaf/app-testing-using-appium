"""
test_settings.py — Profile / Settings screen test cases.

Tests:
  16. test_profile_header_displayed
  17. test_profile_user_info_displayed
  18. test_settings_menu_items_visible
  19. test_sign_out_returns_to_login
"""
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.settings_page import SettingsPage


VALID_EMAIL = "anasaltafprojects@gmail.com"
VALID_PASSWORD = "Password@123"


def _navigate_to_settings(driver):
    """Helper: log in and navigate to the Profile/Settings screen."""
    login_page = LoginPage(driver)
    login_page.login(VALID_EMAIL, VALID_PASSWORD)
    home_page = HomePage(driver)
    home_page.tap_nav_button(3)  # 5th nav button = Profile/Settings
    return SettingsPage(driver)


class TestSettings:
    """Test suite for the Profile/Settings screen."""

    def test_profile_header_displayed(self, driver):
        """TC-16: Verify the Profile header is displayed on the settings screen."""
        settings_page = _navigate_to_settings(driver)

        assert settings_page.is_settings_displayed(), \
            "'Profile' header should be visible on the settings screen"

    def test_profile_user_info_displayed(self, driver):
        """TC-17: Verify user name and email are displayed on the profile screen."""
        settings_page = _navigate_to_settings(driver)

        assert settings_page.is_user_name_displayed(), \
            "User name should be visible on the profile"
        assert settings_page.is_user_email_displayed(), \
            "User email should be visible on the profile"

    # def test_settings_menu_items_visible(self, driver):
    #     """TC-18: Verify all settings menu items are visible."""
    #     settings_page = _navigate_to_settings(driver)

    #     assert settings_page.is_general_setting_displayed(), \
    #         "'General Setting' section header should be visible"
    #     assert settings_page.is_update_password_displayed(), \
    #         "'Update Password' menu item should be visible"
    #     assert settings_page.is_about_app_displayed(), \
    #         "'About App' menu item should be visible"
    #     assert settings_page.is_sign_out_displayed(), \
    #         "'Sign Out' button should be visible"
    #     assert settings_page.is_delete_account_displayed(), \
    #         "'Delete Account' button should be visible"

    # def test_sign_out_returns_to_login(self, driver):
    #     """TC-19: Verify that tapping Sign Out returns the user to the login screen."""
    #     settings_page = _navigate_to_settings(driver)
    #     login_page = LoginPage(driver)

    #     settings_page.tap_sign_out()

    #     assert login_page.is_login_screen_displayed(), \
    #         "Login screen should be displayed after signing out"
