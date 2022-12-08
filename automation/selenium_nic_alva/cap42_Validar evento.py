import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'C:\dchrome\chromedriver.exe')

    def test_text_validacion_evento(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
        time.sleep(3)
        radio_bt = driver.find_element(By.XPATH, "//*[@id='main']/div[3]/div[1]/input[4]")
        time.sleep(8) # para visualizar este evento aumenta el tiempo a 10 y cerrar el navegar antes de los 10 seg

        try:
            radio_bt.click()
            time.sleep(3)
        except WebDriverException as e:
            print("No se ejecuto el evento del radio_button") # true
            print(e) # false
            time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == "_-main__":
    unittest.main()

