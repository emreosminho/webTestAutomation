from selenium.webdriver.common.by import By
import time


class HamburgerMenu:
    def __init__(self, driver):
        self.driver = driver

        # Hamburger Locators
        self.menu_button = (By.ID, "react-burger-menu-btn") 


    def open_menu(self):
        self.driver.find_element(*self.menu_button).click()
