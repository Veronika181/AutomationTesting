import self as self
import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(executable_path="/Users/veronikaobrtelova/Downloads/chromedriver-mac-arm64/chromedriver")
driver = selenium.webdriver.Chrome(service=service_obj)


class LoginPage:
    uname_input = By.ID, "useremail"
    signinbutton = By.NAME, "submit"

    def dologin(selfself, uname, pword):
        self._enter_text(self.uname_input, uname)
        self._enter_test(self.pword_input, pword)
        self._click(self.signin_button)

# driver.maximize_window()
# driver.find_element(By.XPATH, "//header/div[1]/div[2]/div[2]/a[3]").click()
# stát -rolování
# driver.find_element(By.ID, "license-plate-input").send_keys("5P35010")
# driver.find_element(By.ID, "license-plate-confirmation-input").send_keys("5P35010")
# driver.find_element(By.XPATH, "//input[@id='valid-since-input']").send_keys("15.12.2023")
# driver.find_element(By.ID, "alternative_fuel_type_checkbox_0").click()
# driver.find_element(By.ID, "bio_methane_radio_array_option_0").click()
# driver.find_element(By.CLASS_NAME, "m-0 text-left text-sm-right text-xl-left").click()
# driver.find_element(By.ID, "email-input").send_keys("jannovak@gmail.com")
# driver.find_element(By.ID, "email-confirmation-input").send_keys("jannovak@gmail.com")
# chci obrdrzet zarktnout
# zaskrnout zaslat sms
# dopsat tel. čislo
# zaskrnout platební kartou
# zaskrnoout souhlasím s podmínkami
# driver.find_element(By.XPATH, "//span[contains(text(),'Pokračovat k platbě')]").click()
