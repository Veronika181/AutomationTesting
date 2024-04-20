import email
from telnetlib import EC

from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def select_fuel_type(self):
        fuel_type = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h5[contains(text(),'Standardní palivo')]"))
        )
        fuel_type.click()

    def select_kind_card(self):
        self.driver.find_element(By.XPATH, "//h5[contains(text(),'Roční')]").click()

    def validity_card(self):
        date = datetime(2024, 4, 20)
        self.driver.find_element(By.ID, "valid-since-input").send_keys(date.strftime("%d.%m.%Y"))

    def emails(self):
        self.driver.find_element(By.XPATH, "//input[@id='email-input']").send_keys("jannovak@seznam.cz")

    def emailsrepeat(self):
        self.driver.find_element(By.XPATH, "//input[@id='email-confirmation-input']").send_keys("jannovak@seznam.cz")

    def click_continue(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Pokračovat')]").click()

    def checkbox(self):
        self.driver.find_element(By.XPATH, "//input[@id ='notificationEnabled-true']").click()

    def emailcheckconfirm(self):
        self.driver.find_element(By.XPATH, "//input[@id='_isNotificationEmailSame-true']").click()

    def mobilenumber(self):
        self.driver.find_element(By.XPATH, "//input[@class='kit__input-phone']").send_keys("606432999")

    def payment(self):
        self.driver.find_element(By.XPATH, "//input[@id='bank_transfer_payment_radio_array_option']").click()

    def payButtonExist(self):
        assert self.driver.find_element(By.XPATH, "//span[contains(text(),'Zaplatit')]")

    def conditions(self):
        self.driver.find_element(By.XPATH, "//input[@id='_termsAgreement-true']").click()

#přepiš jako def
main_page.SPZ
main_page.propulsionofvehicles
main_page.stampsvalidity
main_page.daystamps
main_page.newsetofstamps
main_page.continuebulkpurchase
main_page.againcontinue
main_page.pay
main_page.agreetermspayment