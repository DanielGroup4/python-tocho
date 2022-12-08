import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r"C:\dchrome\chromedriver.exe")

    def test_pagina_sig_ant(self):
    	driver = self.driver
    	driver.get("http://gmail.com")
    	time.sleep(5)
    	driver.get("http://google.com")
    	time.sleep(5)
    	driver.get("http://youtube.com")
    	time.sleep(5)
    	driver.back() # esto hace que se regrese a la pagina de google
    	time.sleep(5)
    	driver.back() # regrear a la primer pagina 
    	time.sleep(5)
    	driver.forward() # ir a la pagina adelante
    	time.sleep(5)


if __name__ == '__main__':
    unittest.main()
