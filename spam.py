from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def getParams():
	target = input("Enter target >>>")
	message = input("Enter message to send>>>")
	number = input("How many times to spam>>>")
	return target, message, number

def sendSpam():
	target, message, number = getParams()

	driver = webdriver.Chrome('/home/Downloads/chromedriver')
	driver.get("https://web.whatsapp.com/")
	wait = WebDriverWait(driver, 600)

	#find the search bar 
	y_arg = '//*[@id="side"]/div[2]/div/label/input'
	input_y = wait.until(EC.presence_of_element_located((By.XPATH, y_arg)))

	#search for target and hit enter
	input_y.send_keys(target + Keys.ENTER)

	#search for text input
	input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
	
	#fire away
	for i in range(int(number)):
		input_box.send_keys(message + Keys.ENTER)
		time.sleep(1)

if __name__ == '__main__':
	sendSpam()