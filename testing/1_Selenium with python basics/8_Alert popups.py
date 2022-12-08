from selenium import webdriver
from selenium.webdriver.common.by import By
import time

validateText = "Option3"
driver = webdriver.Chrome(executable_path = r"C:\drivers_browsers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(validateText)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert # cambiar a la alerta popup
print(alert.text)

# validation
alertText = alert.text
assert validateText in alertText
alert.accept() # click boton aceptar en popup
# alert.dismiss() # click boton cancelar en popup

