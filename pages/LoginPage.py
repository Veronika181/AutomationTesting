import time
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_login_page(self):
        self.driver.get("https://edalnice.cz")

    def accept_cookies(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(@class,'acceptCookies')]").click()
