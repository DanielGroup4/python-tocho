import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r"C:\dchrome\chromedriver.exe")

    def test_usando_select(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        time.sleep(5)
        selector = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")
        opcion = selector.find_elements_by_tag_name("option")
        time.sleep(5)

        for i in opcion:
            print("los valores son: {}".format(str(i.get_attribute("value"))))
            i.click()
            time.sleep(3)
        seleccionar = Select(driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))
        seleccionar.select_by_value("10")
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()
