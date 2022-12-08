import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r"C:\dchrome\chromedriver.exe")

    def test_manejando_mouse(self):
        self.driver.get("https://www.w3schools.com/")
        time.sleep(4)
        mouse_mov = self.driver.find_element(By.XPATH, "//*[@id='navbtn_exercises']")
        mouse_mov2 = self.driver.find_element(By.XPATH, "//*[@id='nav_exercises']/div/div/div[3]/a[7]")
        movimiento = ActionChains(self.driver)
        movimiento.move_to_element(mouse_mov).click().perform()
        time.sleep(4)
        movimiento.move_to_element(mouse_mov2).click().perform()
        time.sleep(4)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()