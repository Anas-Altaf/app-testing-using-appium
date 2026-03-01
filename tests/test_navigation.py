"""
test_navigation.py — Screen navigation test cases.

Tests:
  12. test_navigate_to_conversations
  13. test_navigate_to_profile_settings
  14. test_navigate_back_to_home
  15. test_conversations_tabs_visible
"""
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.settings_page import SettingsPage
from pages.conversations_page import ConversationsPage


VALID_EMAIL = "anasaltafprojects@gmail.com"
VALID_PASSWORD = "Password@123"


def _login_first(driver):
    """Helper: log in so we reach the home screen."""
    login_page = LoginPage(driver)
    login_page.login(VALID_EMAIL, VALID_PASSWORD)
    return HomePage(driver)


class TestNavigation:
    """Test suite for screen-to-screen navigation."""

    def test_navigate_to_conversations(self, driver):
        """TC-12: Verify navigation from Home to Conversations screen via nav bar."""
        home_page = _login_first(driver)
        conversations_page = ConversationsPage(driver)

        # Tap 3rd nav button (index 1 = Conversations/Chat)
        home_page.tap_nav_button(1)

        assert conversations_page.is_conversations_displayed(), \
            "Conversations screen should be displayed after tapping nav button"

    def test_navigate_to_profile_settings(self, driver):
        """TC-13: Verify navigation from Home to Profile/Settings via nav bar."""
        home_page = _login_first(driver)
        settings_page = SettingsPage(driver)

        # Tap 5th nav button (index 3 = Profile/Settings)
        home_page.tap_nav_button(3)

        assert settings_page.is_settings_displayed(), \
            "Profile/Settings screen should be displayed after tapping nav button"

    def test_navigate_back_to_home(self, driver):
        """TC-14: Verify navigating back to Home after visiting Profile."""
        home_page = _login_first(driver)
        settings_page = SettingsPage(driver)

        # Navigate to Profile
        home_page.tap_nav_button(3)
        assert settings_page.is_settings_displayed(), \
            "Should navigate to Profile first"

        # Navigate back to Home via nav bar
        home_page.tap_nav_button(0)

        assert home_page.is_home_screen_displayed(), \
            "Home screen should be displayed after navigating back"

    def test_conversations_tabs_visible(self, driver):
        """TC-15: Verify Chats and Groups tabs are visible on Conversations screen."""
        home_page = _login_first(driver)
        conversations_page = ConversationsPage(driver)

        # Navigate to Conversations
        home_page.tap_nav_button(1)

        assert conversations_page.is_chats_tab_displayed(), \
            "Chats tab should be visible"
        assert conversations_page.is_groups_tab_displayed(), \
            "Groups tab should be visible"
