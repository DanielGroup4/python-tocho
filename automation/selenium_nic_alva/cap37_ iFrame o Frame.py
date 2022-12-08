import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome("chromedriver.exe")

	def test_buscar_frame(self):
		driver = self.driver
		driver.get("http://www.google.com")
		time.sleep(3)
		click1 = driver.find_element(By.ID,"gbwa") # accediendo al iframe
		time.sleep(3)
		click1.click()
		time.sleep(2)

		driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div[3]/iframe"))
		time.sleep(3)
		click2 = driver.find_element(By.ID, "yDmH0d")
		time.sleep(2)
		click2.click()
		time.sleep(5)

if __name__ == '__main__':
	unittest.main()