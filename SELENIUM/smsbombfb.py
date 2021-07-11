
import selenium 
from selenium import webdriver
import time

browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://www.facebook.com/login/identify/?ctx=recover")

number = browser.find_element_by_xpath('//*[@id="identify_email"]')
submit = browser.find_element_by_xpath('//*[@id="did_submit"]')



number.send_keys('+917015069609')
submit.click()
time.sleep(2)


final_submit=browser.find_element_by_xpath('//*[@id="initiate_interstitial"]/div[3]/div/div[1]/button')
final_submit.click()