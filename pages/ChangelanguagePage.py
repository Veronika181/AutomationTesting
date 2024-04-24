from selenium.webdriver.common.by import By


class ChangelanguagePage:
    def __init__(self, driver):
        self.driver = driver

    def CS(self):
        self.driver.find_element(By.ID, "edaz-lang-select").click()

    def EN(self):
        self.driver.find_element(By.ID, "edaz-lang-select").click()

    def DE(self):
        self.driver.find_element(By.ID, "edaz-lang-select").click()

    def RU(self):
        self.driver.find_element(By.ID, "edaz-lang-select").click()

    def PL(self):
        self.driver.find_element(By.ID, "edaz-lang-select").click()

    def HU(self):
        self.driver.find_element(By.ID, "edaz-lang-select").click()
