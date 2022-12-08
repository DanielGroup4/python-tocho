import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r"C:\dchrome\chromedriver.exe")

    def test_cambiar_ventana(self):
        driver = self.driver
        driver.get("http://www.google.com") # ventana 0
        time.sleep(5)
        driver.execute_script("window.open('');")
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1]) # posicion en pestaña 1
        driver.get("http://www.stackoverflow.com")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0]) # regresar a la pestaña 0
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()
