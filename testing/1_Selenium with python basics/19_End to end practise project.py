from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path= r"C:\drivers_browsers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

# //div[@class='card h-100']/div/h4/a
# product = //div[@class='card h-100']
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        # add item into cart
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 7) # 7 segundos de espera para encontrar el texto india
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
#print(driver.find_element(By.CLASS_NAME, "alert-success").text)
successText = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you" in successText # debe devolver True para que el test tenga exito

# tomar un screenshot si el test es exitoso
driver.get_screenshot_as_file("screen.png")