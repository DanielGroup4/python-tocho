from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("file:///C:/Users/Dael/Documents/1._IT/1.1_SELENIUM/selenium_nic_alva/cap41_Auto_llenar_formulario/login.html")
time.sleep(3)

#inicia ciclo de auto llenado de form
with open("datos.txt") as file:
    for i, line in enumerate(file):
        usuario = (line)
        sep = ","
        dividir = usuario.split(sep)
        try:
            got_data = dividir[1]
            user_name = dividir[0]
            user_pass = dividir[1]
        except IndexError:
            got_data = "null"

        print(user_name)
        print(user_pass)
        driver.find_element(By.ID, "login").send_keys(user_name)
        time.sleep(2)
        driver.find_element(By.ID, "cont").send_keys(user_pass)
        time.sleep(2)
        driver.find_element(By.ID, "acce").click() # click en boton
        time.sleep(2)

file.close()
driver.close()
