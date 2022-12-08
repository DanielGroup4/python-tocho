import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

excel_songs = r"C:\Users\Dael\Documents\1._IT\1.1_SELENIUM\selenium_jjoya\yt_songs.xlsx"
df = pd.read_excel(excel_songs, sheet_name= "song list")
print(df)

url = "https://www.youtube.com"

path_search = "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input"
btn_search = "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button"
path_song = "/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]"

# open browser
driver = webdriver.Chrome(executable_path= "C:\drivers_browsers\chromedriver.exe")
# maximizar pantalla
driver.maximize_window()
driver.get(url)

for i in df.index:
    song = str(df["song"][i])
    # tipear la cancion
    driver.find_element(By.XPATH, path_search).send_keys(song)
    driver.find_element(By.XPATH, btn_search).click()
    # esperar que aparezcan los elementos
    wait = WebDriverWait(driver, 10) # max 10 seg
    wait.until(ec.visibility_of_element_located((By.XPATH, path_song)))
    # entrar en la cancion
    driver.find_element(By.XPATH, path_song).click()
    # enjoy the song
    time.sleep(20)
    # Borrar la busqueda actual
    driver.find_element(By.XPATH, path_song).clear()
driver.quit()

