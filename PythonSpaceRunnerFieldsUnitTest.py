import unittest, config, Selectors, Norm_Filter, Int_Filter, Date_Filter
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
import PyAutoGuiExporter

class PythonSpaceRunnerFieldsUnitTest(unittest.TestCase):
    def __init__(self, methodName = 'runTest'):

        #init config and Selector objects
        config_object = config.config()
        selector_object = Selectors.Selectors()

        #system info
        self.system_info = config_object.system_info
        self.downloads_path = config_object.downloads_path
        
        #Screenshot dir
        self.imageDir = config_object.imageDir

        #Login information
        self.url          = config_object.url
        self.adminUserName = config_object.adminUserName
        self.adminPassword = config_object.adminPassword

        #Application Buttons and links
        self.excelButtonClassName  = selector_object.excelButtonClassName
        self.eventsButtonClassName = selector_object.className_IconEvents
        self.catalogLinkClass      = selector_object.className_IconCatalog
        self.logoutLinkXPath       = selector_object.logoutLinkXPath
        self.iconXyiconClassName   = selector_object.className_IconXyicons
        self.editButton            = selector_object.editButtonXpath
        self.deleteButton          = selector_object.deleteButtonXPath #'//button[contains(text(),"Delete")]'
        self.okButton              = selector_object.okButtonXpath #'//div[2]/ui-button-submit/button'
        self.spaceXpath            = selector_object.spaceXPath
        self.xyiconQuickEditXPath  = selector_object.xyiconQuickEditXPath
        self.xyiconGridRow         = selector_object.xyiconGridRow
        self.name_userName         = selector_object.name_userName
        self.name_pwInput          = selector_object.name_pwInput
        self.name_submit           = selector_object.name_submit
        self.doneButton            = selector_object.doneButton
        self.className_IconHome    = selector_object.className_IconHome
        self.className_IconSpaces  = selector_object.className_IconSpaces
        self.galleryTileXpath      = selector_object.galleryTileXpath
        self.catalogItemXpath      = selector_object.catalogItemXpath
        self.id_floorplan          = selector_object.id_floorplan
        self.name_submitButton     = selector_object.name_submitButton
        self.xyiconSubmitXpath     = selector_object.xyiconSubmitXpath
        self.deleteButtonXPath     = selector_object.deleteButtonXPath
        self.editDeleteButtonXPath = selector_object.editDeleteButtonXPath
        self.okButtonXpath         = selector_object.okButtonXpath
        self.xyiconGridRowXpath    = selector_object.xyiconGridRowXpath
        self.sortMenuButtonsXpath  = selector_object.sortMenuButtonsXpath
        self.xyiconModelFilterXpath        = selector_object.xyiconModelFilterXpath
        self.xyiconFilterButtonXpath       = selector_object.xyiconFilterButtonXpath
        self.xyiconModelFilterCloseXpath   = selector_object.xyiconModelFilterCloseXpath
        self.listItemModelXpath            = selector_object.listItemModelXpath
        self.a_contains_Model_Xpath        = selector_object.a_contains_Model_Xpath
        self.manageColumnsButtonXpath      = selector_object.manageColumnsButtonXpath
        self.columnManager_available       = selector_object.columnManager_available
        self.columnManager_available_model = selector_object.columnManager_available_model
        self.columnManager_selected        = selector_object.columnManager_selected
        self.columnManager_selected_model  = selector_object.columnManager_selected_model
        self.css_headerButton              = selector_object.css_headerButton
        self.xyiconGridHeaderXpath         = selector_object.xyiconGridHeaderXpath
        self.xyiconDepartmentHeader        = selector_object.xyiconDepartmentHeader
        self.xyiconSpaceHeader             = selector_object.xyiconSpaceHeader
        self.exportButtonXpath             = selector_object.exportButtonXpath
        self.xyiconEditDeleteXpath         = selector_object.xyiconEditDeleteXpath
        self.specialCaseOkButton           = selector_object.specialCaseOkButton
        self.className_IconProject          = selector_object.className_IconProject
        self.mainProjectTitle               = config_object.mainProjectTitle
        self.mainSpaceTitle                 = config_object.mainSpaceTitle
        self.projectTileXPath               = selector_object.projectTileXPath
        self.xyiconIDFilterButton           = "//th[@data-title='Xyicon ID']/a/span"
        #Xyicon Editor field selectors
        self.className_xyiconForms = selector_object.className_xyiconForms
        self.editorDepartmentId    = selector_object.editorDepartmentId
        self.editorRoomId          = selector_object.editorRoomId
        self.editorNotesId         = selector_object.editorNotesId
        self.editorXyiconNameId    = selector_object.editorXyiconNameId
        self.editorAssetTagId      = selector_object.editorAssetTagId
        self.editorSerialNumberId  = selector_object.editorSerialNumberId
        self.editorOwnerId         = selector_object.editorOwnerId
        self.editorContactId       = selector_object.editorContactId
        self.editorPlacementId     = selector_object.editorPlacementId
        self.editorInServiceDateId = selector_object.editorInServiceDateId
        self.xyiconForms           = selector_object.xyiconForms       
        self.xyiconFormInput       = selector_object.xyiconFormInput
        self.xyiconFormNotes       = selector_object.xyiconFormNotes
        self.inServiceDatePicker    = selector_object.inServiceDatePicker
        self.className_IconXyicons  = selector_object.className_IconXyicons
        self.span_contains_start    = selector_object.span_contains_start
        self.contains_end           = selector_object.contains_end 
        self.editDateButtonXPath    = selector_object.editDateButtonXPath
        
        self.spaceDeleteButtonXPath = selector_object.spaceDeleteButtonXPath
        self.deleteRightClickXPath  = selector_object.deleteRightClickXPath
        self.selectDateXPath        = selector_object.selectDateXPath
        self.notesFieldXPath        = selector_object.notesFieldXPath
        self.datePickerXPath        = selector_object.datePickerXPath
        self.xyiconSpaceEditSaveXPath = selector_object.xyiconSpaceEditSaveXPath
        self.filterTextBarXPath     = selector_object.filterTextBarXPath
        self.td_span_contains_start = selector_object.td_span_contains_start
        self.tr_contains_start      = selector_object.tr_contains_start
        self.contains_end           = selector_object.contains_end
        self.columnManagerButtonXPath      = selector_object.columnManagerButtonXPath 
        self.catalogFilterMenuXPath        = selector_object.catalogFilterMenuXPath
        self.filterClearButtonXPath        = selector_object.filterClearButtonXPath
        self.filterTextBar1XPath           = selector_object.filterTextBar1XPath
        self.cancelButtonXpath             = selector_object.cancelButtonXpath
        self.className_IconCatalog         = selector_object.className_IconCatalog
        self.className_IconFields          = selector_object.className_IconFields
        self.filterProjectXPath            = selector_object.filterProjectXPath
        self.className_IconFields          = selector_object.className_IconFields
        
        self.chromDriverEXE = os.path.dirname(os.path.realpath(__file__)) + "\\webDriver\\chromedriver.exe"
        self.myPyDriver = webdriver.Chrome(self.chromDriverEXE)
        self.myPyDriver.maximize_window()
        #wait setup
        self.wait = WebDriverWait(self.myPyDriver, 15)
        
        #init Action chains
        self.action = action_chains.ActionChains(self.myPyDriver)
        
        #init time stamp 
        self.now = datetime.datetime.now()
        self.date = self.now.strftime('%H%M%S_%m%d%y')

        if self.myPyDriver:
            try:
                self.myPyDriver.get(self.url)
                self.assertTrue( self.myPyDriver.title == "SpaceRunner" )
                self.wait.until(EC.presence_of_element_located((By.NAME,self.name_userName)))
                self.userNameField = self.myPyDriver.find_element_by_name(self.name_userName)
                self.userNameField.send_keys(self.adminUserName)
                self.userPassword = self.myPyDriver.find_element_by_name(self.name_pwInput)
                self.userPassword.send_keys(self.adminPassword)
                self.loginSubmitButton = self.myPyDriver.find_element_by_name(self.name_submitButton)
                self.loginSubmitButton.click()
                self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconProject)))
                self.selectProjectModule = self.myPyDriver.find_element_by_class_name(self.className_IconProject)
                self.selectProjectModule.click()
                self.wait.until(EC.element_to_be_clickable((By.XPATH,self.projectTileXPath))).click()
                time.sleep(3)
                self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconFields))).click()
                time.sleep(1)
            except:
                self.myPyDriver.quit()
                self.fail()
            return super(PythonSpaceRunnerFieldsUnitTest, self).__init__(methodName)
        else:
            print("Unable to init webDriver!")


    #Can be called in order to switch to a project with designated amounts of xyicons, for quicker testing
    def goToFilterProject(self):
        time.sleep(2)
        self.selectProjectModule = self.myPyDriver.find_element_by_class_name(self.className_IconProject)
        self.selectProjectModule.click()
        time.sleep(2)
        project = self.myPyDriver.find_element_by_xpath('//h5[contains(text(),"Filter Tests")]')
        project.click()
        time.sleep(3)
        return

    def highlightElement(self,element):
        self.myPyDriver.execute_script("arguments[0].setAttribute('style', arguments[1]);",element, "color: red; border: 3px solid red;")
    
    def random_string(self):
        range = random.randint(6,12)
        randomString = ''.join([random.choice(string.ascii_letters +string.digits) for n in xrange(range)])
        return randomString
            
    def send_random(self, elementId):
        #element = self.myPyDriver.find_element_by_id(elementId)
        element = elementId
        element.clear()
        randomString = self.random_string()
        element.send_keys(randomString)
        return randomString
     
    def waitForDataLoad(self):
        self.wait = WebDriverWait(self.myPyDriver, 30)
        self.wait.until(EC.invisibility_of_element_located((By.XPATH,'//div[contains(text(),"Your project data is being loaded...")]')))
        time.sleep(1)
        self.wait = WebDriverWait(self.myPyDriver, 15)
        return



    #TODO :  
    #Average time:  (dependant on which columns are present)
    #Precondition: 
    #notes: glitch with textbar is workaround by refreshing webpage after every column (last lines of test)
    #Status: 
    def test_filterByColumn(self,methodName= 'test_filterByColumn'):
       # self.goToFilterProject()
        time.sleep(2)     
        self.waitForDataLoad() #Solves current project data loading issue which crashes all tests, adds ~~15 seconds

       #Use manage column to list columns to be checked
        #self.wait.until(EC.presence_of_element_located((By.XPATH,self.columnManagerButtonXPath))).click()
        self.myPyDriver.find_element_by_xpath("//div[@id='contentWrapper']/div/div/div/div/div/div/div/div/div/div/div/span/button").click()
        time.sleep(2)
        selectedColumn = self.myPyDriver.find_element_by_xpath("//div[2]/div/div[2]/ul")
        columnElements = selectedColumn.find_elements_by_tag_name('li')
        time.sleep(2)
        self.columnLists = []
        self.columnManager_available_model=[]
        count = 1
        for opt in columnElements:          
            self.columnLists.append(count)
            count = count + 1
        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.cancelButtonXpath)))
        self.cancelButton=self.myPyDriver.find_element_by_xpath(self.cancelButtonXpath)
        self.cancelButton.click()
        
        _normalFilter = "e"               
        
        for col in range(0,len(self.columnLists)):
            filterXpath = "//th["+str(self.columnLists[col])+"]/a/span"
            filterTextXpath = "//th["+str(self.columnLists[col])+"]/a[2]"
            filterText = self.myPyDriver.find_element_by_xpath(filterTextXpath).text
            Norm_Filter.Norm_Filter(_normalFilter, self.columnLists[col], "fields", self.myPyDriver, self.wait)
           
            if (col != len(self.columnLists)):
               self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.className_IconCatalog))).click()
               self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
               self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,'td')))
        return super(PythonSpaceRunnerFieldsUnitTest, self).__init__(methodName)










    def tearDown(self):
        #self.signOutLink = self.myPyDriver.find_element_by_xpath(self.logoutLinkXPath)
        #self.signOutLink.click()
        self.myPyDriver.quit()
        return super(PythonSpaceRunnerFieldsUnitTest, self).tearDown()

if __name__ == '__main__':
    unittest.main()
