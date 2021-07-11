from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
chrome_options=Options()
chrome_options.add_argument("headless")
browser = webdriver.Chrome("chromedriver.exe",chrome_options=chrome_options)

for x in range(20):

	browser.get('https://www.instagram.com/accounts/password/reset/')
	element = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/section/main/div[2]/div/div/div/div/div[4]/form/label/input')))


	number=browser.find_element_by_xpath('/html/body/div[1]/section/main/div[2]/div/div/div/div/div[4]/form/label/input')
	submit= browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div[2]/div/div/div/div/div[5]')

	number.send_keys('+919802366015')
	submit.click()
	time.sleep(2)

	ok_button=browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/button')

	ok_button.click()
	time.sleep(3)