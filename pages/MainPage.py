import email
from telnetlib import EC

from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def validity_card(date):
        date = datetime.now()
        # self.driver.find_element(By.ID, "valid-since-input").send_keys(date)
        print("Datum", date)

    def select_fuel_type(self):
        fuel_type = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h5[contains(text(),'Standardní palivo')]"))
        )
        fuel_type.click()


    def select_kind_card(self):
        self.driver.find_element(By.XPATH, "//h5[contains(text(),'Roční')]").click()

    def validity_card(self):
        date = datetime.today()
        self.driver.find_element(By.ID, "valid-since-input").send_keys(date.strftime("%d.%m.%Y"))

    def emails(self):
        self.driver.find_element(By.XPATH, "//input[@id='email-input']").send_keys("jannovak@seznam.cz")

    def click_continue(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Pokračovat')]").click()