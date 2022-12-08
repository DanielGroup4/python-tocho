from selenium import webdriver
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions() # objeto de chromeOptions
chrome_options.add_argument("--start-maximized") # maxima la ventana
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors") # ignora errores


driver = webdriver.Chrome(executable_path= r"C:\drivers_browsers\chromedriver.exe", options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
