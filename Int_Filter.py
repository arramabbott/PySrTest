import time
import unittest
import sys
import os, config, Selectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Int_Filter(unittest.TestCase):
        
    def __init__(self, filterWord, column, myPyDriver, wait):    
        self.myPyDriver = myPyDriver
        self.wait = wait
        selector_object = Selectors.Selectors()
        self.catalogFilterMenuXPath        = selector_object.catalogFilterMenuXPath
        self.filterClearButtonXPath        = selector_object.filterClearButtonXPath
        self.filterTextBar1XPath           = selector_object.filterTextBar1XPath
        self.catalogFilterButton           = selector_object.catalogFilterButton
        self.xyiconGridRow                 = selector_object.xyiconGridRow
        self.filterSubmitButtonXPath       = selector_object.filterSubmitButtonXPath
        
        _filter = filterWord
        filterXpath = "//th["+str(column)+"]/a/span"
        for i in range(1,7):         
           time.sleep(1)
           filterButton = self.myPyDriver.find_element_by_xpath(filterXpath)
           time.sleep(1)
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
           #self.textBar.click()
  
           count = 1
           self.upButton = self.myPyDriver.find_element_by_xpath('//span[2]/span/span/span/span')
           while(count<=int(_filter)):
               self.upButton.click()
               count = count + 1;
           self.myPyDriver.find_element_by_xpath(self.filterSubmitButtonXPath).click()        
  
           table = self.myPyDriver.find_elements_by_xpath(self.xyiconGridRow)
           for tr in table:
               tds = tr.find_elements_by_tag_name('td')
               currentText = str(tds[(column-1)].text).lower()
               if(i == 1):
                 self.assertTrue(_filter == currentText)
               if(i == 2):
                self.assertTrue(_filter != currentText)
               if(i == 3):
                self.assertTrue(int(_filter) <= int(currentText))
               if(i == 4):
                self.assertTrue(int(_filter) < int(currentText))
               if(i == 5):
                self.assertTrue(int(_filter) >= int(currentText))
               if(i == 6):
                self.assertTrue(int(_filter) > int(currentText))
           time.sleep(1)
          
           self.myPyDriver.find_element_by_xpath(filterXpath).click()
           time.sleep(1)
           self.wait.until(EC.element_to_be_clickable((By.XPATH,self.filterClearButtonXPath))).click()


