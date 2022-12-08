import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

excel_credenciales = r"C:\Users\Dael\Documents\1._IT\1.1_SELENIUM\selenium_jjoya\credenciales.xlsx"
df = pd.read_excel(excel_credenciales)
#print(df)

user = df['usuario'][0]
psw = df['contraseña'][0]
print(user)
print(psw)

url = 'https://www.linkedin.com/'

# selectores CSS
btn_inicio_sesion = "body > nav > div > a.nav__button-secondary" # copy selector
selector_usuario = "#username"
selector_contrasenia = "#password"
btn_login = "#organic-div > form > div.login__form_action_container > button"

# open browser
driver = webdriver.Chrome(executable_path= "C:\drivers_browsers\chromedriver.exe")

# maximizar pantalla
driver.maximize_window()
driver.get(url)

# acciones en la pagina
driver.find_element(By.CSS_SELECTOR, btn_inicio_sesion).click()

# logearse
driver.find_element(By.CSS_SELECTOR, selector_usuario).send_keys(user)
driver.find_element(By.CSS_SELECTOR, selector_contrasenia).send_keys(psw)
driver.find_element(By.CSS_SELECTOR, btn_login).click()

# mas acciones dentro de la pagina
time.sleep(8)

# cerrar
driver.quit()