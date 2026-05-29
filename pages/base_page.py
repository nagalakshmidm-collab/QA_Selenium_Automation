from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver: WebDriver, timeout: int = DEFAULT_TIMEOUT) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
