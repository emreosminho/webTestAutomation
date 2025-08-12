from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

class DriverFactory:
    @staticmethod
    def create_driver():
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        
        # ChromeDriver path'ini düzelt
        try:
            driver_path = ChromeDriverManager().install()
            # Windows'ta path sorununu çöz
            if os.name == 'nt':  # Windows
                driver_path = driver_path.replace('/', '\\')
            
            service = ChromeService(driver_path)
            return webdriver.Chrome(service=service, options=options)
        except Exception as e:
            print(f"ChromeDriver kurulumunda hata: {e}")
            # Fallback olarak sistem PATH'indeki chromedriver'ı kullan
            return webdriver.Chrome(options=options)
