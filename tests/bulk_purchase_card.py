from selenium import webdriver

from pages import main
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage

#hromadný nakup elektronícké známky

driver = webdriver.Chrome()
login_page = LoginPage(driver)
