from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path= r"C:\drivers_browsers\chromedriver.exe")

#driver.get("https://www.familysearch.org/en/")
#ActionChains

#action.move_to_element(driver.find_element_by_id("search")).perform()

#action.move_to_element(driver.find_element_by_link_text("Genealogies")).click().perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
driver.maximize_window()
action = ActionChains(driver)
action.context_click(driver.find_element(By.ID, "double-click")).perform() # click derecho
action.double_click(driver.find_element(By.ID, "double-click")).perform()

alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()

