import pytest
from pages.login_page import LoginPage
from pages.hamburger_menu import HamburgerMenu
from utils.config import Config
import time

def test_open_all_items(driver):
    login_page = LoginPage(driver)
    login_page.load(Config.BASE_URL)
    login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

    time.sleep(2)  # Wait for the login to process

    # Hamburger menü açma işlemi
    hamburger_menu = HamburgerMenu(driver)
    hamburger_menu.open_menu()

    driver.implicitly_wait(5)  # Sayfanın yüklenmesi için bekleme süresi

    # Hamburger menüden "Tüm Ürünler" sayfasını açma işlemi
    hamburger_menu.open_all_items()

    driver.implicitly_wait(5)  # Sayfanın yüklenmesi için bekleme süresi

    # Kontrol: "Tüm Ürünler" sayfasının açıldığını kontrol et
    assert "inventory.html" in driver.current_url, "Tüm Ürünler sayfası açılmadı!"
    print("Tüm Ürünler sayfası başarılıyla açıldı!")