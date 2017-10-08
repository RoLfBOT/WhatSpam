from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
 
driver = webdriver.Chrome('path to chromedriver')
 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
 
target = "Name of your friend / group"
 
string = "String to send"

y_arg = '//*[@id="side"]/div[2]/div/label/input'
input_y = wait.until(EC.presence_of_element_located((By.XPATH, y_arg)))
input_y.send_keys(target + Keys.ENTER)

input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

while(1):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)