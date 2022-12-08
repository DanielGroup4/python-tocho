from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path= r"C:\drivers_browsers\chromedriver.exe")
driver.maximize_window()
#iframe, frameset, frame
driver.get("https://the-internet.herokuapp.com/iframe")

#frame id or frame name or index valuez
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR, "#tinymce").clear() # limpiar el contenido que ya tiene por defecto
driver.find_element(By.CSS_SELECTOR, "#tinymce").send_keys("I am able to automate")
driver.switch_to.default_content() # salir del iframe y regresar al codigo de html

print(driver.find_element(By.TAG_NAME, "h3").text)
