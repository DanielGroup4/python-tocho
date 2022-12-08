# implicit Wait -
# pause the test for few seconds using Time class

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path = r"C:\drivers_browsers\chromedriver.exe")
# wait until 5 seconds if object is not displayed
# global wait
# 1.5 second to reach next page - execution will resume in 1.5 seconds
# if object do not show up at all, then max time your test waits for 5 seconds
# es decir, no necesariamente esperará los 5 segundos si puede abrir la pagina antes la abrirá
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(4)

count = len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))
assert count == 3

buttons = driver.find_elements(By.XPATH, "//div[@class = 'product-action']/button")
for button in buttons:
    button.click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)

