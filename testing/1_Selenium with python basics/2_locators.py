from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = r"C:\drivers_browsers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")


#driver.find_element(By.NAME, "name").send_keys("daniel")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("daniel")
driver.find_element(By.NAME, "email").send_keys("daniel_ys1@outlook.com")

driver.find_element(By.ID, "exampleCheck1").click()

driver.find_element(By.XPATH, "//input[@type='submit']").click()

print(driver.find_element(By.CLASS_NAME, "alert-success").text) # grab the text

# //*[contains(@class, 'alert-success')]  - Xpath
# [class*='alert-success']  -  CSS


