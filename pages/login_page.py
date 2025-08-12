from selenium.webdriver.common.by import By
import time


class LoginPage:
    def __init__(self, driver):
        self.driver = driver


        #Login Locators
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")


    def load(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        time.sleep(2)  # Wait for the login to process, adjust as necessary





