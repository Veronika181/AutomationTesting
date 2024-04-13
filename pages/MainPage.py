from telnetlib import EC

from selenium.webdriver.common.by import By
from datetime import datetime



def validity_card(date):
    date = datetime.now()
    #self.driver.find_element(By.ID, "valid-since-input").send_keys(date)
    print("Datum", date)


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def select_fuel_type(self):
        self.driver.find_element(By.XPATH, "//h5[contains(text(),'Standardní palivo')]")
    def select_kind_card(self):
        self.driver.find_element(By.XPATH, "//h5[contains(text(),'Roční')]").click()

    def validity_card(self):
        date = datetime.now()
        print("Datum", date)

    #def emails(self):

    def click_continue(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Pokračovat')]").click()
