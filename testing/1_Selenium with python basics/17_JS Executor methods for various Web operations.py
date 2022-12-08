#Js DOM can access any elements on web page just like how selenium does
# selenium have a method to execute javascript code in it
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path= r"C:\drivers_browsers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "name").send_keys("hello")
print(driver.find_element(By.NAME, "name").text)
print(driver.find_element(By.NAME, "name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopButton = driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
driver.execute_script("arguments[0].click();", shopButton) # esto es click en codigo js

# desplazarse hacia abajo (scroll down) en js
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")








