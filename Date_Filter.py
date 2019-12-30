import time
import unittest
import sys
import os, config, Selectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Date_Filter(unittest.TestCase):
    def __init__(self, filterWord, column, myPyDriver, wait):        
        self.myPyDriver = myPyDriver
        self.wait = wait
        selector_object = Selectors.Selectors()
        self.catalogFilterMenuXPath        = selector_object.catalogFilterMenuXPath
        self.filterClearButtonXPath        = selector_object.filterClearButtonXPath
        self.filterTextBar1XPath           = selector_object.filterTextBar1XPath
        self.catalogFilterButton           = selector_object.catalogFilterButton
        self.xyiconGridRow                 = selector_object.xyiconGridRow
        


        _filter = filterWord
        filterXpath = "//th["+str(column)+"]/a/span"
        for i in range(1,4):         
           time.sleep(2)
           filterButton = self.myPyDriver.find_element_by_xpath(filterXpath)
           filterButton.click()
           self.wait.until(EC.presence_of_all_elements_located((By.XPATH,self.filterTextBar1XPath))) 
           time.sleep(1)             
           self.wait.until(EC.element_to_be_clickable((By.XPATH,self.catalogFilterButton))).click()
           time.sleep(1)
           self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,'li')))          
           self.currentFilter = self.myPyDriver.find_element_by_xpath(self.catalogFilterMenuXPath+"["+str(i)+"]")
           self.currentFilter.click()
           self.textBar = self.myPyDriver.find_element_by_xpath(self.filterTextBar1XPath)
           self.textBar.clear()
           time.sleep(1)
           self.textBar.click()
           self.textBar.send_keys(_filter)            
           self.textBar.send_keys(Keys.ENTER)
           table = self.myPyDriver.find_elements_by_xpath(self.xyiconGridRow)
           for tr in table:
               tds = tr.find_elements_by_tag_name('td')               
               currentText = str(tds[(column-1)].text).lower()
               if(currentText == ''):
                   continue
               split_currentText = currentText.split('/')     #split text at '/'
               split_filter = _filter.split('/')
               xyDate = map(int, split_currentText)           #cast to integers
               fiDate = map(int, split_filter)
               dateDiff = [xyDate[0]-fiDate[0],xyDate[1]-fiDate[1],xyDate[2]-fiDate[2]]
               isCorrect = False
                
               if(i == 1):
                if(dateDiff[2] > 0):
                 isCorrect = True
                elif(dateDiff[2] == 0 and dateDiff[0] > 0):       
                 isCorrect = True
                elif(dateDiff[2] == 0 and dateDiff[0] == 0 and dateDiff[1] >= 0):
                 isCorrect = True
                self.assertTrue(isCorrect)
           
                if(i == 2):
                 if(dateDiff[2] < 0):
                  isCorrect = True
                 elif(dateDiff[2] == 0 and dateDiff[0] < 0):       
                  isCorrect = True
                 elif(dateDiff[2] == 0 and dateDiff[0] == 0 and dateDiff[1] <= 0):
                  isCorrect = True
                 self.assertTrue(isCorrect)
          
                 if(i == 3):
                  self.assertTrue(fiDate == xyDate)
           
           time.sleep(1)
           self.myPyDriver.find_element_by_xpath(filterXpath).click()
           time.sleep(1)
           self.wait.until(EC.element_to_be_clickable((By.XPATH,self.filterClearButtonXPath))).click()


