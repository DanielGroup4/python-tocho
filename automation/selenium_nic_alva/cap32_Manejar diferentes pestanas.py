import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")

    def test_manejando_ventanas(self):
        self.driver.get("https://www.google.com/intl/es/gmail/about/#")
        time.sleep(5)
        siguiente = self.driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div/div/div/div[1]/div[3]/div[1]/a/span[2]")
        siguiente.click()
        print(self.driver.current_window_handle)
        time.sleep(3)

        handles = self.driver.window_handles # aqui se crea la instancia de window handles
        for handle in handles:
            self.driver.switch_to.window(handle) # cambiar de pestaña
            print(self.driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()