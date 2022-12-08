import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # acciones de teclado
import time

path_driver = r'C:\Users\Dael\Documents\1._IT\1_PYTHON\commited\webScraping\chromedriver.exe'


class usandoUnittest(unittest.TestCase):

    def setUp(self):
        """inicializar el driver"""
        self.driver = webdriver.Chrome(executable_path=path_driver)

    def test_buscar(self):
        driver = self.driver
        driver.get('http://www.google.com')
        self.assertIn('Google', driver.title)
        elemento = driver.find_element_by_name('q')  # barra de busqueda de google
        elemento.send_keys('selenium')
        elemento.send_keys(Keys.RETURN)  # RETURN es como un enter
        time.sleep(6)
        assert 'No se encontró el elemento' not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
