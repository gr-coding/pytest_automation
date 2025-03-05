
import pytest
from utils.driver_factory import DriverFactory

def pytest_addoption(parser):
    """
    Adds command-line options for:
    - `--browser`: Select a browser (chrome, firefox, edge).
    
    Example Usage:
    pytest --browser=firefox
    """
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to run tests (chrome, firefox, edge)"
    )

@pytest.fixture(scope="function")
def driver(request):
    """
    Pytest fixture to initialize and close WebDriver instance.

    - Reads browser type from command-line arguments.
    - Reads `base_url` from test-level parameters.
    - Uses DriverFactory to create a WebDriver instance.
    """
    browser = request.config.getoption("--browser")
    base_url = "https://www.saucedemo.com/"

    driver = DriverFactory.get_driver(browser=browser)
    driver.get(base_url)
    yield driver
    driver.quit()
