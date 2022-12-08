from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("file:///C:/Users/Dael/Documents/1._IT/1.1_SELENIUM/selenium_nic_alva/cap41_formulario%20auto%20datos%20de%20excel/from.html")
time.sleep(3)

file_sheet = "ejemplo.xlsx"
wb = load_workbook(file_sheet)
sheets = wb.get_sheet_names()
sheet_name = wb.get_sheet_by_name("Hoja 1")
wb.close() # cerrando el arhivo excel

for i in range(1,5):
    name, last_name, age = sheet_name[f'A{i}:C{i}'][0] 
    print(name.value, last_name.value, age.value)

    driver.find_element(By.ID, "nom").send_keys(name.value)
    time.sleep(2)
    driver.find_element(By.ID, "ape").send_keys(last_name.value)
    time.sleep(2)
    driver.find_element(By.ID, "edad").send_keys(int(age.value))
    time.sleep(2)

    driver.find_element(By.ID, "enviar").click()
    time.sleep(2)
    print("datos enviados")

driver.close()