import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=service)
    chrome.maximize_window()
    yield chrome
    chrome.quit()
