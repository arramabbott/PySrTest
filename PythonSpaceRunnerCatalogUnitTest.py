import unittest
import string
import sys
import random
import datetime
import time
import os, config, Selectors, Norm_Filter
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import PyAutoGuiExporter

class PythonSpaceRunnerCatalogUnitTest(unittest.TestCase):
    #Class for all the Catalog Unit tests for 
    #SpaceRunner
    def __init__(self, methodName = 'runTest'):
        #init configuration object
        config_object   = config.config()
        
        #system info
        self.system_info = config_object.system_info
        self.downloads_path = config_object.downloads_path

        #Login information
        self.adminUserName   = config_object.adminUserName
        self.adminPassword   = config_object.adminPassword
        self.url             = config_object.url

        #init selector object
        selector_object = Selectors.Selectors()
        
        #Application Buttons and links
        self.excelButtonClassName          = selector_object.excelButtonClassName
        self.catalogLinkCSSSelector        = selector_object.catalogLinkCSSSelector
        self.catalogGridLinkClass          = selector_object.catalogGridLinkClass
        self.catalogGridRowXPath           = selector_object.catalogGridRowXPath
        self.logoutLinkXPath               = selector_object.logoutLinkXPath
        self.projectsLinkClassName         = selector_object.projectsLinkClassName
        self.projectTileXPath              = selector_object.projectTileXPath
        self.createButtonCSSSelector       = selector_object.createButtonCSSSelector
        self.electricalSelectXpath         = selector_object.electricalSelectXpath
        self.iconSearchXPath               = selector_object.iconSearchXPath
        self.svgIconCSSSelector            = selector_object.svgIconCSSSelector
        self.IconColorXPath                = selector_object.IconColorXPath
        self.doneButton                    = selector_object.doneButton
        self.spaceXPath                    = selector_object.spaceXPath
        self.name_submitButton             = selector_object.name_submitButton
        self.name_userName                 = selector_object.name_userName
        self.name_make                     = selector_object.name_make
        self.name_pwInput                  = selector_object.name_pwInput
        self.name_submit                   = selector_object.name_submit
        self.className_IconProject         = selector_object.className_IconProject
        self.catalogHeaderXPath            = selector_object.catalogHeaderXPath
        self.name_model                    = selector_object.name_model
        self.name_description              = selector_object.name_description
        self.name_iconText                 = selector_object.name_iconText
        self.td_span_xpath                 = selector_object.td_span_xpath
        self.td_span_contains_start        = selector_object.td_span_contains_start
        self.span_contains_start           = selector_object.span_contains_start
        self.contains_end                  = selector_object.contains_end
        self.class_lightingXPath           = selector_object.class_lightingXPath
        self.editButtonXpath               = selector_object.editButtonXpath
        self.ui_saveButtonXpath            = selector_object.ui_saveButtonXpath
        self.catalogItem12057_Xpath        = selector_object.catalogItem12057_Xpath
        self.css_editCatalogTitle          = selector_object.css_editCatalogTitle
        self.css_deleteButton              = selector_object.css_deleteButton
        self.css_okButton                  = selector_object.css_okButton
        self.css_headerButton              = selector_object.css_headerButton
        self.newCatalogItemXpath           = selector_object.newCatalogItemXpath
        self.cancelButtonXpath             = selector_object.cancelButtonXpath
        self.catalogCloneButtonXpath       = selector_object.catalogCloneButtonXpath
        self.catalogGridBodyXpath          = selector_object.catalogGridBodyXpath
        self.catalog_exportButtonXpath     = selector_object.catalog_exportButtonXpath
        self.catalogGridTableHeaderXpath   = selector_object.catalogGridTableHeaderXpath
        self.catalogGridTableRowXpath      = selector_object.catalogGridTableRowXpath
        self.a_contains_Class_Xpath        = selector_object.a_contains_Class_Xpath
        self.a_contains_Model_Xpath        = selector_object.a_contains_Model_Xpath
        self.listItemModelXpath            = selector_object.listItemModelXpath
        self.columnManager_available       = selector_object.columnManager_available
        self.columnManager_selected        = selector_object.columnManager_selected
        self.manageColumnsButtonXpath      = selector_object.manageColumnsButtonXpath
        self.columnManager_available_model = selector_object.columnManager_available_model
        self.columnManager_selected_model  = selector_object.columnManager_selected_model
        self.saveButtonXpath               = selector_object.saveButtonXpath
        self.downloadsPath                 = selector_object.downloadsPath
        self.exportAutoItPath              = selector_object.exportAutoItPath
        self.sortMenuButtonsXpath          = selector_object.sortMenuButtonsXpath
        self.catalogFilterModelXpath       = selector_object.catalogFilterModelXpath
        self.catalogModelFilterCloseXpath  = selector_object.catalogModelFilterCloseXpath
        self.catalogFilterButton           = selector_object.catalogFilterButton
        self.catEditSaveID                 = selector_object.catEditSaveID
        self.walkMeCloseButtonXPath        = selector_object.walkMeCloseButtonXPath  
        self.catalogAddClassXPATH          = selector_object.catalogAddClassXPATH
        self.className_IconCatalog         = selector_object.className_IconCatalog
        self.iconXyiconClassName           = selector_object.className_IconXyicons
        self.modelFilterFieldXPath         = selector_object.modelFilterFieldXPath
        self.filterSubmitButtonXPath       = selector_object.filterSubmitButtonXPath
        self.xyiconGridRow                 = selector_object.xyiconGridRow
        self.gridFirstRow                  = selector_object.gridFirstRow 
        self.columnManagerButtonXPath      = selector_object.columnManagerButtonXPath 
        self.catalogFilterMenuXPath        = selector_object.catalogFilterMenuXPath
        self.filterClearButtonXPath        = selector_object.filterClearButtonXPath
        self.filterTextBar1XPath           = selector_object.filterTextBar1XPath
        self.fourPorts                     = selector_object.fourPorts
        self.fourPortsOutcome              = selector_object.fourPortsOutcome

        
        self.chromDriverEXE = os.path.dirname(os.path.realpath(__file__)) + "\\webDriver\\chromedriver.exe"
        self.myPyDriver = webdriver.Chrome(self.chromDriverEXE)
        self.myPyDriver.maximize_window()

        #wait setup
        self.wait = WebDriverWait(self.myPyDriver, 15)
        self.myPyDriver.set_page_load_timeout(15)
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
                time.sleep(1)
                self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconCatalog)))
                self.selectCatalogModule = self.myPyDriver.find_element_by_class_name(self.className_IconCatalog)
                self.selectCatalogModule.click()
                time.sleep(4)
                self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//td')))
            except:
                self.myPyDriver.quit()
                self.fail()
            return super(PythonSpaceRunnerCatalogUnitTest, self).__init__(methodName)
        else:
            print("Unable to init webDriver!")
  
    

    def random_string(self):
        range = random.randint(10,20)
        randomString = ''.join([random.choice(string.ascii_letters +string.digits) for n in xrange(range)])
        return randomString
    
    def waitForDataLoad(self):
        self.wait = WebDriverWait(self.myPyDriver, 30)
        self.wait.until(EC.invisibility_of_element_located((By.XPATH,'//div[contains(text(),"Your project data is being loaded...")]')))
        time.sleep(1)
        self.wait = WebDriverWait(self.myPyDriver, 15)
        return
       
    def highlightElement(self,element):
        self.myPyDriver.execute_script("arguments[0].setAttribute('style', arguments[1]);",element, "color: red; border: 3px solid red;")     


    #TODO : 
    #Average time: 35 seconds 
    #Precondition: 
    #Status: ✔ 
    def test_AddCatalogItem(self, methodName = "test_AddCatalogItem"):
        # unusual failure with following string, thinks an item with same make/model already exists

        #_text = """Panelboard Interior, Main Lug, Convertible, Amps 400, Number of Spaces 42,  
        #         Voltage 480Y/277VAC, Phase 3, Bus Material Aluminum, Recommended Enclosure 22P067 for Main Lug,  
        #         22P068 for Main Breaker, Recommended Flush Cover 3TX91 for Main Lug, 3TX96 for Main Breaker,  
        #         Recommended Surface Cover 3TX92 for Main Lug, 3TX97 for Main Breaker, Main Circuit Breaker Adapter Kit 22P071,  
        #         Circuit Breaker Type EDB/EGB/EJB, Height 56 In., Width 10-1/2 In., Depth 5-3/4 In.,  
        #         Recommended Ground Bar Kit G1971907"""

        _text = self.random_string()
        _model = 'New - ' + self.random_string()
        #click add button in catalog
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//td')))
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,self.createButtonCSSSelector)))
        _addButton =  self.myPyDriver.find_element_by_css_selector(self.createButtonCSSSelector)
        _addButton.click()
        time.sleep(2)
        #Add and store fields to new catalog item
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.catalogAddClassXPATH)))
        _selectClassDropDown = self.myPyDriver.find_element_by_xpath(self.catalogAddClassXPATH)       
        time.sleep(1)
        _selectClassDropDown.click()
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.electricalSelectXpath)))
        time.sleep(1)
        self.myPyDriver.find_element_by_xpath(self.electricalSelectXpath).click()
        _xyiconMakeField = self.myPyDriver.find_element_by_name(self.name_make)
        _xyiconModelField = self.myPyDriver.find_element_by_name(self.name_model)
        _xyiconDescriptionField = self.myPyDriver.find_element_by_name(self.name_description)
        _xyiconIconText = self.myPyDriver.find_element_by_name(self.name_iconText)
        _xyiconPorts = self.myPyDriver.find_element_by_name('defaultDeviceLinks')

        _xyiconMakeField.send_keys("Panelboard Interior")
        _xyiconModelField.send_keys(_model)
        _xyiconDescriptionField.send_keys(_text)
        _xyiconIconText.send_keys("NF442L4")
        _xyiconPorts.clear()
        _xyiconPorts.send_keys(self.fourPorts)
        _iconSearch = self.myPyDriver.find_element_by_xpath(self.iconSearchXPath)
        _iconSearch.send_keys("Electrical")
        _iconIconSelect = self.myPyDriver.find_element_by_css_selector(self.svgIconCSSSelector)
        _iconIconSelect.click()
        _iconColor = self.myPyDriver.find_element_by_xpath(self.IconColorXPath)
        _iconColor.click()
        _xyiconMakeFieldValue = _xyiconMakeField.get_attribute('value')
        _xyiconModelFieldValue = _xyiconModelField.get_attribute('value')
        _xyiconDescriptionFieldValue = _xyiconDescriptionField.get_attribute('value')
        _xyiconIconTextValue = _xyiconIconText.get_attribute('value') 
        _submitButton = self.myPyDriver.find_element_by_name(self.name_submitButton)
        _submitButton.click()
        time.sleep(3)
        #Find the created catalog item using the filter
        modelFilterXPath = self.td_span_contains_start+_model+self.contains_end
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,modelFilterXPath)))         
        self.myPyDriver.find_element_by_xpath(self.modelFilterFieldXPath).click()
        self.textBar = self.myPyDriver.find_element_by_xpath(self.filterTextBar1XPath)
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,self.filterTextBar1XPath))) 
        time.sleep(2)
        self.textBar.click()
        self.textBar.send_keys(_model)
        self.submitButton = self.myPyDriver.find_element_by_xpath(self.filterSubmitButtonXPath)

        self.submitButton.click()

        #select the created catalog item and compare values to make sure it was created correctly
        _savedXyiconGridRow = self.myPyDriver.find_elements_by_xpath('//tr')
        #two \\tr's should be the one created catalog item and the title bar ("class//make//model" etc)
        self.assertTrue(len(_savedXyiconGridRow)==2)
        self.action.double_click(_savedXyiconGridRow[1]).perform()
        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.NAME,self.name_make)))
        _xyiconMakeFieldSaved = self.myPyDriver.find_element_by_name(self.name_make)
        _xyiconModelFieldSaved  = self.myPyDriver.find_element_by_name(self.name_model)
        _xyiconDescriptionFieldSaved  = self.myPyDriver.find_element_by_name(self.name_description)
        _xyiconIconTextSaved  = self.myPyDriver.find_element_by_name(self.name_iconText)
        _xyiconPorts = self.myPyDriver.find_element_by_name('defaultDeviceLinks')

        _xyiconMakeFieldSavedValue = _xyiconMakeFieldSaved.get_attribute('value')
        _xyiconModelFieldSavedValue = _xyiconModelFieldSaved.get_attribute('value')
        _xyiconDescriptionFieldSavedValue = _xyiconDescriptionFieldSaved.get_attribute('value')
        _xyiconIconTextSavedValue = _xyiconIconTextSaved.get_attribute('value')
        _xyiconPortsSavedValue = _xyiconPorts.get_attribute('value')

        self.assertTrue(_xyiconMakeFieldSavedValue == _xyiconMakeFieldValue)
        self.assertTrue(_xyiconModelFieldSavedValue == _xyiconModelFieldValue)
        self.assertTrue(_xyiconDescriptionFieldSavedValue == _xyiconDescriptionFieldValue)
        self.assertTrue(_xyiconIconTextSavedValue == _xyiconIconTextValue)
        self.assertTrue(_xyiconPortsSavedValue == self.fourPortsOutcome)
        return super(PythonSpaceRunnerCatalogUnitTest, self).__init__(methodName)

    #TODO : 
    #Average time: 42 seconds 
    #Precondition: Exists a catalog item "New - *"
    #Status: ✔ 
    def test_EditCatalogItem(self, methodName = "test_EditCatalogItem"):
  
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//td')))
        try:
            self.myPyDriver.find_element_by_xpath(self.modelFilterFieldXPath).click()
            time.sleep(1)
            self.textBar = self.myPyDriver.find_element_by_xpath(self.filterTextBar1XPath)
           # self.wait.until(EC.presence_of_all_elements_located(("//input[@type='text'][1]"))) 
            time.sleep(2)
            self.textBar.click()
            self.textBar.send_keys("New")
            time.sleep(1)
            self.submitButton = self.myPyDriver.find_element_by_xpath(self.filterSubmitButtonXPath)
            self.submitButton.click()
            time.sleep(1)
            _catalogGridRow = self.myPyDriver.find_element_by_xpath(self.newCatalogItemXpath)
            _catalogGridRow.click()
        except Exception as e:
            raise e
            self.myPyDriver.quit()
        time.sleep(2)
        #select edit button
        _catalogEditButton = self.myPyDriver.find_element_by_xpath(self.editButtonXpath)
        _catalogEditButton.click()
        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,self.css_editCatalogTitle)))
        #get current values edit all values
        _xyiconMakeField = self.myPyDriver.find_element_by_name(self.name_make)
        _xyiconMakeField.clear()
        _xyiconMakeField.send_keys(self.random_string())
        _xyiconModelField = self.myPyDriver.find_element_by_name(self.name_model)
        _model = 'Edit - ' + self.random_string()
        _xyiconModelField.clear()
        _xyiconModelField.send_keys(_model)
        _xyiconDescriptionField = self.myPyDriver.find_element_by_name(self.name_description)
        _xyiconDescriptionField.clear()
        _xyiconDescriptionField.send_keys(self.random_string())
        _xyiconIconText = self.myPyDriver.find_element_by_name(self.name_iconText)
        _xyiconIconText.clear()
        _xyiconIconText.send_keys(self.random_string())
        _iconSearch = self.myPyDriver.find_element_by_xpath(self.iconSearchXPath)
        _iconSearch.send_keys("Lighting")
        _iconIconSelect = self.myPyDriver.find_element_by_css_selector(self.svgIconCSSSelector)
        _iconIconSelect.click()
        _iconColor = self.myPyDriver.find_element_by_xpath(self.IconColorXPath)
        _iconColor.click()

        _xyiconMakeField = self.myPyDriver.find_element_by_name(self.name_make)
        _xyiconModelField  = self.myPyDriver.find_element_by_name(self.name_model)
        _xyiconDescriptionField  = self.myPyDriver.find_element_by_name(self.name_description)
        _xyiconIconText  = self.myPyDriver.find_element_by_name(self.name_iconText)

        _xyiconMakeFieldValue = _xyiconMakeField.get_attribute('value')
        _xyiconModelFieldValue = _xyiconModelField.get_attribute('value')
        _xyiconDescriptionFieldValue = _xyiconDescriptionField.get_attribute('value')
        _xyiconIconTextValue = _xyiconIconText.get_attribute('value')

        #save Catalog item
        _submitButtonParent = self.myPyDriver.find_element_by_id(self.catEditSaveID)
        _submitButton       = _submitButtonParent.find_element_by_xpath('.//button')
        _submitButton.click()
        time.sleep(3)
        
        #Clear filter
        self.myPyDriver.find_element_by_xpath(self.modelFilterFieldXPath).click()
        time.sleep(1)
        self.textBar = self.myPyDriver.find_element_by_xpath(self.filterTextBar1XPath)
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,self.filterTextBar1XPath))) 
        time.sleep(2)
        self.textBar.click()
        self.textBar.clear()
        time.sleep(1)

        #filter for edit      
        self.textBar.send_keys(_model)
        time.sleep(1)
        self.submitButton = self.myPyDriver.find_element_by_xpath(self.filterSubmitButtonXPath)
        self.submitButton.click()
        time.sleep(1)

        _savedXyiconGridRow = self.myPyDriver.find_elements_by_xpath('//tr')
        #two \\tr's should be the one created catalog item and the title bar ("class//make//model" etc)
        self.assertTrue(len(_savedXyiconGridRow)==2)
        
        #reopen Item
        _catalogEditButton = self.myPyDriver.find_element_by_xpath(self.editButtonXpath)
        _catalogEditButton.click()

        #verify changes
        self.wait.until(EC.presence_of_element_located((By.NAME,self.name_make)))
        _xyiconMakeFieldSaved = self.myPyDriver.find_element_by_name(self.name_make)
        _xyiconModelFieldSaved  = self.myPyDriver.find_element_by_name(self.name_model)
        _xyiconDescriptionFieldSaved  = self.myPyDriver.find_element_by_name(self.name_description)
        _xyiconIconTextSaved  = self.myPyDriver.find_element_by_name(self.name_iconText)

        _xyiconMakeFieldSavedValue = _xyiconMakeFieldSaved.get_attribute('value')
        _xyiconModelFieldSavedValue = _xyiconModelFieldSaved.get_attribute('value')
        _xyiconDescriptionFieldSavedValue = _xyiconDescriptionFieldSaved.get_attribute('value')
        _xyiconIconTextSavedValue = _xyiconIconTextSaved.get_attribute('value')

        self.assertTrue(_xyiconMakeFieldSavedValue == _xyiconMakeFieldValue)
        self.assertTrue(_xyiconModelFieldSavedValue == _xyiconModelFieldValue)
        self.assertTrue(_xyiconDescriptionFieldSavedValue == _xyiconDescriptionFieldValue)
        self.assertTrue(_xyiconIconTextSavedValue == _xyiconIconTextValue)
        return super(PythonSpaceRunnerCatalogUnitTest, self).__init__(methodName)

    #TODO : 
    #Average time: 28 seconds
    #Precondition: exists a catalog item with the model "Edit - *"
    #Status: ✔ 
    def test_DeleteCatalogItem(self, methodName = "test_DeleteCatalogItem"):
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.td_span_xpath)))
        self.assertTrue(self.myPyDriver.find_element_by_xpath(self.td_span_contains_start+'Edit -'+self.contains_end))
        _savedXyiconGridRow = self.myPyDriver.find_element_by_xpath(self.td_span_contains_start+'Edit -'+self.contains_end)
        _savedXyiconModel = _savedXyiconGridRow.text
        time.sleep(1)
        _savedXyiconGridRow.click()
        _deleteCSSSeletor = self.css_deleteButton
        _deleteButton = self.myPyDriver.find_element_by_css_selector(_deleteCSSSeletor)
        _deleteButton.click()
        time.sleep(3)
        _okButtonCSSSeletor = self.css_okButton
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,_okButtonCSSSeletor)))
        _okButton = self.myPyDriver.find_element_by_css_selector(_okButtonCSSSeletor)
        _okButton.click()
        time.sleep(5)
        self.assertTrue(len(self.myPyDriver.find_elements_by_xpath(self.td_span_contains_start+_savedXyiconModel+self.contains_end)) == 0)
        return super(PythonSpaceRunnerCatalogUnitTest, self).__init__(methodName)

    #TODO : 
    #Average time: 33 seconds
    #Precondition: exists a cloneable catalog item 
    #Status: ✔ 
    def test_CloneCatalogItem(self, methodName = "test_CloneCatalogItem"):
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,'td')))
        #select record
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.newCatalogItemXpath)))
        time.sleep(1)
        _catalogGridRow = self.myPyDriver.find_element_by_xpath(self.newCatalogItemXpath)
        _catalogGridRow.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editButtonXpath))).click()
        self.wait.until(EC.presence_of_element_located((By.NAME,self.name_make)))
        _xyiconParentMake = self.myPyDriver.find_element_by_name(self.name_make).get_attribute('value')
        _xyiconParentModel  = self.myPyDriver.find_element_by_name(self.name_model).get_attribute('value')
        _xyiconParentDescription  = self.myPyDriver.find_element_by_name(self.name_description).get_attribute('value')
        _xyiconParentIcon  = self.myPyDriver.find_element_by_name(self.name_iconText).get_attribute('value')
        time.sleep(1)
        self.myPyDriver.find_element_by_xpath(self.cancelButtonXpath).click()
        #select clone xyicon button
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.catalogCloneButtonXpath))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.catalogAddClassXPATH)))
        time.sleep(1)
        _selectClassDropDown = self.myPyDriver.find_element_by_xpath(self.catalogAddClassXPATH)       
        time.sleep(1)
        _selectClassDropDown.click()
        #css selector has been changed to xpath see add function
        time.sleep(1)
        electricalOption = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.electricalSelectXpath)))
        electricalOption.click()
        #verify values carried over from parent Catalog Item
        _make = self.myPyDriver.find_element_by_name(self.name_make).get_attribute('value')
        _model = self.myPyDriver.find_element_by_name(self.name_model).get_attribute('value')
        _description = self.myPyDriver.find_element_by_name(self.name_description).get_attribute('value')
        _iconText = self.myPyDriver.find_element_by_name(self.name_iconText).get_attribute('value')
        self.assertTrue(_xyiconParentMake == _make)
        self.assertTrue(_xyiconParentModel == _model)
        self.assertTrue(_xyiconParentDescription == _description)
        self.assertTrue(_xyiconParentIcon == _iconText)
        #input values in form
        _model = ('(CLONE - ' + self.random_string() + ')')
        _modelField = self.myPyDriver.find_element_by_name(self.name_model)
        _modelField.clear()
        _modelField.send_keys(_model)
        #save form
        self.myPyDriver.find_element_by_xpath(self.saveButtonXpath).click()
        _cloneXPath = self.span_contains_start+str(_model)+self.contains_end
        #self.wait.until(EC.element_to_be_clickable((By.XPATH,_cloneXPath)))
        #reselect row
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.modelFilterFieldXPath))).click()
        self.textBar = self.myPyDriver.find_element_by_xpath(self.filterTextBar1XPath)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.filterTextBar1XPath))) 
        time.sleep(2)
        self.textBar.click()
        self.textBar.send_keys(_model)
        self.submitButton = self.myPyDriver.find_element_by_xpath(self.filterSubmitButtonXPath)
        self.submitButton.click()
        time.sleep(1)
        
        _savedXyiconGridRow = self.myPyDriver.find_elements_by_xpath('//tr')
        #two \\tr's should be the one created catalog item and the title bar ("class//make//model" etc)
        self.assertTrue(len(_savedXyiconGridRow)==2)

        self.myPyDriver.find_element_by_xpath(_cloneXPath).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editButtonXpath))).click()
        #verify clone's values after save
        self.wait.until(EC.presence_of_element_located((By.NAME,self.name_make)))
        _xyiconCloneMake = self.myPyDriver.find_element_by_name(self.name_make).get_attribute('value')
        _xyiconCloneModel  = self.myPyDriver.find_element_by_name(self.name_model).get_attribute('value')
        _xyiconCloneDescription  = self.myPyDriver.find_element_by_name(self.name_description).get_attribute('value')
        _xyiconCloneIcon  = self.myPyDriver.find_element_by_name(self.name_iconText).get_attribute('value')
        self.assertTrue(_xyiconCloneMake == _make)
        self.assertTrue(_xyiconCloneModel == _model)
        self.assertTrue(_xyiconCloneDescription == _description)
        self.assertTrue(_xyiconCloneIcon == _iconText)
        return super(PythonSpaceRunnerCatalogUnitTest, self).__init__(methodName)

    #TODO : 
    #Average time: 16 seconds
    #Precondition: 
    #Status: 
    def test_CatalogExport(self, methodName = "test_CatalogExport"):
        path = self.downloads_path
        init_num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
        #click export button from catalog grid
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.catalog_exportButtonXpath))).click()
        time.sleep(1)
        #######system dialog handler########
        #PyAutoGuiExporter.PyAutoGuiExporter()
        ####################################
        #verify increase in # of files in 'path' by 1
        post_num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
        self.assertTrue((post_num_files - init_num_files) == 1)
        return super(PythonSpaceRunnerCatalogUnitTest, self).__init__(methodName)
    
    #TODO: FIX
    def test_CatalogDragColumns(self, methodName = "test_CatalogDragColumns"):
        _thXPath = self.catalogGridTableHeaderXpath
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.a_contains_Class_Xpath)))
        _classHeader = self.myPyDriver.find_element_by_xpath(self.a_contains_Class_Xpath)
        _modelHeader = self.myPyDriver.find_element_by_xpath(self.a_contains_Model_Xpath)
        _table = self.myPyDriver.find_elements_by_xpath(_thXPath)
        _tableHeaders = []
        for th in _table:
            title = th.get_attribute("data-title")
            _tableHeaders.append(title)
        _cIndex = _tableHeaders.index("Class")
        _mIndex = _tableHeaders.index("Model")
        self.action.drag_and_drop(_modelHeader, _classHeader).perform()
        time.sleep(1)
        _table = self.myPyDriver.find_elements_by_xpath(_thXPath)
        _upTableHeaders = []
        for th in _table:
            title = th.get_attribute("data-title")
            _upTableHeaders.append(title)
        self.assertTrue(_upTableHeaders.index("Model") == 0)
        self.assertTrue(_upTableHeaders.index("Class") == (_cIndex + 1))
        return super(PythonSpaceRunnerCatalogUnitTest, self).__init__(methodName)

    #TODO : 
    #Average time: 47 seconds
    #Precondition: Model is included in selected fields column, fields tab contains fields 
    #Notes: preCondition can be eliminated once drag n drop function is established  
    #Status: ✔     
    def test_CatalogSortByModel(self, methodName = 'test_CatalogSortByModel'):
        _trXPath = self.xyiconGridRow
        _sortTab = self.a_contains_Model_Xpath       
        time.sleep(1)
        _modelTab = self.myPyDriver.find_element_by_xpath(_sortTab)
        _modelTab.click()
        time.sleep(1)
        _table = self.myPyDriver.find_elements_by_xpath(_trXPath)
       
        #ensure that precondition is met and find model index
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.columnManagerButtonXPath))).click()
        time.sleep(2)
        selectedColumn = self.myPyDriver.find_element_by_xpath("//div[2]/div/div[2]/ul")
        columnElements = selectedColumn.find_elements_by_tag_name('li')
        time.sleep(2)
        columnLength = len(columnElements)
        modelIndex = 0
        for _li in columnElements:
            self.assertTrue(modelIndex<=columnLength)
            if _li.text == 'Model':
                break
            else:
                modelIndex = modelIndex + 1        
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.cancelButtonXpath)))
        self.cancelButton=self.myPyDriver.find_element_by_xpath(self.cancelButtonXpath)
        self.cancelButton.click()
        time.sleep(1)
        
        #record models of rows in table
        _modelList = []        
        for _tr in _table:
            _tds= _tr.find_elements_by_tag_name('td')
            _modelList.append(_tds[modelIndex].text)      
        
        #click on model filter
        _modelTab = self.myPyDriver.find_element_by_xpath(_sortTab)
        _modelTab.click()
        time.sleep(1)                
        _updatedModelList = []
        _table = self.myPyDriver.find_elements_by_xpath(_trXPath)        
        
        #Record rows of table after model filter is clicked
        for _tr in _table:
            _tds= _tr.find_elements_by_tag_name('td')
            _updatedModelList.append(_tds[modelIndex].text)
        
        #reverse the anti-alphabetical list to make sure it was sorted exactly backwards    
        _reversedList = []
        for i in range(0,len(_updatedModelList)):
            _reversedList.append(_updatedModelList.pop())  
                   
        self.assertTrue(_reversedList == _modelList)     
        return super(PythonSpaceRunnerCatalogUnitTest, self).__init__(methodName)


    ##TODO :  
    ##Average time:  4 min (dependant on which columns are present)
    ##Precondition: 
    ##notes: glitch with textbar is workaround by refreshing webpage after every column (last lines of test)
    ##Status: 
    def test_filterByColumn(self,methodName= 'test_filterByColumn'):
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,'td')))
        
        #ensure that precondition is met and find model index
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.columnManagerButtonXPath))).click()
        time.sleep(2)
        selectedColumn = self.myPyDriver.find_element_by_xpath("//div[2]/div/div[2]/ul")
        columnElements = selectedColumn.find_elements_by_tag_name('li')
        time.sleep(2)
        self.columnLists = []
        count = 1
        for opt in columnElements:
            if (opt.text !='Icon Color' and opt.text != 'Icon' ):
                self.columnLists.append(count)
            count = count + 1
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.cancelButtonXpath)))
        self.cancelButton=self.myPyDriver.find_element_by_xpath(self.cancelButtonXpath)
        self.cancelButton.click()
        
        _normalFilter = "e"        
        _intFilter = "42"          #Must be an int
        _dateFilter = "8/6/2016"   #Must be in date format ('*/*/*')
        
        for col in range(0,len(self.columnLists)):
            filterXpath = "//th["+str(self.columnLists[col])+"]/a/span"
            filterTextXpath = "//th["+str(self.columnLists[col])+"]/a[2]"
            filterText = self.myPyDriver.find_element_by_xpath(filterTextXpath).text
            Norm_Filter.Norm_Filter(_normalFilter, self.columnLists[col], "catalog", self.myPyDriver, self.wait)
           
            if (col != len(self.columnLists)):
               self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
               self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.className_IconCatalog))).click()
               self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,'td')))
        return super(PythonSpaceRunnerCatalogUnitTest, self).__init__(methodName)

    #TODO: FIX
    def test_CatalogColumnManager(self,methodName = 'test_CatalogColumnManager'):
        _modelXPath = self.listItemModelXpath
        _modelTabXPath = self.a_contains_Model_Xpath
        _availableXPath = self.columnManager_available
        _selectedXPath = self.columnManager_selected
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.manageColumnsButtonXpath))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, _modelXPath)))
        source_element = self.myPyDriver.find_element_by_xpath(_modelXPath)
        dest_element = self.myPyDriver.find_element_by_xpath(_availableXPath)
        self.action.drag_and_drop(source_element, dest_element).perform()
        time.sleep(1)
        #assert Model is in available fields column
        self.assertTrue(len(self.myPyDriver.find_elements_by_xpath(self.columnManager_available_model))==1)
        self.myPyDriver.find_element_by_name(self.name_submitButton).click()
        time.sleep(1)
        #assert Model is no longer displayed
        self.assertFalse(self.myPyDriver.find_element_by_xpath(_modelTabXPath).is_displayed())
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.css_headerButton))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, _modelXPath)))
        source_element = self.myPyDriver.find_element_by_xpath(_modelXPath)
        dest_element = self.myPyDriver.find_element_by_xpath(_selectedXPath)
        #drag Model back
        action_chains.ActionChains(self.myPyDriver).drag_and_drop(source_element, dest_element).perform()
        time.sleep(1)
        #assert Model is in selected fields column
        self.assertTrue(len(self.myPyDriver.find_elements_by_xpath(self.columnManager_selected_model))==1)
        self.myPyDriver.find_element_by_name(self.name_submitButton).click()
        time.sleep(1)
        #assert Model is displayed again
        self.assertTrue(self.myPyDriver.find_element_by_xpath(_modelTabXPath).is_displayed())
        return super(PythonSpaceRunnerCatalogUnitTest, self).__init__(methodName)
    
    def tearDown(self):
        #self.signOutLink = self.myPyDriver.find_element_by_xpath(self.logoutLinkXPath)
        #self.signOutLink.click()
        self.myPyDriver.quit()
        return super(PythonSpaceRunnerCatalogUnitTest, self).tearDown()
if __name__ == '__main__':
    unittest.main()
