import HtmlTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class suite(unittest.TestCase):
    def setUp(self):
        self.cdriver = webdriver.Chrome("chromedriver.exe")

    def test_busqueda(self):
        self.cdriver.get("http:/www.google.com")
        self.busqueda = self.cdriver.find_element(By.NAME, "q") # find_element_by_name is deprecated
        self.busqueda.send_keys("selenium")
        self.busqueda.submit()
        time.sleep(3)
        self.cdriver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)

    def test_link_por_texto(self):
        driver = self.cdriver
        self.cdriver.get("https://www.w3schools.com/")
        time.sleep(5)
        continue_link = self.cdriver.find_element(By.LINK_TEXT, "Learn Python")
        continue_link.click()
        time.sleep(5)

    def tearDown(self): # cerrar los drivers
        self.cdriver.quit()

if __name__ == "__main__":
    unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner(output= "cap_29_Resultados de mi test plan"))