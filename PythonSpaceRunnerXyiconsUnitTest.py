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

class PythonSpaceRunnerXyiconsUnitTest(unittest.TestCase):
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
        
        #webDriver setup
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
                #self.wait.until(EC.element_to_be_clickable((By.XPATH,self.doneButton))).click()
                #self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconHome)))
                self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconProject)))
                self.selectProjectModule = self.myPyDriver.find_element_by_class_name(self.className_IconProject)
                self.selectProjectModule.click()
                self.wait.until(EC.element_to_be_clickable((By.XPATH,self.projectTileXPath))).click()
               
               #Used for creating filter tests, less amount of xyicons, does not work with delete methods
                #self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div/h5[contains(text(),'Filter Tests')]"))).click()
                time.sleep(1)
                
                #self.wait.until(EC.presence_of_element_located((By.XPATH,self.projectTileXPath)))
                #self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconProject))).click()
                #_projectTile = self.myPyDriver.find_elements_by_link_text('Sel del sol')
                #_projectTile.click()
            except:
                self.myPyDriver.quit()
                self.fail()
            return super(PythonSpaceRunnerXyiconsUnitTest, self).__init__(methodName)
        else:
            print("Unable to init webDriver!")

   # def closeWalkMe(self):
   #     _closeButton = ".walkme-click-and-hover.walkme-custom-balloon-close-button.walkme-action-close"
   #     _closeButtonCSSSelector = self.myPyDriver.find_element_by_css_selector(_closeButton)
   #     _closeButtonCSSSelector.click()
    
    
    #Can be called in order to switch to a project with designated amounts of xyicons, for quicker testing
    def goToFilterProject(self):
        time.sleep(2)
        self.selectProjectModule = self.myPyDriver.find_element_by_class_name(self.className_IconProject)
        self.selectProjectModule.click()
        time.sleep(2)
        project = self.myPyDriver.find_element_by_xpath('//h5[contains(text(),"Filter Tests")]')
        project.click()
        time.sleep(3)
    
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

    def compare_values(self,storedValue,elementId):
        element = self.myPyDriver.find_element_by_id(elementId)
        value = element.get_attribute("value")
        return (storedValue == value)
     
    def waitForDataLoad(self):
        self.wait = WebDriverWait(self.myPyDriver, 30)
        self.wait.until(EC.invisibility_of_element_located((By.XPATH,'//div[contains(text(),"Your project data is being loaded...")]')))
        time.sleep(1)
        self.wait = WebDriverWait(self.myPyDriver, 15)
        return
    

    def selectXyiconViaFloorplan(self):
        #click space
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.spaceXpath))).click()
        #click xyicon on floorplan
        pass
    

    #TODO: implement JS for drag-drop function
    #notes: drag and drop silenium function does not work with html 5
    #       once outside drag and drop method is found this method shouold work
    #Status: 
    def test_addXyicons(self, methodName = 'test_addXyicons'):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
        #self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "td")))
        
        #xyicon_table = self.myPyDriver.find_elements_by_tag_name("tr")
        xyiconCountXPath = self.span_contains_start + "Xyicon(s)" + self.contains_end
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xyiconCountXPath)))
        time.sleep(4)
        self.firstXyiconText = self.myPyDriver.find_element_by_xpath(xyiconCountXPath).text.split();
        self.firstCount =self.firstXyiconText[4] 
        self.myPyDriver.find_element_by_class_name(self.className_IconSpaces).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.galleryTileXpath)))
        project = self.myPyDriver.find_element_by_xpath(self.spaceXpath)
        project.click()
        
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,self.catalogItemXpath)))
        catalog = self.myPyDriver.find_elements_by_tag_name(self.catalogItemXpath)
        floorplan = self.myPyDriver.find_element_by_id(self.id_floorplan)
        time.sleep(4)
        self.action.drag_and_drop(catalog[3],floorplan).perform()   ############################### Noted Issue
        time.sleep(4)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
        #self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))
        
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xyiconCountXPath)))
        time.sleep(4)
        self.secondXyiconText = self.myPyDriver.find_element_by_xpath(xyiconCountXPath).text.split()
        self.secondCount =self.secondXyiconText[4] 
        #updated_xyicon_table = self.myPyDriver.find_elements_by_tag_name("tr")
        #self.assertTrue((len(updated_xyicon_table)-len(xyicon_table)) == 6) 
        self.assertTrue(int(self.firstCount) < int(self.secondCount))
        return super(PythonSpaceRunnerXyiconsUnitTest, self).__init__(methodName)

    #Average time: 55 seconds
    #Precondition: has xyicon to be deleted in 'Xyicons' tab
    #TODO: 
    #Notes: Cannot pull data from date text box in order to check it
    #       Therefore it is not checked in edit method
    #Status: ✔
    def test_editXyiconsViaButton(self, methodName = 'test_editXyiconsViaButton'): 
        #Go to xyicons tab
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName)))
        iconXyicon = self.myPyDriver.find_element_by_class_name(self.iconXyiconClassName)
        iconXyicon.click()
        #self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//td')))
        self.waitForDataLoad() #Solves current project data loading issue which crashes all tests, adds ~~15 seconds
        #click/edit on first row
        gridRow = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.xyiconGridRow))) 
        gridRow.click()
        self.myPyDriver.find_element_by_xpath(self.editButton).click()

        #send edit values and store them in a list
        self.wait.until(EC.presence_of_all_elements_located((By.NAME, self.className_xyiconForms)))
        xyiconForm = self.myPyDriver.find_element_by_name(self.className_xyiconForms)
        inputs = xyiconForm.find_elements_by_xpath(self.xyiconFormInput)
        notes = xyiconForm.find_element_by_xpath(self.xyiconFormNotes)
        fieldValues = []
        
        for input in inputs:
            fieldValues.append(self.send_random(input))
        notesValue = self.send_random(notes)
       
        time.sleep(1)
        self.myPyDriver.find_element_by_xpath(self.editDateButtonXPath).click() 
        dateSelectorXPath = self.selectDateXPath 
        self.dateSelector = self.myPyDriver.find_element_by_xpath(dateSelectorXPath)
        time.sleep(2)
        self.dateSelector.click()
        time.sleep(4)
        #self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,self.name_submitButton)))
        submitButton = self.myPyDriver.find_element_by_name(self.name_submitButton)
        submitButton.click()
        time.sleep(4)
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))
        #reclick on first row and edit
        self.myPyDriver.find_element_by_xpath(self.xyiconGridRow).click()
        self.myPyDriver.find_element_by_xpath(self.editButton).click()
        self.wait.until(EC.presence_of_all_elements_located((By.NAME, self.className_xyiconForms)))
        xyiconForm = self.myPyDriver.find_element_by_name(self.className_xyiconForms)
        inputs = xyiconForm.find_elements_by_xpath(self.xyiconFormInput)
        notes = xyiconForm.find_element_by_xpath(self.xyiconFormNotes)
        notesField = self.myPyDriver.find_element_by_xpath(self.notesFieldXPath)  
        
        fieldValuesLength  = len(fieldValues)
        fieldValuesCounter = 0
        #Check edited values for correctness
        while fieldValuesCounter < fieldValuesLength:
            for input in inputs:
                self.highlightElement(input)
                if(input.get_attribute("value") != "Area:  sqft"):
                    self.assertTrue(input.get_attribute("value") == fieldValues[fieldValuesCounter])
                fieldValuesCounter += 1
        self.assertTrue(notes.get_attribute("value") == notesValue)
        
        return super(PythonSpaceRunnerXyiconsUnitTest, self).__init__(methodName)
    
    #Average time: 55 seconds
    #Precondition: has xyicon in grid
    #Status: ✔
    def test_editXyInServiceDate(self, methodName = 'test_editXyInServiceDate'):
        time.sleep(2)
        #Go to xyicon tab
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName)))
        iconXyicon = self.myPyDriver.find_element_by_class_name(self.iconXyiconClassName)
        iconXyicon.click()
        #Click on first row
        #self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//td')))
        self.waitForDataLoad() #Solves current project data loading issue which crashes all tests, adds ~~15 seconds        
        gridRow = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.xyiconGridRow))) 
        gridRow.click()
        self.myPyDriver.find_element_by_xpath(self.editButton).click()
        #clear date Field
        self.wait.until(EC.presence_of_all_elements_located((By.NAME, self.className_xyiconForms)))
        datePicker = self.myPyDriver.find_element_by_xpath(self.inServiceDatePicker)
        if datePicker.get_attribute("value") != '':
            datePicker.clear()
        time.sleep(1)
        #Click datePicker and choose date
        self.myPyDriver.find_element_by_xpath(self.editDateButtonXPath).click() 
        dateSelectorXPath = self.selectDateXPath 
        self.dateSelector = self.myPyDriver.find_element_by_xpath(dateSelectorXPath)
        time.sleep(2)
        self.dateSelector.click()
        time.sleep(4)        
        submitButton = self.myPyDriver.find_element_by_name(self.name_submitButton)
        submitButton.click()
        time.sleep(4)
        #click on first row
        self.correctDate = time.strftime("%Y/%m/13")
        gridRow = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.xyiconGridRow)))  
        self.action.double_click(gridRow).perform()
        time.sleep(2)
        #Pull data from date field value
        datePicker = self.myPyDriver.find_element_by_xpath(self.inServiceDatePicker)
        self.editedDate = datePicker.get_attribute("data-value") 
        self.myPyDriver.find_element_by_xpath(self.editDateButtonXPath).click() 
        
        editedDateElem = self.myPyDriver.find_element_by_xpath('//tr/td[@aria-selected="true"]/a')
        self.draftEditedDate = editedDateElem.get_attribute("data-value") 
        #Compare pulled Date and correct date
        splitEditedDate = self.draftEditedDate.split('/')
        splitCorrectDate = self.draftEditedDate.split('/')

        #compare ints to prevent error (ex. day 08 != 8)
        finalEditedDate = desired_array = [int(numeric_string) for numeric_string in splitEditedDate]
        finalCorrectedDate = desired_array = [int(numeric_string) for numeric_string in splitCorrectDate]
        
        self.assertTrue(finalEditedDate == finalCorrectedDate)
        return super(PythonSpaceRunnerXyiconsUnitTest, self).__init__(methodName)


    #Average time: 43 seconds
    #Precondition: has xyicon to be deleted in 'Xyicons' tab
    #TODO: 
    #Status: 
    def test_editXyiconsViaFLoorplanButton(self, methodName = 'test_editXyiconsViaFLoorplanButton'):
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"li")))
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.className_IconSpaces)))
        time.sleep(4)
        #click on space tab
        iconSpace = self.myPyDriver.find_element_by_class_name(self.className_IconSpaces)
        iconSpace.click()
        #click on space
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.galleryTileXpath)))
        project = self.myPyDriver.find_element_by_xpath(self.spaceXpath)
        project.click()
        
        #click on center xyicon in space              
        self.wait.until(EC.element_to_be_clickable((By.ID,self.id_floorplan)))
        self.waitForDataLoad() #Solves current project data loading issue which crashes all tests, adds ~~15 seconds
        floorplan = self.myPyDriver.find_element_by_id(self.id_floorplan)
        floorplan.click()
        #click edit button
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.editButton))).click()
        self.wait.until(EC.presence_of_all_elements_located((By.NAME, self.className_xyiconForms)))
        
        #storing xyicon ID
        self.IDXPath = self.span_contains_start + "Editor" + self.contains_end
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.IDXPath)))
        time.sleep(1)
        self.xyIDText = self.myPyDriver.find_element_by_xpath(self.IDXPath).text.split()
        self.xyID = self.xyIDText[4]
        #send edit values and store them in a list
        xyiconForm = self.myPyDriver.find_element_by_name(self.className_xyiconForms)
        inputs = xyiconForm.find_elements_by_xpath(self.xyiconFormInput)
        notes = xyiconForm.find_element_by_xpath(self.xyiconFormNotes)
        fieldValues = []
        for input in inputs:
            fieldValues.append(self.send_random(input))
        notesValue = self.send_random(notes)
        time.sleep(2)              
        self.wait.until(EC.presence_of_all_elements_located((By.NAME,self.name_submitButton)))
        submitButton = self.myPyDriver.find_element_by_xpath(self.xyiconSpaceEditSaveXPath) #self.xyiconSpaceEditSaveXPath '//ui-button-submit[@id="equipEditSav"]/button'
        submitButton.click()
        time.sleep(2)

        #self.wait.until(EC.element_to_be_clickable((By.NAME,self.className_IconXyicons)))
        iconXyicon = self.myPyDriver.find_element_by_class_name(self.className_IconXyicons) 
        iconXyicon.click()
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))
   
        #filter xyicons to find one in center       
        time.sleep(2)
        self.myPyDriver.find_element_by_xpath(self.xyiconIDFilterButton).click()
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"span")))         
        self.textBar = self.myPyDriver.find_element_by_xpath("//input[@type='text'][2]") #self.filterTextBarXPath "//input[@type='text'][2]"
        self.highlightElement(self.textBar)
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,"//input[@type='text'][2]"))) 
        time.sleep(3)
        self.textBar.click()
        self.textBar.send_keys(self.xyID)
        self.submitButton = self.myPyDriver.find_element_by_xpath("//div[2]/button") #self.filterSubmitButtonXPath "//div[2]/button"
        self.submitButton.click()  
        self.myPyDriver.find_element_by_xpath(self.xyiconGridRow).click()   
        
        #checks that there is only one xyicon after filter      
        self.xyiconCountXPath = self.span_contains_start + "Xyicon(s)" + self.contains_end
        self.firstXyiconText = self.myPyDriver.find_element_by_xpath(self.xyiconCountXPath).text.split();
        self.rowsFound =self.firstXyiconText[4] 
        self.assertTrue(self.rowsFound==str(1))

        #click on top row 
        self.myPyDriver.find_element_by_xpath(self.xyiconGridRow).click()
        self.myPyDriver.find_element_by_xpath(self.editButton).click()
        self.wait.until(EC.presence_of_all_elements_located((By.NAME, self.className_xyiconForms)))
        xyiconForm = self.myPyDriver.find_element_by_name(self.className_xyiconForms)
        inputs = xyiconForm.find_elements_by_xpath(self.xyiconFormInput)
        #Ensure you are checking the same xyicon as edited earlier
        #self.wait.until(EC.presence_of_element_located((By.XPATH,IDXPath)))
        time.sleep(2)
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,'td')))
        self.updatedXyIDText = self.myPyDriver.find_element_by_xpath(self.IDXPath).text.split()
        self.updatedXyID = self.xyIDText[4]
        self.assertTrue(self.xyID == self.updatedXyID)

        #check edited fields for correctness
        notes = xyiconForm.find_element_by_xpath(self.xyiconFormNotes)
        notesField = self.myPyDriver.find_element_by_xpath(self.notesFieldXPath)
        #datePicker = self.myPyDriver.find_element_by_xpath(self.datePickerXPath)
        fieldValuesLength  = len(fieldValues)
        fieldValuesCounter = 0
        #TODO fix the field arrays to compare len values
       
        while fieldValuesCounter < fieldValuesLength:
            for input in inputs:
                self.highlightElement(input)
                if(input.get_attribute("value") != "Area:  sqft"):
                    self.assertTrue(input.get_attribute("value") == fieldValues[fieldValuesCounter])
                fieldValuesCounter += 1
        self.assertTrue(notes.get_attribute("value") == notesValue)
 
        return super(PythonSpaceRunnerXyiconsUnitTest, self).__init__(methodName)  


    #Average time: 25 seconds
    #Precondition: has xyicon to be deleted in 'Xyicons' tab
    #TODO: ✔
    def test_deleteXyiconsByDeleteButton(self, methodName = 'test_deleteXyiconsByDeleteButton'):
        time.sleep(2)
        #Click on xyicon tab
        xyiconTab= self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName)))
        xyiconTab.click()
        #self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))
        self.waitForDataLoad() #Solves current project data loading issue which crashes all tests, adds ~~15 seconds
        time.sleep(2)
        #Use text in bottom right to find the current number of xyicons
        xyiconCountXPath = self.span_contains_start + "Xyicon(s)" + self.contains_end
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xyiconCountXPath)))
        time.sleep(2)
        self.firstXyiconText = self.myPyDriver.find_element_by_xpath(xyiconCountXPath).text.split();
        self.firstCount =self.firstXyiconText[4] 
        #click on the bottom row
        table = self.myPyDriver.find_elements_by_tag_name("tr")
        last_element = table.pop()
        last_element.click()
        #click on the delete/ok button
        self.myPyDriver.find_element_by_xpath(self.deleteButtonXPath).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.okButton))).click()
        time.sleep(3)
        #Use the bottom right text to check for correctness
        self.secondXyiconText = self.myPyDriver.find_element_by_xpath(xyiconCountXPath).text.split()
        self.secondCount =self.secondXyiconText[4]
        self.assertTrue(int(self.firstCount) > int(self.secondCount))
        return super(PythonSpaceRunnerXyiconsUnitTest, self).__init__(methodName)
    
    #Average time: 30 seconds
    #Precondition: has xyicon to be deleted in 'Xyicons' tab
    #TODO: ✔
    def test_deleteXyiconsByEditMenu(self, methodName = 'test_deleteXyiconsByEditMenu'):
        time.sleep(2)
        #Click on xyicon tab
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "td")))
        time.sleep(2)
        #find current number of xyicons through bottom right text
        xyiconCountXPath = self.span_contains_start + "Xyicon(s)" + self.contains_end
        self.firstXyiconText = self.myPyDriver.find_element_by_xpath(xyiconCountXPath).text.split();
        self.firstCount =self.firstXyiconText[4] 
        #Click on bottom row
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xyiconCountXPath)))
        table = self.myPyDriver.find_elements_by_tag_name("tr")
        last_element = table.pop()
        self.action.double_click(last_element).perform()
        #Click on edit button
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editDeleteButtonXPath)))
        #Click on delete/ok button 
        deleteElem = self.myPyDriver.find_element_by_xpath(self.editDeleteButtonXPath)
        deleteElem.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.okButton))).click()
        time.sleep(5)
        #find current number of xyicons through bottom right text
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xyiconCountXPath)))
        time.sleep(2)
        self.secondXyiconText = self.myPyDriver.find_element_by_xpath(xyiconCountXPath).text.split()
        self.secondCount =self.secondXyiconText[4]
        #Check that xyicon has been deleted
        self.assertTrue(int(self.firstCount) > int(self.secondCount))
        #self.assertFalse((len(table)==len(updatedTable)))     
        return super(PythonSpaceRunnerXyiconsUnitTest, self).__init__(methodName)

    #Average time: 40 seconds (explicit wait on floorplan load)
    #Precondition: has xyicon to be deleted in center of DEL SOL floorplan
    #Status: ✔
    def test_deleteXyiconsByFloorplanDeleteKey(self, methodName = "test_deleteXyiconsByFloorplanDeleteKey"):
        time.sleep(2)
        #Click on xyicons tab
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
        #self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))
        self.waitForDataLoad() #Solves current project data loading issue which crashes all tests, adds ~~15 seconds
        time.sleep(2)
        #Find current number of xyicons through bottom right text
        xyiconCountXPath = self.span_contains_start + "Xyicon(s)" + self.contains_end
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xyiconCountXPath)))
        time.sleep(2)
        self.firstXyiconText = self.myPyDriver.find_element_by_xpath(xyiconCountXPath).text.split();
        self.firstCount =self.firstXyiconText[4] 
        #Click on spaces tab
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.className_IconSpaces))).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.galleryTileXpath)))
        #click on DEL SOL space
        project = self.myPyDriver.find_element_by_xpath(self.spaceXpath)
        project.click()
        time.sleep(4)
        floorplan = self.myPyDriver.find_element_by_id(self.id_floorplan)
        floorplan.click()
        #Click on center xyicon
        time.sleep(3)
        #Press delete key / ok button
        floorplan.send_keys(Keys.DELETE)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.okButtonXpath))).click()
        time.sleep(4)
        #Click xyicon tab
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))
        time.sleep(2)
        
        #Find current number of xyicons through bottom right text
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xyiconCountXPath)))
        time.sleep(2)
        self.secondXyiconText = self.myPyDriver.find_element_by_xpath(xyiconCountXPath).text.split()
        self.secondCount =self.secondXyiconText[4]
        #Check that xyicon has been deleted
        self.assertTrue(int(self.firstCount) > int(self.secondCount))   
        return super(PythonSpaceRunnerXyiconsUnitTest, self).__init__(methodName)
    
    #Average time: 43 seconds (explicit wait on floorplan load)
    #Precondition: has xyicon to be deleted in center of DEL SOL floorplan
    #Notes:     implicit waits do not work on buttons within space taskbar
    #Status: ✔
    def test_deleteXyiconsByFloorplanButton(self, methodName = "test_deleteXyiconsByFloorplanButton"):
        time.sleep(2)
        #Click the xyicon tab
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
        #self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "td")))
        self.waitForDataLoad() #Solves current project data loading issue which crashes all tests, adds ~~15 seconds
        time.sleep(2)
        #Find current number of xyicons through bottom right text
        xyiconCountXPath = self.span_contains_start + "Xyicon(s)" + self.contains_end
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xyiconCountXPath)))
        time.sleep(2)
        self.firstXyiconText = self.myPyDriver.find_element_by_xpath(xyiconCountXPath).text.split();
        self.firstCount =self.firstXyiconText[4] 
        #Click on spaces tab
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.className_IconSpaces))).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.galleryTileXpath)))
        #Click on DEL SOL space
        project = self.myPyDriver.find_element_by_xpath(self.spaceXpath)
        project.click()
        time.sleep(5)
        #Click on center xyicon
        floorplan = self.myPyDriver.find_element_by_id(self.id_floorplan)
        floorplan.click()
        time.sleep(2)
        #Click on quick edit menu
        quickEdit = self.myPyDriver.find_element_by_xpath(self.xyiconQuickEditXPath)
        quickEdit.click()
        #Click on delete/ok button
        time.sleep(1)
        delete = self.myPyDriver.find_element_by_xpath(self.spaceDeleteButtonXPath)
        delete.click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.okButtonXpath))).click()
        time.sleep(4)
        #Click on xyicon tab
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))
        time.sleep(2)
        #Find current number of xyicons through bottom right text
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xyiconCountXPath)))
        time.sleep(2)
        self.secondXyiconText = self.myPyDriver.find_element_by_xpath(xyiconCountXPath).text.split()
        self.secondCount =self.secondXyiconText[4]
        #Check that xyicon has been deleted
        self.assertTrue(int(self.firstCount) > int(self.secondCount))
        return super(PythonSpaceRunnerXyiconsUnitTest, self).__init__(methodName)

    #Average time: 43 seconds (explicit wait on floorplan load)
    #Precondition: has xyicon to be deleted in center of DEL SOL floorplan
    #Created: Thomas Brochard
    #Status: ✔
    def test_deleteXyiconsByFloorplanRightClick(self, methodName = 'test_deleteXyiconsByFloorplanRightClick'):
        time.sleep(2)
        #1 Click on xyicon tab
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
        #self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))
        self.waitForDataLoad() #Solves current project data loading issue which crashes all tests, adds ~~15 seconds
        #2 Find current number of xyicons through bottom right text
        xyiconCountXPath = self.span_contains_start + "Xyicon(s)" + self.contains_end
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xyiconCountXPath)))
        time.sleep(2)
        self.firstXyiconText = self.myPyDriver.find_element_by_xpath(xyiconCountXPath).text.split();
        self.firstCount =self.firstXyiconText[4] 
        #3 Click on spaces tab
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.className_IconSpaces))).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.galleryTileXpath)))
        #4 Click on DEL SOL space
        project = self.myPyDriver.find_element_by_xpath(self.spaceXpath)
        project.click()
        time.sleep(5)
        #5 Click on center xyicon, and right click it
        floorplan = self.myPyDriver.find_element_by_id(self.id_floorplan)
        floorplan.click()            
        self.action.context_click(floorplan).perform()
        time.sleep(1)
        #6 click on delete/ok button
        delete = self.myPyDriver.find_element_by_xpath(self.deleteRightClickXPath)
        delete.click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.okButtonXpath))).click()
        time.sleep(4)
        #7 Click on xyicon tab
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))
        time.sleep(2)
        #8 Find current number of xyicons through bottom right text
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xyiconCountXPath)))
        time.sleep(2)
        self.secondXyiconText = self.myPyDriver.find_element_by_xpath(xyiconCountXPath).text.split()
        self.secondCount =self.secondXyiconText[4]
        #9 Ensure xyicon has been deleted
        self.assertTrue(int(self.firstCount) > int(self.secondCount))
        return super(PythonSpaceRunnerXyiconsUnitTest, self).__init__(methodName)


    #TODO :  
    #Average time:  (dependant on which columns are present)
    #Precondition: 
    #notes: glitch with textbar is workaround by refreshing webpage after every column (last lines of test)
    #Status: 
    def test_filterByColumn(self,methodName= 'test_filterByColumn'):
       # self.goToFilterProject()
        time.sleep(2)
        self.myPyDriver.find_element_by_class_name(self.iconXyiconClassName).click()
        
        #self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,'td')))
        time.sleep(2)

       #Use manage column to list columns to be checked
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.columnManagerButtonXPath))).click()
        time.sleep(2)
        selectedColumn = self.myPyDriver.find_element_by_xpath("//div[2]/div/div[2]/ul")
        columnElements = selectedColumn.find_elements_by_tag_name('li')
        time.sleep(2)
        self.columnLists = []
        self.columnManager_available_model=[]
        count = 1
        for opt in columnElements:
            #if (opt.text !='Icon Color' and opt.text != 'Icon' ):
                if(opt.text == 'Department' and len(self.columnLists)==5): self.columnLists.append(13)
                else: self.columnLists.append(count)
                count = count + 1
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.cancelButtonXpath)))
        self.cancelButton=self.myPyDriver.find_element_by_xpath(self.cancelButtonXpath)
        self.cancelButton.click()
        
       #set filters for each type of column
        _normalFilter = "e"        
        _intFilter = '42'          #Must be an int  class for solution (keys.NUM5))
        _dateFilter = "7/31/2010"   #Must be in date format ('*/*/*')
           
       #iterate over grid columns   
        for col in range(0,len(self.columnLists)):
            filterXpath = "//th["+str(self.columnLists[col])+"]/a/span"
            filterTextXpath = "//th["+str(self.columnLists[col])+"]/a[2]"
            filterText = self.myPyDriver.find_element_by_xpath(filterTextXpath).text
            

           #These are built in fields that are not in the fields tab
            noFields = ["Xyicon ID","Class","Description","closed Events", "Open Events","Icon","Make","Model","Space","Square Feet","Square Meters"]
           #Find current columns filter type by using fields tab 
            type = ''
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.className_IconFields))).click()
            self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,'td')))
            if(filterText not in noFields): #xyicon ID is not in fields 
                time.sleep(2)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, self.xyiconGridRow)))
                table = self.myPyDriver.find_elements_by_xpath(self.xyiconGridRow)            
                for tr in table:
                    linetext = tr.text
                    if(filterText in linetext):
                        type = tr.text
                        break
                              
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
            self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,'td')))
            #Call class depending on which filterType is needed (norm, int, or date) 
            if(filterText == "Xyicon ID"):
                Int_Filter.Int_Filter(_intFilter, self.columnLists[col], self.myPyDriver, self.wait)
            elif("Date" in type):
                Date_Filter.Date_Filter(_dateFilter, self.columnLists[col], self.myPyDriver, self.wait)
            else:
                Norm_Filter.Norm_Filter(_normalFilter, self.columnLists[col], "xyicon", self.myPyDriver, self.wait)
         
        return super(PythonSpaceRunnerXyiconsUnitTest, self).__init__(methodName)
    

    #TODO : Fix test, needs page scrolling when 300<Xyicons
    #Average time: 42
    #Precondition: Model is included in selected fields column
    #Notes: precondition can be eliminated once drag n drop function is established  
    #Status: 
    def test_xyiconSortByModel(self, methodName = 'test_xyiconSortByModel'):
        time.sleep(3)
        self.goToFilterProject()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
        time.sleep(2)
        _trXPath = self.xyiconGridRow
        _sortTab = self.a_contains_Model_Xpath      
        time.sleep(25)
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "td")))
        self.waitForDataLoad() #Solves current project data loading issue which crashes all tests, adds ~~15 seconds
        _modelTab = self.myPyDriver.find_element_by_xpath(_sortTab)
        _modelTab.click()
        time.sleep(1)
        _table = self.myPyDriver.find_elements_by_xpath(_trXPath)
       
        #ensure that precondition is met and find eventID index
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.columnManagerButtonXPath))).click()
        time.sleep(2)
        selectedColumn = self.myPyDriver.find_element_by_xpath("//div[2]/div/div[2]/ul")
        columnElements = selectedColumn.find_elements_by_tag_name('li')
        time.sleep(2)
        columnLength = len(columnElements)
        modelIndex = 0
        for _li in columnElements:
            self.highlightElement(_li)
            #checking precondition
            self.assertTrue(modelIndex<=columnLength)
            if _li.text == 'Model':
                break
            else:
                modelIndex = modelIndex + 1        
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.cancelButtonXpath)))
        self.cancelButton=self.myPyDriver.find_element_by_xpath(self.cancelButtonXpath)
        self.cancelButton.click()
        time.sleep(1)
        #record id's of rows in table
        _modelList = []        
        for _tr in _table:
            _tds= _tr.find_elements_by_tag_name('td')
            _modelList.append(_tds[modelIndex].text)             
        #click on id filter
        _modelTab = self.myPyDriver.find_element_by_xpath(_sortTab)
        _modelTab.click()
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "td")))
        time.sleep(1)                
        _updatedIdList = []
        _table = self.myPyDriver.find_elements_by_xpath(_trXPath)        
        time.sleep(1)
        #Record rows of table after id filter is clicked
        for _tr in _table:
            _tds= _tr.find_elements_by_tag_name('td')
            _updatedIdList.append(_tds[modelIndex].text)      
        #reverse the anti-alphabetical list to make sure it was sorted exactly backwards    
        _reversedList = []
        for i in range(0,len(_updatedIdList)):
            _reversedList.append(_updatedIdList.pop())  
                   
        self.assertTrue(_reversedList == _modelList)     
        return super(PythonSpaceRunnerXyiconsUnitTest, self).__init__(methodName)


    #TODO: FIX
    def test_xyiconColumnManager(self, methodName = "test_xyiconColumnManager"):
        self.closeWalkMe()
        _modelXPath       = self.listItemModelXpath
        _modelHeaderXPath = self.a_contains_Model_Xpath
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
        time.sleep(5)       
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.manageColumnsButtonXpath))).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, _modelXPath)))
        source_element = self.myPyDriver.find_element_by_xpath(_modelXPath)
        dest_element = self.myPyDriver.find_element_by_xpath(self.columnManager_available)
        self.action.drag_and_drop(source_element, dest_element).perform()
        time.sleep(3)
        #assert Model is in available fields column
        self.assertTrue(len(self.myPyDriver.find_elements_by_xpath(self.columnManager_available_model))==1)
        self.myPyDriver.find_element_by_name(self.name_submitButton).click()
        time.sleep(3)
        #assert Model is no longer displayed
        self.assertFalse(self.myPyDriver.find_element_by_xpath(_modelHeaderXPath).is_displayed())
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.css_headerButton))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, _modelXPath)))
        source_element = self.myPyDriver.find_element_by_xpath(_modelXPath)
        dest_element = self.myPyDriver.find_element_by_xpath(self.columnManager_selected)
        #drag Model back
        #self.action.drag_and_drop(source_element,dest_element)
        action_chains.ActionChains(self.myPyDriver).drag_and_drop(source_element, dest_element).perform()
        time.sleep(3)
        #assert Model is in selected fields column
        self.assertTrue(len(self.myPyDriver.find_elements_by_xpath(self.columnManager_selected_model))==1)
        self.myPyDriver.find_element_by_name(self.name_submitButton).click()
        time.sleep(3)
        #assert User Status is displayed again
        self.assertTrue(self.myPyDriver.find_element_by_xpath(_modelHeaderXPath).is_displayed())
        return super(PythonSpaceRunnerXyiconsUnitTest, self).__init__(methodName)

    #TODO: FIX
    def test_xyiconsDragColumns(self, methodName = "test_xyiconsDragColumns"):
        _tableHeadersXPath     = self.xyiconGridHeaderXpath
        _departmentHeaderXPath = self.xyiconDepartmentHeader
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, _departmentHeaderXPath)))
        _departmentHeader = self.myPyDriver.find_element_by_xpath(_departmentHeaderXPath)
        _spaceHeader = self.myPyDriver.find_element_by_xpath(self.xyiconSpaceHeader)
        _table = self.myPyDriver.find_elements_by_xpath(_tableHeadersXPath)
        _tableHeaders = []
        for th in _table:
            title = th.get_attribute("data-title")
            _tableHeaders.append(title)
        _dIndex = _tableHeaders.index("Department")
        _sIndex = _tableHeaders.index("Space")
        self.action.drag_and_drop(_departmentHeader, _spaceHeader).perform()
        time.sleep(3)
        _table = self.myPyDriver.find_elements_by_xpath(_tableHeadersXPath)
        _upTableHeaders = []
        for th in _table:
            title = th.get_attribute("data-title")
            _upTableHeaders.append(title)
        self.assertTrue(_upTableHeaders.index("Department") == 1)
        self.assertTrue(_upTableHeaders.index("Space") == (_sIndex + 1))
        return super(PythonSpaceRunnerXyiconsUnitTest, self).__init__(methodName)

    #TODO :  
    #Average time:  24 seconds (dependant on number of expor files you have)
    #Precondition: 
    #Status: ✔
    def test_xyiconsExport(self, methodName = "test_xyiconsExport"):
        path = self.downloads_path
        init_num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.exportButtonXpath))).click()
        time.sleep(3)
        #######system dialog handler########
        #PyAutoGuiExporter.PyAutoGuiExporter()
        ####################################
        #verify increase in # of files in 'path' by 1
        post_num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
        self.assertTrue((post_num_files - init_num_files) == 1)
        return super(PythonSpaceRunnerXyiconsUnitTest, self).__init__(methodName)


    #TODO: FIX
    def test_quickEdit(self, methodName = 'test_quickEdit'):
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.className_IconSpaces))).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.galleryTileXpath)))
        project = self.myPyDriver.find_element_by_xpath(self.spaceXpath)
        project.click()
        time.sleep(8)
        floorplan = self.myPyDriver.find_element_by_id(self.id_floorplan)
        floorplan.click()
        #self.wait.until(EC.element_to_be_clickable((By.XPATH, self.detailsButton))).click()
        inputFields = "controlBoundary"#'//div[@title="Click to edit"]'
        inputs = self.myPyDriver.find_elements(By.CLASS_NAME,inputFields)
        formValues = []
        for input in inputs:
            input.click()
            self.highlightElement(input)
            formValues.append(self.send_random(input))
                    
            
        #formValues.append(input.send_keys("test"))
        #_spaceTile = "//img[@alt='Del Sol HOA']"
        #self.wait.until(EC.presence_of_element_located((By.XPATH,_spaceTile))).click()
        #_floorPlan = self.myPyDriver.find_element_by_id(self.id_floorplan)
        #_floorplan.click()
        #time.sleep(3)
        return super(PythonSpaceRunnerXyiconsUnitTest, self).__init__(methodName)



    def tearDown(self):
        #self.signOutLink = self.myPyDriver.find_element_by_xpath(self.logoutLinkXPath)
        #self.signOutLink.click()
        self.myPyDriver.quit()
        return super(PythonSpaceRunnerXyiconsUnitTest, self).tearDown()

if __name__ == '__main__':
    unittest.main()
