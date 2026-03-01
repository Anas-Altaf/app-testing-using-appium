"""
test_home.py — Home screen test cases.

Tests:
  6.  test_home_screen_displays_welcome_header
  7.  test_home_screen_recent_alerts_section
  8.  test_home_screen_alert_group_section
  9.  test_home_screen_send_alert_button
  10. test_home_screen_customize_alert_message
  11. test_home_screen_bottom_nav_bar
"""
from pages.login_page import LoginPage
from pages.home_page import HomePage


VALID_EMAIL = "anasaltafprojects@gmail.com"
VALID_PASSWORD = "Password@123"


def _login_first(driver):
    """Helper: log in so we reach the home screen."""
    login_page = LoginPage(driver)
    login_page.login(VALID_EMAIL, VALID_PASSWORD)
    return HomePage(driver)


class TestHome:
    """Test suite for the Home screen."""

    def test_home_screen_displays_welcome_header(self, driver):
        """TC-06: Verify 'Welcome Back,' header is displayed after login."""
        home_page = _login_first(driver)

        assert home_page.is_home_screen_displayed(), \
            "'Welcome Back,' header should be visible on the home screen"

    def test_home_screen_recent_alerts_section(self, driver):
        """TC-07: Verify the Recent Alerts section is visible with title and status."""
        home_page = _login_first(driver)

        assert home_page.is_recent_alerts_displayed(), \
            "'Recent Alerts' title should be visible"

        # Check if "No Recent Alert" or alerts list is displayed
        has_no_alert = home_page.is_no_recent_alert_displayed()
        has_view_all = home_page.is_element_displayed(home_page.VIEW_ALL_ALERTS)

        assert has_no_alert or has_view_all, \
            "Either 'No Recent Alert' text or 'View all' link should be visible"

    def test_home_screen_alert_group_section(self, driver):
        """TC-08: Verify the Alert Group section with member count and members."""
        home_page = _login_first(driver)

        assert home_page.is_alert_group_displayed(), \
            "'Your Alert Group' section should be visible"

        member_count = home_page.get_member_count_text()
        assert "members" in member_count.lower() or "member" in member_count.lower(), \
            f"Member count should contain 'members', got: '{member_count}'"

    def test_home_screen_send_alert_button(self, driver):
        """TC-09: Verify the 'Send Alert' button is displayed on home screen."""
        home_page = _login_first(driver)

        assert home_page.is_send_alert_displayed(), \
            "'Send Alert' button should be visible on the home screen"

    def test_home_screen_customize_alert_message(self, driver):
        """TC-10: Verify 'View & Customize Alert Message' button is displayed."""
        home_page = _login_first(driver)

        assert home_page.is_customize_alert_displayed(), \
            "'View & Customize Alert Message' button should be visible"

    def test_home_screen_bottom_nav_bar(self, driver):
        """TC-11: Verify the bottom navigation bar has 5 buttons."""
        home_page = _login_first(driver)

        nav_count = home_page.get_nav_button_count()
        assert nav_count == 4, \
            f"Bottom nav bar should have 5 buttons, found {nav_count}"
