import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class usando_unittest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path= r"C:\dchrome\chromedriver.exe")

    def test_usando_ImplicitWait(self):
        driver =self.driver
        driver.implicitly_wait(5) # espera de hasta 5 segundos, si lo entra antes se ejecutan las lineas siguientes
        driver.get("http://www.google.com")
        myDynamicElement = driver.find_element_by_name("q") # el elemento puede estar cambiando

if __name__ == "__main__":
    unittest.main()


