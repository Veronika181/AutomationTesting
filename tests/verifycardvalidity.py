from selenium import webdriver
from pages.ValidationPage import ValidationPage

driver = webdriver.Chrome()
validation_page = ValidationPage(driver)

validation_page.navigate_to_verifycard()
validation_page.accept_cookies()
validation_page.enter_license_plate("5P35010")
validation_page.verifyvalidity()










