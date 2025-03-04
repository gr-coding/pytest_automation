"""
Login Page - Implements Page Object Model (POM)
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """
    Page Object Model for the Login Page.

    - Contains locators for login elements.
    - Implements reusable methods for login interactions.
    """

    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def login(self, username, password):
        """Performs login action."""
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def is_login_successful(self):
        """Checks if login is successful based on the URL."""
        return "inventory" in self.driver.current_url
