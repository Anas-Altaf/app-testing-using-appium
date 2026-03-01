"""
SettingsPage — Page Object for the Profile / Settings screen.

Locators derived from the actual app XML hierarchy dump.
The app calls this screen "Profile" (visible in the heading).
"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class SettingsPage(BasePage):
    """Encapsulates locators and actions for the Profile/Settings screen."""

    # ── Locators ─────────────────────────────────────────────────
    # Header
    PROFILE_HEADER = (AppiumBy.XPATH, '//android.view.View[@text="Profile"]')

    # User info
    USER_NAME = (AppiumBy.XPATH,
        '//android.widget.TextView[@text="Anas Altaf"]')
    USER_EMAIL = (AppiumBy.XPATH,
        '//android.widget.TextView[@text="anasaltafprojects@gmail.com"]')

    # General settings section
    GENERAL_SETTING_HEADER = (AppiumBy.XPATH,
        '//android.widget.TextView[@text="General Setting"]')
    UPDATE_PASSWORD = (AppiumBy.ACCESSIBILITY_ID, "Update Password")
    PUSH_NOTIFICATION = (AppiumBy.ACCESSIBILITY_ID, "Push Notifcation")
    ABOUT_APP = (AppiumBy.ACCESSIBILITY_ID, "About App")
    TERMS_CONDITIONS = (AppiumBy.ACCESSIBILITY_ID, "Terms & Conditions")
    PRIVACY_POLICY = (AppiumBy.ACCESSIBILITY_ID, "Privacy Policy")

    # Danger zone
    DELETE_ACCOUNT = (AppiumBy.ACCESSIBILITY_ID, "Delete Account")
    SIGN_OUT = (AppiumBy.ACCESSIBILITY_ID, "Sign Out")

    # ── Actions ──────────────────────────────────────────────────

    def tap_update_password(self):
        """Tap the 'Update Password' menu item."""
        self.click(self.UPDATE_PASSWORD)

    def tap_push_notification(self):
        """Tap the 'Push Notification' menu item."""
        self.click(self.PUSH_NOTIFICATION)

    def tap_about_app(self):
        """Tap the 'About App' menu item."""
        self.click(self.ABOUT_APP)

    def tap_terms_conditions(self):
        """Tap the 'Terms & Conditions' menu item."""
        self.click(self.TERMS_CONDITIONS)

    def tap_privacy_policy(self):
        """Tap the 'Privacy Policy' menu item."""
        self.click(self.PRIVACY_POLICY)

    def tap_delete_account(self):
        """Tap the 'Delete Account' button."""
        self.click(self.DELETE_ACCOUNT)

    def tap_sign_out(self):
        """Tap the 'Sign Out' button."""
        self.click(self.SIGN_OUT)

    # ── Queries ──────────────────────────────────────────────────

    def is_settings_displayed(self):
        """Return True if the Profile header is visible."""
        return self.is_element_displayed(self.PROFILE_HEADER)

    def is_user_name_displayed(self):
        """Return True if the user's name is visible on the profile."""
        return self.is_element_displayed(self.USER_NAME)

    def is_user_email_displayed(self):
        """Return True if the user's email is visible on the profile."""
        return self.is_element_displayed(self.USER_EMAIL)

    def is_general_setting_displayed(self):
        """Return True if the 'General Setting' section header is visible."""
        return self.is_element_displayed(self.GENERAL_SETTING_HEADER)

    def is_update_password_displayed(self):
        """Return True if the 'Update Password' option is visible."""
        return self.is_element_displayed(self.UPDATE_PASSWORD)

    def is_about_app_displayed(self):
        """Return True if the 'About App' option is visible."""
        return self.is_element_displayed(self.ABOUT_APP)

    def is_sign_out_displayed(self):
        """Return True if the 'Sign Out' button is visible."""
        return self.is_element_displayed(self.SIGN_OUT)

    def is_delete_account_displayed(self):
        """Return True if the 'Delete Account' button is visible."""
        return self.is_element_displayed(self.DELETE_ACCOUNT)

    def get_user_name_text(self):
        """Return the user name text from the profile."""
        try:
            return self.get_text(self.USER_NAME)
        except Exception:
            return ""

    def get_user_email_text(self):
        """Return the user email text from the profile."""
        try:
            return self.get_text(self.USER_EMAIL)
        except Exception:
            return ""
