from selenium import webdriver
from pages.ChangelanguagePage import ChangelanguagePage

driver = webdriver.Chrome()
change_language = ChangelanguagePage(driver)

change_language.CS()
