import unittest
import string
import sys
import random
import datetime
from selenium.webdriver.common import action_chains  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PythonSpaceRunnerSupportUnitTest(unittest.TestCase):

    def __init__(self, methodName = 'runTest'):
        #Screenshot dir
        self.imageDir = os.path.dirname(os.path.realpath(__file__)) + "\\PyScreenShots\\"

        #Login information
        self.url = ""
        self.adminUserName = ""
        self.adminPassword = ""

        #Application Buttons and links
        self.excelButtonClassName = "k-i-excel"
        self.eventsButtonClassName = "icon-events"
        self.catalogLinkClass = "icon-catalog"
        self.catalogGridLinkClass = "k-grid-content"
        self.catalogGridRowXPath = "//td[1]"
        self.logoutLinkXPath = "//ul[@id='topNavBarLinks']/li[2]/a"
        
        #webDriver setup
        self.chromDriverEXE = os.path.dirname(os.path.realpath(__file__)) + "\\webDriver\\chromedriver.exe"
        self.myPyDriver = webdriver.Chrome(self.chromDriverEXE)
        #self.myPyDriver = webdriver.Firefox()
        
        #wait setup
        self.wait = WebDriverWait(self.myPyDriver, 15)
        
        #init Action chains
        self.action = action_chains.ActionChains(self.myPyDriver)
        
        #init time stamp 
        self.now = datetime.datetime.now()
        self.date = self.now.strftime('%H%M%S_%m%d%y')

        if self.myPyDriver:
            self.myPyDriver.get(self.url)
            self.assertTrue( self.myPyDriver.title == "SpaceRunner" )
            self.wait.until(EC.presence_of_element_located((By.NAME,"userName")))
            self.userNameField = self.myPyDriver.find_element_by_name("userName")
            self.userNameField.send_keys(self.adminUserName)
            self.userPassword = self.myPyDriver.find_element_by_name("pwInput")
            self.userPassword.send_keys(self.adminPassword)
            self.loginSubmitButton = self.myPyDriver.find_element_by_name("submit")
            self.loginSubmitButton.click()
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"icon-home")))
            return super(PythonSpaceRunnerSupportUnitTest, self).__init__(methodName)
        else:
            print("Unable to init webDriver!")

if __name__ == '__main__':
    unittest.main()
