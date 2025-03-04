from selenium import webdriver

class DriverFactory:
    """
    DriverFactory class to manage WebDriver instances.

    - Provides a reusable WebDriver factory.
    - Supports Chrome, Firefox, and Edge.
    """

    @staticmethod
    def get_driver(browser="chrome", headless=True):
        """
        Creates and returns a WebDriver instance.

        :param browser: Browser type (chrome, firefox, edge).
        :param headless: Run in headless mode (default: True).
        :return: WebDriver instance.
        """
        if browser.lower() == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument("--headless")
            return webdriver.Chrome(options=options)

        elif browser.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            return webdriver.Firefox(options=options)

        elif browser.lower() == "edge":
            options = webdriver.EdgeOptions()
            if headless:
                options.add_argument("--headless")
            return webdriver.Edge(options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")
