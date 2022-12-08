from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path = r"C:\drivers_browsers\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# clase: identifying static dropdowns using Select class of selenium
# select class provide the method to handle the options in dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)
#dropdown.select_by_value("M")

