"""
ConversationsPage — Page Object for the Conversations / Chat screen.

Locators derived from the actual app XML hierarchy dump.
"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ConversationsPage(BasePage):
    """Encapsulates locators and actions for the Conversations screen."""

    # ── Locators ─────────────────────────────────────────────────
    # Header
    CONVERSATIONS_HEADER = (AppiumBy.XPATH,
        '//android.view.View[@text="Conversations"]')

    # Tabs
    CHATS_TAB = (AppiumBy.ACCESSIBILITY_ID, "Chats")
    GROUPS_TAB = (AppiumBy.ACCESSIBILITY_ID, "Groups")
    CHATS_TAB_TEXT = (AppiumBy.XPATH, '//android.widget.TextView[@text="Chats"]')
    GROUPS_TAB_TEXT = (AppiumBy.XPATH, '//android.widget.TextView[@text="Groups"]')

    # Chat entries — identified by content-desc containing user name and message
    CHAT_ENTRIES = (AppiumBy.XPATH,
        '//android.view.ViewGroup[contains(@content-desc, ", ") and '
        'contains(@content-desc, "ago")]')

    # ── Actions ──────────────────────────────────────────────────

    def tap_chats_tab(self):
        """Tap the Chats tab."""
        self.click(self.CHATS_TAB)

    def tap_groups_tab(self):
        """Tap the Groups tab."""
        self.click(self.GROUPS_TAB)

    def tap_chat_entry(self, index=0):
        """Tap a chat entry by index."""
        entries = self.get_chat_entries()
        if entries and index < len(entries):
            entries[index].click()

    # ── Queries ──────────────────────────────────────────────────

    def is_conversations_displayed(self):
        """Return True if the Conversations header is visible."""
        return self.is_element_displayed(self.CONVERSATIONS_HEADER)

    def is_chats_tab_displayed(self):
        """Return True if the Chats tab is visible."""
        return self.is_element_displayed(self.CHATS_TAB_TEXT)

    def is_groups_tab_displayed(self):
        """Return True if the Groups tab is visible."""
        return self.is_element_displayed(self.GROUPS_TAB_TEXT)

    def get_chat_entries(self):
        """Return list of chat entry elements."""
        try:
            return self.find_elements(self.CHAT_ENTRIES)
        except Exception:
            return []

    def get_chat_entries_count(self):
        """Return the number of chat entries visible."""
        return len(self.get_chat_entries())
