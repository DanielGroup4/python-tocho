import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import cv2
import time

class usando_unittest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path= r"C:\dchrome\chromedriver.exe")

    def test_usando_opencv(self):
        driver = self.driver
        driver.get("http://www.google.com")
        driver.save_screenshot("Captura2.PNG")
        time.sleep(5)

    def test_comparacion_imagenes(self):
        img1 = cv2.imread("captura1.png")
        img2 = cv2.imread("captura2.png")

        diferencia = cv2.absdiff(img1, img2)
        imagen_gris = cv2.cvtColor(diferencia, cv2.COLOR_BGR2GRAY) # escalcion de grisses
        contornos,_ = cv2.findContours(imagen_gris, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for i in contornos:
            if cv2.contourArea(i) >= 20:
                posi_x, posi_y, ancho, alto = cv2.boundingRect(i)
                cv2.rentangle(img1, (posi_x, posi_y), (posi_x + ancho, posi_y + alto), (0,0,2500), 2)

        while(1):
            cv2.imshow("imagen1", img1)
            cv2.imshow("imagen2", img2)
            cv2.imshow("diferencias reconocidas", diferencia)
            teclado = cv2.waitKey(5) & 0xFF
            if teclado == 27:
                break
        cv2.destroyAllWindows()

if __name__ == "__main__":
    unittest.main()