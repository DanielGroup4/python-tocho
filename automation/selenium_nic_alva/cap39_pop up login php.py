from selenium import webdriver
import keyboard
import pyautogui
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("http://217.182.87.241/testlink/login.php")
time.sleep(5)

keyboard.write("my user")
time.sleep(2)
pyautogui.press("tab")
time.sleep(2)

keyboard.write("my pass123")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)

driver.close()
