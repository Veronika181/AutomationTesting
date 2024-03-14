from selenium.webdriver.common.by import By

date = "20.3.2024" #napsat formatovani jak se piše v Pythonu
email = "jannovak@gmail.com"


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def select_fuel_type(self):
        self.driver.find_element(By.XPATH, "//h5[contains(text(),'Standardní palivo')]").click()

    def select_kind_card(self):
        self.driver.find_element(By.XPATH, "//h5[contains(text(),'Roční')]").click()

    def validity_card(self, date):
        assert isinstance(date, object)
        self.driver.find_element(By.ID, "valid-since-input").send_keys(date)

    def emails(self, email):
        self.driver.find_element(By.ID, "email-input").send_keys(email)

    def click_continue(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Pokračovat')]").click()
