# Js DOM can access any elements on web page just like how selenium does
# selenium have a method to execute javascript code in it

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path= r"C:\drivers_browsers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME, 'name').send_keys('hello')
#print(driver.find_element(By.NAME, 'name').text) esta forma no sirve para obtener el texto hello
print(driver.find_element(By.NAME, 'name').get_attribute('value'))

# sin selenium solo con sintaxis de js
print(driver.execute_script('return document.getElementsByName("name")[0].value')) # javascript commands
