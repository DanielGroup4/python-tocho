import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")

    def test_subir_archivo(self):
        self.driver.get("https://mdbootstrap.com/plugins/jquery/file-upload/")
        time.sleep(4)
        self.driver.find_element(By.ID, "customFile").send_keys(
            r"C:\Users\Dael\Documents\1._IT\1.1_SELENIUM\selenium_nic_alva\fondo_pantalla.jpg")
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
