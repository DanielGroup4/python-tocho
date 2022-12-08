import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
	    self.driver = webdriver.Chrome("chromedriver.exe")

    def test_dobleClick(self):
        self.driver.get("https://www.w3schools.com/")
        time.sleep(4)
        accion_doble_click = self.driver.find_element(By.XPATH, "//*[@id='main']/div[4]/div/div[1]/h1")
        acciones = ActionChains(self.driver)
        acciones.double_click(accion_doble_click).perform()
        time.sleep(4)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
        unittest.main()
