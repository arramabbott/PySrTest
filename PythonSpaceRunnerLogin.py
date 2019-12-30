import unittest, config, Selectors
import string
import sys
import random
import time
import datetime
import os.path
import platform
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import PyAutoGuiExporter ,PythonSpaceRunnerXyiconsUnitTest

class PythonSpaceRunnerLogin(object):
    """description of class"""
    def __init__(self, *args, **kwargs):
        self.myPyDriver = webdriver.Firefox()
        
        #wait setup
        self.wait = WebDriverWait(self.myPyDriver, 15)
        
        #init Action chains
        self.action = action_chains.ActionChains(self.myPyDriver)
        
        #init time stamp 
        self.now = datetime.datetime.now()
        self.date = self.now.strftime('%H%M%S_%m%d%y')
        config_object = config.config()
        selector_object = Selectors.Selectors()

        self.url                    = config_object.url
        self.usernameText           = config_object.usernameText
        self.passwordText           = config_object.passwordText
        self.name_userName          = selector_object.name_userName
        self.name_pwInput           = selector_object.name_pwInput
        self.name_submit            = selector_object.name_submit
        self.doneButton             = selector_object.doneButton
        self.className_IconHome     = selector_object.className_IconHome

        self.myPyDriver.get(self.url)
        self.assertTrue( self.myPyDriver.title == "SpaceRunner" )
        self.wait.until(EC.presence_of_element_located((By.NAME,self.name_userName)))
        self.userNameField = self.myPyDriver.find_element_by_name(self.name_userName)
        self.userNameField.send_keys(self.usernameText)
        self.userPassword = self.myPyDriver.find_element_by_name(self.name_pwInput)
        self.userPassword.send_keys(self.passwordText)
        self.loginSubmitButton = self.myPyDriver.find_element_by_name(self.name_submit)
        self.loginSubmitButton.click()