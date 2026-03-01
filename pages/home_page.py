"""
HomePage — Page Object for the Home / Main screen.

Locators derived from the actual app XML hierarchy dump.
"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class HomePage(BasePage):
    """Encapsulates locators and actions for the Home screen."""

    # ── Locators ─────────────────────────────────────────────────
    # Header
    HOME_HEADER = (AppiumBy.XPATH, '//android.widget.TextView[@text="Welcome Back,"]')

    # Recent Alerts section
    RECENT_ALERTS_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Recent Alerts"]')
    VIEW_ALL_ALERTS = (AppiumBy.ACCESSIBILITY_ID, "View all →")
    NO_RECENT_ALERT = (AppiumBy.XPATH, '//android.widget.TextView[@text="No Recent Alert"]')

    # Alert Group section
    ALERT_GROUP_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Your Alert Group"]')
    MEMBER_COUNT = (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "members")]')
    ADD_MEMBER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Add +")

    # Group member cards (by content-desc)
    GROUP_MEMBERS = (AppiumBy.XPATH,
        '//android.view.ViewGroup[contains(@content-desc, "email:")]')

    # Action buttons
    VIEW_MANAGE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "View all & Manage →")
    SEND_ALERT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Send Alert")
    CUSTOMIZE_ALERT = (AppiumBy.ACCESSIBILITY_ID, "View & Customize Alert Message")

    # Bottom navigation bar (5 buttons by index)
    NAV_BAR_BUTTONS = (AppiumBy.CLASS_NAME, "android.widget.Button")

    # ── Actions ──────────────────────────────────────────────────

    def tap_view_all_alerts(self):
        """Tap the 'View all →' link in the Recent Alerts section."""
        self.click(self.VIEW_ALL_ALERTS)

    def tap_add_member(self):
        """Tap the 'Add +' button in the Alert Group section."""
        self.click(self.ADD_MEMBER_BUTTON)

    def tap_view_manage_group(self):
        """Tap the 'View all & Manage →' button."""
        self.click(self.VIEW_MANAGE_BUTTON)

    def tap_send_alert(self):
        """Tap the 'Send Alert' button."""
        self.click(self.SEND_ALERT_BUTTON)

    def tap_customize_alert(self):
        """Tap the 'View & Customize Alert Message' button."""
        self.click(self.CUSTOMIZE_ALERT)

    def tap_nav_button(self, index):
        """Tap a bottom navigation bar button by index (0-4).

        Index mapping (from the XML):
          0 = Home
          1 = Chat/Conversations
          2 = (middle, possibly alerts)
          3 = Groups
          4 = Profile/Settings
        """
        buttons = self.find_elements(self.NAV_BAR_BUTTONS)
        if buttons and index < len(buttons):
            buttons[index].click()

    # ── Queries ──────────────────────────────────────────────────

    def is_home_screen_displayed(self):
        """Return True if the home header element is visible."""
        return self.is_element_displayed(self.HOME_HEADER)

    def is_recent_alerts_displayed(self):
        """Return True if the 'Recent Alerts' section title is visible."""
        return self.is_element_displayed(self.RECENT_ALERTS_TITLE)

    def is_no_recent_alert_displayed(self):
        """Return True if the 'No Recent Alert' message is visible."""
        return self.is_element_displayed(self.NO_RECENT_ALERT)

    def is_alert_group_displayed(self):
        """Return True if the 'Your Alert Group' section is visible."""
        return self.is_element_displayed(self.ALERT_GROUP_TITLE)

    def is_send_alert_displayed(self):
        """Return True if the 'Send Alert' button is visible."""
        return self.is_element_displayed(self.SEND_ALERT_BUTTON)

    def is_customize_alert_displayed(self):
        """Return True if the 'View & Customize Alert Message' button is visible."""
        return self.is_element_displayed(self.CUSTOMIZE_ALERT)

    def get_member_count_text(self):
        """Return the text of the member count label (e.g. '3 members')."""
        try:
            return self.get_text(self.MEMBER_COUNT)
        except Exception:
            return ""

    def get_group_members(self):
        """Return list of group member card elements."""
        try:
            return self.find_elements(self.GROUP_MEMBERS)
        except Exception:
            return []

    def get_nav_buttons(self):
        """Return a list of bottom navigation bar button elements."""
        try:
            return self.find_elements(self.NAV_BAR_BUTTONS)
        except Exception:
            return []

    def get_nav_button_count(self):
        """Return the number of bottom navigation bar buttons."""
        return len(self.get_nav_buttons())
