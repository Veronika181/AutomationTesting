from datetime import datetime
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BatchPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_bulkpurchasecard(self):
        self.driver.get("https://edalnice.cz/hromadny-nakup/index.html#/multi_eshop/batch")

    def accept_cookies(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(@class,'acceptCookies')]").click()


    def enter_SPZ(self):
        spz_element = self.driver.find_element(By.XPATH, "//span[contains(@class, 'license-plate-frame']")
        spz_element.send_keys("6T49999")

    def select_fuel_type(self):
        fuel_type = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//h5[contains(text(),'Biometan')]"))
        )
        fuel_type.click()

    def validity_card(self):
        date = datetime(2024, 4, 30)
        self.driver.find_element(By.ID, "valid-since-input").send_keys(date.strftime("%d.%m.%Y"))

    def select_kind_card(self):
        self.driver.find_element(By.XPATH, "//h5[contains(text(),'Roční')]").click()

    def click_continue(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Pokračovat')]").click()

    def emails(self):
        self.driver.find_element(By.XPATH, "//input[@id='email-input']").send_keys("jannovak@seznam.cz")

    def emailsrepeat(self):
        self.driver.find_element(By.XPATH, "//input[@id='email-confirmation-input']").send_keys("jannovak@seznam.cz")

    def checkbox(self):
        self.driver.find_element(By.XPATH, "//input[@id ='notificationEnabled-true']").click()

    def emailcheckconfirm(self):
        self.driver.find_element(By.XPATH, "//input[@id='_isNotificationEmailSame-true']").click()

    def mobilenumber(self):
        self.driver.find_element(By.XPATH, "//input[@class='kit__input-phone']").send_keys("606432999")

    def payment(self):
        self.driver.find_element(By.XPATH, "//input[@id='bank_transfer_payment_radio_array_option']").click()

    def conditions(self):
        self.driver.find_element(By.XPATH, "//input[@id='_termsAgreement-true']").click()

    def payButtonExist(self):
        assert self.driver.find_element(By.XPATH, "//span[contains(text(),'Zaplatit')]")
