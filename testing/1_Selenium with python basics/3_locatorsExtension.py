from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path = r"C:\drivers_browsers\chromedriver.exe")
driver.get("https://login.salesforce.com/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("daniel")
driver.find_element(By.CSS_SELECTOR, ".password").send_keys("contraseña001")
driver.find_element(By.CSS_SELECTOR, ".password").clear() # limpia lo anterior escrito
driver.find_element(By.LINK_TEXT, "¿Olvidó la contraseña?").click()

# //tagname[text()='xxx']
driver.find_element(By.XPATH, "//input[@name='cancel']").click() # boton cancelar

# EXTRAYENDO EL TEXTO "Nombre de usuario" DESDE XPATH.
#<form name="login" method="post" id="login_form" onsubmit="handleLogin();" action="https://login.salesforce.com/"
#target="_top" autocomplete="off" novalidate="novalidate">
    #<fieldset style="display:none">...</fieldset>
      #<div id="usernamegroup" class="inputgroup">
        #<label for="username" class="label usernamelabel">Nombre de usuario</label>
print(driver.find_element(By.XPATH, "//form[@name='login']/div[1]/label").text)  #div[1] toma el 1er div luego baja al hijo tag label

# EXTRAYENDO EL TEXTO "Contraseña" DESDE XPATH.
print(driver.find_element(By.XPATH, "//form[@name='login']/label").text)
# OTRA FORMA CON XPATH
print(driver.find_element(By.XPATH, "//label[contains(text(),'Contraseña')]").text)

