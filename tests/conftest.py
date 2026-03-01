"""
conftest.py — pytest fixtures for Appium driver setup and teardown.

The `driver` fixture provides a fresh Appium session for each test function,
ensuring tests are fully independent (no shared state).
"""
import pytest
from utils.driver import get_driver


@pytest.fixture(scope="function")
def driver():
    """
    Fixture: creates a new Appium driver before each test
    and quits it after the test completes (pass or fail).
    """
    _driver = get_driver()
    yield _driver
    _driver.quit()
