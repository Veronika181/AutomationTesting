from datetime import datetime
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
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
        self.driver.find_element(By.XPATH, "//input[@class='order-0 flex-grow-1']").click()
        self.driver.find_element(By.XPATH, "//input[@class='order-0 flex-grow-1']").send_keys("3M40045")
        self.driver.find_element(By.XPATH, "//input[@class='order-0 flex-grow-1']").send_keys(Keys.ENTER)

    def select_fuel_type(self):
        fuel_type = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//h5[contains(text(),'Biometan')]"))
        )
        fuel_type.click()

    def validity_card(self):
        date = datetime(2024, 4, 26)
        self.driver.find_element(By.ID, "valid-since-input").send_keys(date.strftime("%d.%m.%Y"))

    def select_kind_card(self):
        self.driver.find_element(By.XPATH, "//h5[contains(text(),'Roční')]").click()

    def click_continue(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Pokračovat')]").click()



