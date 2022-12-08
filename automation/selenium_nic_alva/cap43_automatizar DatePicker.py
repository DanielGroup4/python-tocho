from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui as robot

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.bestday.com.mx")
robot.hotkey("alt", "space")
robot.hotkey("x")

# origen
cd_origen = driver.find_element(By.XPATH, "//*[@id='searchbox']/div/div/div/div[3]/div[2]/div[2]/div[1]/div/div/div/input")
cd_origen.send_keys("Celaya, Guanajuato, Mexico")
time.sleep(3)
cd_origen.send_keys(Keys.TAB)

# destino
cd_destino = driver.find_element(By.XPATH, "//*[@id='searchbox']/div/div/div/div[3]/div[2]/div[2]/div[2]/div/div/div/div/input")
cd_destino.send_keys("Monterrey, Nuevo Leon, Mexico")
time.sleep(2)
cd_destino.send_keys(Keys.TAB)
time.sleep(2)

# seleccionar ida
datapicker = driver.find_element(By.XPATH, "//*[@id='searchbox']/div/div/div/div[3]/div[2]/div[3]/div/div[1]/div/input")
datapicker.click()
mes_adelante = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div[2]/i")
mes_adelante.click()
mes_adelante.click()

dia_seleccion = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[5]/div[4]/div[4]/span[4]/span[1]")
dia_seleccion.click()
time.sleep(3)

# seleccionar regreso
dia_regreso = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[5]/div[4]/div[4]/span[6]/span[1]")
dia_regreso.click()
time.sleep(2)

btn_aplicar = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[6]/div[2]/button[2]")
btn_aplicar.click()
time.sleep(2)

# seleccionar habitacion
room = driver.find_element(By.XPATH, "//*[@id='searchbox']/div/div/div/div[3]/div[2]/div[5]/div/div/div[5]/div/div")
room.click()
time.sleep(2)

# seleccionar cantidad de personas
person = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div/a[2]")
person.click()
person.click()
time.sleep(2)

# selec personas menores
person_menor = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div/a[2]")
person_menor.click()
time.sleep(2)
#selec edad personas menores
edad_person_menor = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/select/option[6]")
edad_person_menor.click()
time.sleep(2)

# boton aplicar habitacion
btn_apli_habitacion = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/a[1]")
btn_apli_habitacion.click()
time.sleep(2)

# boton buscar
btn_search = driver.find_element(By.XPATH, "//*[@id='searchbox']/div/div/div/div[3]/div[2]/div[6]/div")
btn_search.click()
time.sleep(2)
