from selenium import webdriver
from time import sleep

from creds import username, password

class KrowdsterBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://app.krowdster.co/login')

        email_in = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[1]/input')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[2]/div/input')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[3]/input')
        login_btn.click()

    def Select(self):
        backer_btn = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div/div/div[1]/div/a')
        backer_btn.click()

    

bot = KrowdsterBot()
bot.login()
bot.Select()