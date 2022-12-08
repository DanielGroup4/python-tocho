from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path = r"C:\drivers_browsers\chromedriver.exe")

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

wait = WebDriverWait(driver, 7)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)

