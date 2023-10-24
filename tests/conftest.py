import pytest
from selenium import webdriver
import selenium
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    service_obj = Service(executable_path="/Users/veronikaobrtelova/Downloads/chromedriver-mac-arm64/chromedriver")
    #selenium.webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    driver.get("https://edalnice.cz")
    #driver.find_element()klikni na tlačitko
    driver.find_elememnt("useremail").send_keys("email")
    #driver.find_element("submit").click()
