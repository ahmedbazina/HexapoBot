import gspread 
from selenium import webdriver
from time import sleep
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from creds import username, password
import re


driver = webdriver.Chrome("C:\webDrivers\chromedriver.exe")
driver.get('https://app.krowdster.co/login')
		
email_in = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[1]/input')
email_in.send_keys(username)

pw_in = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[2]/div/input')
pw_in.send_keys(password)

login_btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[3]/input')
login_btn.click()

backer_btn = driver.find_element_by_xpath('//*[@id="wrapper"]/article/div/div/div[1]/div/a')
backer_btn.click()

Platform_btn = driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/form/div/div/div[1]/select/option[2]')
Platform_btn.click()

Category_btn = driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/form/div/div/div[2]/select/option[15]')
Category_btn.click()

sleep(5)

Find_btn = driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/form/div/div/div[5]/button[1]/span')
Find_btn.click()

sleep(5)

def data():
	scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
	credentials = ServiceAccountCredentials.from_json_keyfile_name('bot-creds.json', scope)
	client = gspread.authorize(credentials)
	sheet = client.open('HexaPo Cost Sheet').get_worksheet(6)
	
	# For loop to get all backers on the page starting at 24 stopping at 0 in reverse order (downwards)
	for i in range(24, 0, -1):
		Pic = driver.find_element_by_xpath("//*[@id='wrapper']/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[{}]/div/div[1]/div[5]/a/img".format(i)).get_attribute('src')
		image = '=IMAGE("{}")'.format(Pic)

		Name = driver.find_element_by_xpath("//*[@id='wrapper']/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[{}]/div/div[2]/div/h4/a".format(i)).text

		Loc = driver.find_element_by_xpath("//*[@id='wrapper']/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[{}]/div/div[2]/div/div".format(i)).text

		Categ = driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/form/div/div/div[2]/select/option[15]').text

		KS = driver.find_element_by_xpath("//*[@id='wrapper']/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[{}]/div/div[3]/div/div[1]/a[1]".format(i)).get_attribute('href')

		FB = driver.find_element_by_xpath("//*[@id='wrapper']/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[{}]/div/div[3]/div/div[1]/a[2]".format(i)).get_attribute('href')

		TW = driver.find_element_by_xpath("//*[@id='wrapper']/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[{}]/div/div[3]/div/div[1]/a[3]".format(i)).get_attribute('href')

		Backer = driver.find_element_by_xpath("//*[@id='wrapper']/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[{}]/div/div[1]/div[1]".format(i)).text.strip('Backed')

		#print(Backer.strip('Backed'))

		row = [image, Name, Loc, Categ, KS, FB, TW, Backer]
		index = 2
		sheet.insert_row(row, index)

data()	