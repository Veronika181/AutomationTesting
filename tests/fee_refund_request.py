from selenium.webdriver.common.by import By

from pages.LoginPage import driver

driver.get("https://edalnice.cz")
driver.find_element(By.XPATH, "//header/div[1]/div[2]/div[2]/a[3]").click()
#stát -rolovánídriver.execute_script("window.scrollTo({}, {});".format(element_location['x'], element_location['y']))
driver.find_element(By.ID, "license-plate-input").send_keys("5P35010")
driver.find_element(By.ID, "license-plate-confirmation-input").send_keys("5P35010")
driver.find_element(By.XPATH, "//span[@class='kit__button__cont']").click()
driver.find_element(By.XPATH, "//h5[contains(text(),'Standardní palivo')]").click()
driver.find_element(By.XPATH, "//span[contains(text(),'Pokračovat')]").click()


#driver.find_element(By.XPATH, "//body/main[@id='main']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[2]/div[1]/div[2]")
#driver.find_element(By.XPATH, "//input[@id='valid-since-input']").send_keys("15.03.2024")
# driver.find_element(By.ID, "email-input").send_keys("jannovak@gmail.com")
# driver.find_element(By.ID, "email-confirmation-input").send_keys("jannovak@gmail.com")
# driver.find_element(By.ID, "zaskrnutí check").click()
# dopsat tel. čislo aasert True
# stisknout tlacitko Pokračovat
# zaskrnout platební kartou
# zaskrnoout souhlasím s podmínkami
# driver.find_element(By.XPATH, "//span[contains(text(),'Pokračovat k platbě')]").click()