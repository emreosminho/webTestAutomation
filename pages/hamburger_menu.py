from selenium.webdriver.common.by import By
import time


class HamburgerMenu:
    def __init__(self, driver):
        self.driver = driver

        # Hamburger Locators
        self.menu_button = (By.ID, "react-burger-menu-btn") 
        self.menu_all_items = (By.ID, "inventory_sidebar_link")


    def open_menu(self):
        self.driver.find_element(*self.menu_button).click()

    def open_all_items(self):
        self.driver.find_element(*self.menu_all_items).click()
        
