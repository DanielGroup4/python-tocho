from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path= r"C:\dchrome\chromedriver.exe")
driver.get("file:///C:/Users/Dael/Documents/1._IT/1.1_SELENIUM/selenium_nic_alva/alerts/alert_simple.html")
time.sleep(3)

alerta_simple = driver.find_element_by_name("alerta")
alerta_simple.click()
time.sleep(3)

alerta_simple = driver.switch_to.alert.dismiss()  # dismiss es como darle e avion a un botón
#alerta_simple.dismiss()  
time.sleep(3)
driver.close()


