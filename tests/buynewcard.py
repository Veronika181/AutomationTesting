from selenium import webdriver

from pages import main
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage


driver = webdriver.Chrome()
login_page = LoginPage(driver)


login_page.navigate_to_buynewcard_page()
login_page.enter_SPZ("5P35010")
login_page.click_continue()


main_page = MainPage(driver)
main_page.select_fuel_type()
main_page.click_continue()
main_page.select_kind_card()
main_page.validity_card()
main_page.click_continue()
main_page.emails()

#napsat funkci na cookies cookie_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "xpath_tlacitka_s_cookies")))

