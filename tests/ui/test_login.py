import pytest
from pages.login_page import LoginPage

pytestmark = pytest.mark.ui

def test_valid_login(driver):
    """
    Test to verify that login works with valid credentials.
    - Checks if the login is successful by verifying the URL.
    """
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    get_page_url = driver.current_url
    assert "inventory" in get_page_url, "Login failed"

def test_invalid_login(driver):
    """
    Test to verify that assertionerror thrown for invalid login credentials.
    - Checks if the login has failed by verifying the URL.
    """
    login_page = LoginPage(driver)
    login_page.login("standard_user", "invalid_pass")
    get_page_url = driver.current_url
    assert not "inventory" in get_page_url, "Login failed"
