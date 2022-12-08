from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path = r"C:\drivers_browsers\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@type='submit']").click() # boton de subbmit

message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "success" in message # si esta presente en el texto de la variable message
#assert "success44455" in message