from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path= r"C:\dchrome\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")
time.sleep(5)

# valor = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr[2]/td[2]").text
# print(valor)

filas = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
columnas =len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th"))

print(filas)
print(columnas)

for i in range(2, filas + 1):
	for j in range(1, columnas + 1):
		datos = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
		print(datos, end='		')
	print()

# otra alternativa en a partir de la linea 8
"""
tabla = driver.find_elements(By.CSS_SELECTOR, "table#customers")
filas = tabla.find_elements(By.CSS_SELECTOR, "tr")
for fila in filas:
    fila = fila.find_elements(By.CSS_SELECTOR, "th, td")
    print([c.text for c in fila])
"""