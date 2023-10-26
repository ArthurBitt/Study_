import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
os.environ['PATH']+=r"C:\\selenium_drivers\\chromedriver-win32\\chromedriver-win32"



driver = webdriver.Chrome()
url = driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
#driver.implicitly_wait()
elemento = driver.find_element(By.ID,"downloadButton")
elemento.click()
title_element = driver.find_element(By.CLASS_NAME, "progress-label")

print(title_element.text)
time.sleep(30)