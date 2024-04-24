from selenium import webdriver
from pages.LoginPage import LoginPage

driver = webdriver.Chrome()
login_page = LoginPage(driver)
