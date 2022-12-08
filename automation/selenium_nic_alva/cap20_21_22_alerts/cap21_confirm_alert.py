from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("file:///C:/Users/Dael/Documents/1._IT/1.1_SELENIUM/selenium_nic_alva/alerts/confirm_alert.html")
time.sleep(3)

confirm_alert = driver.find_element_by_name("confirmar alert")
confirm_alert.click()
time.sleep(3)

confirm_alert = driver.switch_to.alert.dismiss() # se da click en el boton cancelar
# confirm_alert.accept() # da click en boton de aceptar
time.sleep(3)
driver.close()


