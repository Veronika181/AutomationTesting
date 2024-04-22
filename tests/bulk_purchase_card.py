from selenium import webdriver

from pages.LoginPage import LoginPage
from pages.MainPage import MainPage

driver = webdriver.Chrome()
login_page = LoginPage(driver)

login_page.navigate_to_bulkpurchasecard
login_page.enter_SPZ

main_page = MainPage(driver)
main_page.select_fuel_type
#main_page.stampsvalidity
#main_page.daystamps
#main_page.newsetofstamps
#main_page.continuebulkpurchase
#main_page.againcontinue
#login_page.email
#login_page.email
#login_page.checkboxnotice
#login_page.sameemailconfirmation
#login_page.telephonenumber
#login_page.click_continue()
#main_page.pay
#main_page.agreetermspayment


