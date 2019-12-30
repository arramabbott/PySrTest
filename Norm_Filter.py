import time
import unittest
import sys
import os, config, Selectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Norm_Filter(unittest.TestCase):
    
    def __init__(self, filterWord, column, methodType, myPyDriver, wait):        
        self.myPyDriver = myPyDriver
        self.wait = wait
        selector_object = Selectors.Selectors()
        self.catalogFilterMenuXPath        = selector_object.catalogFilterMenuXPath
        self.filterClearButtonXPath        = selector_object.filterClearButtonXPath
        self.filterTextBar1XPath           = selector_object.filterTextBar1XPath
        self.catalogFilterButton           = selector_object.catalogFilterButton
        self.xyiconGridRow                 = selector_object.xyiconGridRow
        

        k = 22 + int(column)*2
        _filter = filterWord
        if(methodType == "User" or methodType == "fields"):
           filterXpath = "//th["+str(column)+"]/span/span/span/span/span/span"
        else:
           filterXpath = "//th["+str(column)+"]/a/span"

        for i in range(1,7):         
           if(methodType == "User" or methodType == "fields"):
            self.currentFilterXpath = "//div["+str(k)+"]/div/ul/li"+"["+str(i)+"]"
            #listIndex = i-1    
            time.sleep(1)
            filterButton = self.myPyDriver.find_element_by_xpath(filterXpath)
            filterButton.click()
            time.sleep(1)
            #self.plz = self.myPyDriver.find_elements_by_xpath("//div["+str(k)+"]/div/ul/li")
            self.currentFilter = self.myPyDriver.find_element_by_xpath(self.currentFilterXpath) #self.catalogFilterMenuXPath+"["+str(i)+"]")
            self.currentFilter.click()
            
            #self.plz[listIndex].click()
            time.sleep(1)
            #textbar = self.myPyDriver.find_element_by_xpath("//th"+str(column)+"/span/span/span/input")
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH,self.filterTextBar1XPath))) 
            self.textBar = self.myPyDriver.find_element_by_xpath(self.filterTextBar1XPath)
            self.textBar.click()
            time.sleep(1)
            self.textBar.send_keys(_filter)            
            self.textBar.send_keys(Keys.ENTER)
            table = self.myPyDriver.find_elements_by_xpath(self.xyiconGridRow)           
           
            for tr in table:
               tds = tr.find_elements_by_tag_name('td')
               currentText = str(tds[(column-1)].text).lower()
               if(i == 1):
                  self.assertTrue(_filter == currentText)
               if(i == 2):
                  self.assertTrue(_filter != currentText)
               if(i == 3):               
                  var = currentText.startswith(_filter)
                  self.assertTrue(currentText.startswith(_filter))  
               if(i == 4):
                  self.assertTrue(_filter in currentText)
               if(i == 5):
                  self.assertTrue(_filter not in currentText)
               if(i == 6):
                  self.assertTrue(currentText.endswith(_filter))
            clearButton = self.myPyDriver.find_element_by_xpath("//th["+str(column)+"]/span/span/button")                              
            clearButton.click()                



           else:    
            time.sleep(1)
            filterButton = self.myPyDriver.find_element_by_xpath(filterXpath)
            filterButton.click()
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH,self.filterTextBar1XPath))) 
            time.sleep(2)   
            if(i != 1):
             filterButton = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.catalogFilterButton)))
             filterButton.click()
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
            time.sleep(1)
            table = self.myPyDriver.find_elements_by_xpath(self.xyiconGridRow)
            for tr in table:
                tds = tr.find_elements_by_tag_name('td')
                currentText = str(tds[(column-1)].text).lower()
                if(i == 1):
                 self.assertTrue(_filter in currentText)
                if(i == 2):
                 self.assertTrue(_filter not in currentText)
                if(i == 3):
                 self.assertTrue(_filter == currentText)
                if(i == 4):
                 self.assertTrue(_filter != currentText)
                if(i == 5):               
                 var = currentText.startswith(_filter)
                 self.assertTrue(currentText.startswith(_filter))                       
                if(i == 6):
                 self.assertTrue(currentText.endswith(_filter))
            time.sleep(1)
            self.myPyDriver.find_element_by_xpath(filterXpath).click()
            time.sleep(1)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,self.filterClearButtonXPath))).click()
           
  