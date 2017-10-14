from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib

def getImage():
	
	driver = webdriver.Chrome('/home/kaustabh/Downloads/chromedriver')
	driver.get("ttps://web.whatsapp.com")
	wait = WebDriverWait(driver, 600)

	
	img_arg = '//*[@id="app"]/div/div/div/div[1]/div[1]/div/img'
	img = wait.until(EC.presence_of_element_located((By.XPATH, img_arg)))
	src = img.get_attribute('src')
	urllib.urlretrieve(src, "qr.png")
