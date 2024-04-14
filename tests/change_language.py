from selenium import webdriver
from selenium.webdriver.common.by import By

from pages import main
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage

driver = webdriver.Chrome()
login_page = LoginPage(driver)


def changelanguage(self):
    self.driver.find_element(By.ID, "edaz-lang-select").click()
