import pytest
from pages.login_page import LoginPage
from pages.hamburger_menu import HamburgerMenu
from utils.config import Config
import time


def test_open_hamburger_menu(driver):
    login_page = LoginPage(driver)
    login_page.load(Config.BASE_URL)
    login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

    time.sleep(2)  # Bekleme: Login işlemi için bekleme süresi

    # Hamburger menu açma işlemi
    hamburger_menu = HamburgerMenu(driver)
    hamburger_menu.open_menu()

    time.sleep(1)  # Bekleme: Hamburger menünün açılması için bekleme süresi
    

    # Hamburger menünün açıldığını kontrol et
    assert driver.find_element(*hamburger_menu.menu_button).is_displayed(), "Hamburger menu açılmadı!"
    print("Hamburger menu başarılıyla açıldı!")

