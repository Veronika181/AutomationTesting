import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages import main
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from datetime import datetime


driver = webdriver.Chrome()
login_page = LoginPage(driver)

main_page = MainPage(driver)
main_page.navigate_to_buynewcard_page()
main_page.enter_SPZ("5P35010")
login_page.accept_cookies()
main_page.click_continue()
main_page.select_fuel_type()
main_page.click_continue()
main_page.select_kind_card()
main_page.validity_card()
time.sleep(2)
main_page.click_continue()
main_page.emails()
main_page.emailsrepeat()
main_page.checkbox()
main_page.emailcheckconfirm()
main_page.mobilenumber()
main_page.click_continue()
main_page.payment()
main_page.conditions()
main_page.payButtonExist()





