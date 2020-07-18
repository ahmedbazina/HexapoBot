from selenium import webdriver
from getpass import getpass
from time import sleep

from creds import username, password

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

sleep(2)

Find_btn = driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/form/div/div/div[5]/button[1]/span')
Find_btn.click()

sleep(2)

Profilepic = driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[1]/div/div[1]/div[5]/a/img')
img = Profilepic.get_attribute('src')
print(img)

Name = driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[1]/div/div[2]/div/h4/a')
name = Name.text
print(name)

Location = driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[1]/div/div[2]/div/div')
Loc = Location.text
print(Loc)

Kickstarter = driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[1]/div/div[3]/div/div[1]/a[1]')
KS = Kickstarter.get_attribute('href')
print(KS)

Facebook = driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[1]/div/div[3]/div/div[1]/a[2]')
FB = Facebook.get_attribute('href')
print(FB)

TW = driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[1]/div/div[3]/div/div[1]/a[3]')
Twitter = TW.get_attribute('href')
print(Twitter)

Category = driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/form/div/div/div[2]/select/option[15]')
Categ = Category.get_attribute('value')
print(Categ)

Backer = driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[1]/div/div[1]/div[1]')
Backed = Backer.text
print(Backed)
