import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        chrome_opciones = Options()
        chrome_opciones.add_experimental_option(
            "prefs", {
                "download.default_directory": r"C:\Users\Dael\Downloads" # mi ruta de descarga
            }
        )
        self.driver = webdriver.Chrome("chromedriver.exe", chrome_options= chrome_opciones)

    def test_descarga_archivos(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/tryit.asp?filename=tryhow_html_download_link")
        time.sleep(3)
        driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/iframe"))
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/p[2]/a/img").click()
        time.sleep(6) 
        

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
    