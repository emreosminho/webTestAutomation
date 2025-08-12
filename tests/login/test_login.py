import pytest
from pages.login_page import LoginPage
from utils.config import Config


def test_login_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.load(Config.BASE_URL)
    login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

    # Login başarılı olup olmadığını kontrol et
    assert "inventory.html" in driver.current_url, "Login başarısız oldu!"
    print("Login başarılı!")