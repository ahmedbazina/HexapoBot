# https://www.youtube.com/watch?v=lvFAuUcowT4
# Imports the web driver and sleep from selenium & time 
from selenium import webdriver
from time import sleep

# Import Google Sheets & Oauth2client to work with Gsheets api
import gspread 
from oauth2client.service_account import ServiceAccountCredentials

# Pretty print to visualise data nicely 
from pprint import pprint

# Create a creds.py and add username and password to extract login details from their
from creds import username, password

class KrowdsterBot():
     
    def __init__(self):
        # Start web driver chrome

        self.driver = webdriver.Chrome()
 
    def login(self):
        # Login function saving xpath elements in variables with actions that send login details from creds.py and click on buttons:
        # Open the site 
        # Enter email, password & click login button
        # Sleep for 5 seconds until popup appear then close it
        # inititate/Run SelectFilters           

        self.driver.get('https://app.krowdster.co/login')
 
        email_in = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[1]/input')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[2]/div/input')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[3]/input')
        login_btn.click()

        sleep(5)

        popup_1 = self.driver.find_element_by_xpath('/html/body/div[9]/div/div[3]/div[2]/button[1]')
        popup_1.click()

        bot.SelectFilters()


    def SelectFilters(self):
        # Select filters function saving xpath elements in variables with actions that click on buttons & sleep for the page to load 

        backer_btn = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div/div/div[1]/div/a')
        backer_btn.click()

        Platform_btn = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/form/div/div/div[1]/select/option[2]')
        Platform_btn.click()

        Category_btn = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/form/div/div/div[2]/select/option[15]')
        Category_btn.click()

        sleep(5)

        Find_btn = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/form/div/div/div[5]/button[1]/span')
        Find_btn.click()

        sleep(5)

        bot.AddToSheet()
 
    def FindSingleUser(self):
        # Find single user function for debugging

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

    def AddToSheet(self):
        # Function that initiates connection with Gsheets api and dynamically add the data from the site
        # Add scope for api
        # Credentials to access api
        # inititate client connection to Gsheets api
        # Client access sheet by name and get worksheet by index

        scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        credentials = ServiceAccountCredentials.from_json_keyfile_name('bot-creds.json', scope)
        client = gspread.authorize(credentials)
        sheet = client.open('HexaPo Cost Sheet').get_worksheet(5)

        # For loop to get all backers on the page starting at 24 stopping at 0 in reverse order (downwards)
        # Insert row starting at index

        for i in range(24, 0, -1):
            Pic = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[{}]/div/div[1]/div[5]/a/img'.format(i)).get_attribute('src')
            Profile = '=IMAGE("{}")'.format(Pic)

            Name = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[{}]/div/div[2]/div/h4/a'.format(i)).text

            Loc = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[{}]/div/div[2]/div/div'.format(i)).text

            Categ = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/form/div/div/div[2]/select/option[15]').text

            KS = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[{}]/div/div[3]/div/div[1]/a[1]'.format(i)).get_attribute('href')

            FB = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[{}]/div/div[3]/div/div[1]/a[2]'.format(i)).get_attribute('href')

            TW = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[{}]/div/div[3]/div/div[1]/a[3]'.format(i)).get_attribute('href')

            Backer = self.driver.find_element_by_xpath('//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[1]/div[{}]/div/div[1]/div[1]'.format(i)).text.strip('Backed')

            row = [Profile, Name, Loc, Categ, KS, FB, TW, Backer]
            index = 2
            sheet.insert_row(row, index)

        # Variables to read all records, single row or column within the worksheet stated above 
        # Print what was read

        # allRecords = sheet.get_all_records()
        # pprint(allRecords)

        # Row = sheet.row_values(2)
        # pprint(Row)

        # Column = sheet.col_values(2)
        # pprint(Column)


    # Auto function to run the whole script 

    # def auto_run(self):
    #     while True:
    #         sleep(0.5)
    #         try:
    #             self.like()
    #         except Exception:
    #             try:
    #                 self.close_popup()
    #             except Exception:
    #                 self.close_match()


# Create an instanance of the bot and Run login function
bot = KrowdsterBot()
bot.login()