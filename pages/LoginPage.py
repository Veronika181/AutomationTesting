import time
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_login_page(self):
        self.driver.get("https://edalnice.cz")

    def navigate_to_buynewcard_page(self):
        self.driver.get("https://edalnice.cz/jednoduchy-nakup/index.html#/eshop/order/license")

    def navigate_to_verifycard(self):
        self.driver.get("https://edalnice.cz/index.html#/validation")

    def enter_SPZ(self, SPZ_number):
        self.driver.find_element(By.ID, "license-plate-input").send_keys(SPZ_number)
        self.driver.find_element(By.ID, "license-plate-confirmation-input").send_keys(SPZ_number)

    def enter_license_plate(self, plate_number):
        self.driver.find_element(By.ID, "license-plate-input").send_keys(plate_number)

    def click_continue(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Pokračovat')]").click()

    def accept_cookies(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(@class,'acceptCookies')]").click()

    def verify_validity(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Ověřit platnost')]").click()

    def navigate_to_bulogin_page

    def email

    def sameemailconfirmation

    def telephonenumber

    def click_continue():




