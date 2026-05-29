from pages.login_page import LoginPage

USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"
EXPECTED_SUCCESS_MESSAGE = "You logged into a secure area!"


class TestHerokuLogin:
    def test_successful_login_shows_flash_message(self, driver):
        login_page = LoginPage(driver).open()
        login_page.login(USERNAME, PASSWORD)

        flash_text = login_page.get_success_flash_text()

        assert EXPECTED_SUCCESS_MESSAGE in flash_text
