
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages import main
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from datetime import datetime


driver = webdriver.Chrome()
login_page = LoginPage(driver)

login_page.navigate_to_buynewcard_page()
login_page.enter_SPZ("5P35010")
login_page.accept_cookies()
login_page.click_continue()

main_page = MainPage(driver)
main_page.select_fuel_type()
main_page.click_continue()
main_page.select_kind_card()
main_page.validity_card()
main_page.click_continue()
main_page.emails()
main_page.emails()
main_page.check_box()
main_page.mobilenumber()
main_page.click_continue()
main_page.conditions()
main_page.click_continue()
main_page.cancelpayment()



