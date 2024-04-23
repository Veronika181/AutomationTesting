import time

from selenium import webdriver

from pages.BatchPage import BatchPage


driver = webdriver.Chrome()
batch_page = BatchPage(driver)
batch_page.navigate_to_bulkpurchasecard()
batch_page.accept_cookies()
time.sleep(2)
batch_page.enter_SPZ()
time.sleep(5)
batch_page.select_fuel_type()
time.sleep(2)
batch_page.validity_card()
batch_page.select_kind_card()
batch_page.click_continue()
batch_page.click_continue()


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


