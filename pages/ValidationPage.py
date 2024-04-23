import time

from selenium.webdriver.common.by import By


class ValidationPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_verifycard(self):
        self.driver.get("https://edalnice.cz/index.html#/validation")

    def enter_license_plate(self, plate_number):
        self.driver.find_element(By.ID, "license-plate-input").send_keys(plate_number)

    def verifyvalidity(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Ověřit platnost')]").click()

    def accept_cookies(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(@class,'acceptCookies')]").click()


