from selenium import webdriver
from getpass import getpass

from creds import username, password

driver = webdriver.Chrome("C:\webDrivers\chromedriver.exe")
driver.get('https://app.krowdster.co/login')
		
email_in = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[1]/input')
email_in.send_keys(username)

pw_in = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[2]/div/input')
pw_in.send_keys(password)

login_btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[3]/input')
login_btn.click()