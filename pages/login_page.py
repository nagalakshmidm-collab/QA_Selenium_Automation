from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    _USERNAME = (By.ID, "username")
    _PASSWORD = (By.ID, "password")
    _LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    _SUCCESS_FLASH = (By.CSS_SELECTOR, ".flash.success")

    def open(self) -> "LoginPage":
        self.driver.get(self.URL)
        return self

    def enter_username(self, username: str) -> "LoginPage":
        field = self.wait.until(EC.visibility_of_element_located(self._USERNAME))
        field.clear()
        field.send_keys(username)
        return self

    def enter_password(self, password: str) -> "LoginPage":
        field = self.wait.until(EC.visibility_of_element_located(self._PASSWORD))
        field.clear()
        field.send_keys(password)
        return self

    def click_login(self) -> "LoginPage":
        button = self.wait.until(EC.element_to_be_clickable(self._LOGIN_BUTTON))
        button.click()
        return self

    def login(self, username: str, password: str) -> "LoginPage":
        return (
            self.enter_username(username)
            .enter_password(password)
            .click_login()
        )

    def get_success_flash_text(self) -> str:
        flash = self.wait.until(
            EC.visibility_of_element_located(self._SUCCESS_FLASH)
        )
        return flash.text.strip()
