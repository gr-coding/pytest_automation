import pytest
from pages.login_page import LoginPage


@pytest.mark.ui
def test_login(driver):
    """
    Test to verify that login works with valid credentials.
    - Checks if the login is successful by verifying the URL.
    """
    login_page = LoginPage(driver)
    login_page.login("standard_user", secret_sauce)
    get_page_url = driver.current_url
    assert "inventory" in get_page_url, "Login failed"
