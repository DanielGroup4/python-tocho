from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path= r"C:\drivers_browsers\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
childwindow = driver.window_handles[1] # lista de ventanas
# ('parent_id', 'child_id')

driver.switch_to.window(childwindow)
print(driver.find_element(By.TAG_NAME, "h3").text) # mostrara el texto
driver.close()
driver.switch_to.window(driver.window_handles[0]) # volver a la ventana inicial

print(driver.find_element(By.TAG_NAME, "h3").text)

assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text # esto es lo que se esta evaluando
