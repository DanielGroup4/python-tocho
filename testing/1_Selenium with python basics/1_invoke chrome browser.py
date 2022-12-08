from selenium import webdriver

# using Chrome
#driver = webdriver.Chrome(executable_path = r"C:\drivers_browsers\chromedriver.exe")

# using firefox
#driver = webdriver.Firefox(executable_path=r"C:\drivers_browsers\geckodriver.exe")
driver = webdriver.Edge(executable_path=r"C:\drivers_browsers\msedgedriver.exe")
driver.get("https://rahulshettyacademy.com/")  # get method to hit url on browser
driver.maximize_window()

print(driver.title)
print(driver.current_url)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back() # back to main page, I put debug point in this phase
driver.refresh()
driver.close()

