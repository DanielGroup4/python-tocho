from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.youtube.com/watch?v=HXBZLTm6Z7g&t=5383s")
time.sleep(5)
driver.get_screenshot_as_file(r"C:\Users\Dael\Documents\1._IT\1.1_SELENIUM\selenium_nic_alva\mi_captura.png")
#time.sleep(3)
driver.quit()
