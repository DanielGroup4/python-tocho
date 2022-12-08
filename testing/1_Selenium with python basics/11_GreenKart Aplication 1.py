import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

list = []
list2 = []
driver = webdriver.Chrome(executable_path= r"C:\drivers_browsers\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(5)
count = len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
# esta es pregunta de entrevista
# xpath from child to parent:
# //div[@class='product_action']/button/parent::div/parent::div/h4

for button in buttons:
    #print(button.find_element(By.XPATH, "parent::div/parent::div/h4").text) # codigo restante despues de xpath buttons
    list.append(button.find_element(By.XPATH, "parent::div/parent::div/h4").text)
    button.click()
print(list)

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()

wait = WebDriverWait(driver, 7)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))

# validate whether products selected in page 1 are showing in page 2 check page
## validar si los productos seleccionados en la página 1 se muestran en la página 2 comprobar la página
veggies = driver.find_elements(By.CSS_SELECTOR, "p.product-name")
for veg in veggies:
    list2.append(veg.text)
print(list2) # esto es para comparar ambas listas

assert list == list2

# verify if price decreases on discount
## verificar si el precio disminuye con el descuento
orginalAmount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
discountAmount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text

assert float(discountAmount) < int(orginalAmount) # esta debe regresar True

print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)

# verify if sum of products in chekout page matches with Total amount
## verifica si la suma de los productos en la página de la compra coincide con el importe total
amounts = driver.find_elements(By.XPATH, "//tr/td[5]/p")

sum = 0
for amount in amounts:
    sum = sum + int(amount.text) # 32 + 48 + 60
print(sum)

totalAmount = int(driver.find_element(By.CLASS_NAME, "totAmt").text)

assert sum == totalAmount
