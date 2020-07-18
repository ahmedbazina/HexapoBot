import gspread 
from selenium import webdriver
from time import sleep
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
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

        sleep(6)

        popup_1 = self.driver.find_element_by_xpath('/html/body/div[9]/div/div[3]/div[2]/button[1]')
        popup_1.click()

            
    def SelectFilters(self):
        backer_btn = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div/div/div[1]/div/a')
        backer_btn.click()

        Platform_btn = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/form/div/div/div[1]/select/option[2]')
        Platform_btn.click()

        Category_btn = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/form/div/div/div[2]/select/option[15]')
        Category_btn.click()

        sleep(2)

        Find_btn = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/form/div/div/div[5]/button[1]/span')
        Find_btn.click()

        sleep(2)


    def data(self):
        Pic = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[1]/div/div[1]/div[5]/a/img')
        Profilepic = Pic.get_attribute('src')
        print(Profilepic)
                
        name = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[1]/div/div[2]/div/h4/a')
        Name = name.text
        print(Name)

        Loc = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[1]/div/div[2]/div/div')
        Location = Loc.text
        print(Location)

        Categ = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/form/div/div/div[2]/select/option[15]')
        Category = Categ.text
        print(Category)

        KS = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[1]/div/div[3]/div/div[1]/a[1]')
        Kickstarter = KS.get_attribute('href')
        print(Kickstarter)
         
        FB = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[1]/div/div[3]/div/div[1]/a[2]')
        Facebook = FB.get_attribute('href')
        print(Facebook)

        TW = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[1]/div/div[3]/div/div[1]/a[3]')
        Twitter = TW.get_attribute('href')
        print(Twitter)

        Backer = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[1]/div/div[1]/div[1]')
        Backed = Backer.text
        print(Backed)


def Gsheets():
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name('bot-creds.json', scope)
    client = gspread.authorize(credentials)
    sheet = client.open('HexaPo Cost Sheet').get_worksheet(5)

    data = sheet.get_all_records()
    data2 = sheet.row_values(2)
    data3 = sheet.col_values(2)

    pprint(data)
    pprint(data2)
    pprint(data3)


bot = KrowdsterBot()
bot.login()
bot.SelectFilters()
bot.data()

#Gsheets()
