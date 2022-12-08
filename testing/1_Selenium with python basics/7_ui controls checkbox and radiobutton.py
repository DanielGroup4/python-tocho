from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path = r"C:\drivers_browsers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

# Selecconar todos los checkboxes
#for checkbox in checkboxes:
    #print(checkbox.get_attribute("value"))
    #checkbox.click()
    #assert checkbox.is_selected() #validacion si los checkboxes no se vinculan correctamente

# Seleccionar solo el checkbox 2
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

# radio button
radiobuttons = driver.find_elements(By.NAME, "radioButton") # elements en plural
print(radiobuttons)
radiobuttons[2].click()
assert radiobuttons[2].is_selected()