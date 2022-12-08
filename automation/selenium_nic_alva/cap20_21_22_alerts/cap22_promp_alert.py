from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("file:///C:/Users/Dael/Documents/1._IT/1.1_SELENIUM/selenium_nic_alva/alerts/promp_alert.html")
time.sleep(3)

alert = driver.find_element_by_name("mi boton de prompt alert")
alert.click()
time.sleep(3)

alert = driver.switch_to.alert
#alert.accept() # boton aceptar
alert.dismiss() # boton cancelar
time.sleep(3)
driver.close()

