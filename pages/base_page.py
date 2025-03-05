"""
Base Page Class - Parent for All Page Objects
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    Base class for page UI interactions across this framework.

    - Provides reusable methods for interacting with web elements.
    - Implements WebDriverWait for reliable element interaction.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """Finds a single element using explicit wait."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Clicks an element after waiting for it to be visible."""
        self.find_element(locator).click()

    def fill_in_field(self, locator, value):
        """Fills in the given value after waiting for the element to be visible."""
        self.find_element(locator).send_keys(value)
        