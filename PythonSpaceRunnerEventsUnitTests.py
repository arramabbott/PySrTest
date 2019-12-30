import unittest, Selectors, config, Norm_Filter, Int_Filter, Date_Filter
import string
import sys
import random
import datetime
import time
import os.path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException  
import PyAutoGuiExporter

class PythonSpaceRunnerEventsUnitTests(unittest.TestCase):

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

        #gmail
        self.gmail_address  = config_object.gmail_address
        self.gmail_password = config_object.gmail_password

        #users
        self.adminName = config_object.adminFullName
        self.gmailAccountOwnersName = config_object.gmailUserFullName

        #init selector object
        selector_object = Selectors.Selectors()

        #Application Buttons and links
        self.className_IconXyicons         = selector_object.className_IconXyicons
        self.doneButton                    = selector_object.doneButton
        self.name_userName                 = selector_object.name_userName
        self.name_pwInput                  = selector_object.name_pwInput
        self.name_submit                   = selector_object.name_submit
        self.className_IconProject         = selector_object.className_IconProject
        self.className_IconEvents          = selector_object.className_IconEvents
        self.editButtonXpath               = selector_object.editButtonXpath
        self.logoutLinkXPath               = selector_object.logoutLinkXPath
        self.excelButtonClassName          = selector_object.excelButtonClassName
        self.editEventGridRowXPath         = selector_object.editEventGridRowXPath
        self.projectTileXPath              = selector_object.projectTileXPath
        self.spaceFloorPlanTileXPath       = selector_object.spaceFloorPlanTileXPath
        self.spaceFloorPlanCSSSeletor      = selector_object.spaceFloorPlanCSSSeletor
        self.eventAddButtonXPath           = selector_object.eventAddButtonXPath
        self.reportedByListSelectorXPath   = selector_object.reportedByListSelectorXPath
        self.editEventSpanXPath            = selector_object.editEventSpanXPath
        self.spacesHeaderXpath             = selector_object.spacesHeaderXpath
        self.span_contains_start           = selector_object.span_contains_start
        self.contains_end                  = selector_object.contains_end
        self.eventEdit_saveXpath           = selector_object.eventEdit_saveXpath
        self.id_navigator                  = selector_object.id_navigator
        self.eventGrid_firstItem           = selector_object.eventGrid_firstItem
        self.eventIDXpath                  = selector_object.eventIDXpath
        self.deleteButtonXPath             = selector_object.deleteButtonXPath
        self.okButtonXpath                 = selector_object.okButtonXpath
        self.id_eventListItem              = selector_object.id_eventListItem
        self.editEventsButtonXpath         = selector_object.editEventsButtonXpath
        self.eventRow1Xpath                = selector_object.eventRow1Xpath
        self.childDivXpath                 = selector_object.childDivXpath
        self.subElementEventId             = selector_object.subElementEventId
        self.subElementStrong              = selector_object.subElementStrong
        self.specialCaseDeleteButton       = selector_object.specialCaseDeleteButton
        self.specialCaseOkButton           = selector_object.specialCaseOkButton
        self.manageColumnsButtonXpath      = selector_object.manageColumnsButtonXpath
        self.listItemModelXpath            = selector_object.listItemModelXpath
        self.columnManager_available       = selector_object.columnManager_available
        self.columnManager_available_model = selector_object.columnManager_available_model
        self.name_submitButton             = selector_object.name_submitButton
        self.a_contains_Model_Xpath        = selector_object.a_contains_Model_Xpath
        self.a_contains_EventID_Xpath      = selector_object.a_contains_EventID_Xpath
        self.columnManager_selected        = selector_object.columnManager_selected
        self.css_headerButton              = selector_object.css_headerButton
        self.columnManager_selected_model  = selector_object.columnManager_selected_model
        self.a_contains_Event_ID           = selector_object.a_contains_Event_ID
        self.a_contains_Status             = selector_object.a_contains_Status
        self.eventGridTableHeaderXpath     = selector_object.eventGridTableHeaderXpath
        self.downloadsPath                 = selector_object.downloadsPath
        self.exportAutoItPath              = selector_object.exportAutoItPath
        self.exportButtonXpath             = selector_object.exportButtonXpath
        self.eventGridTableRowXpath        = selector_object.eventGridTableRowXpath
        self.sortMenuButtonsXpath          = selector_object.sortMenuButtonsXpath
        self.eventsFilterIDXpath           = selector_object.eventsFilterIDXpath
        self.eventsFilterModelXpath        = selector_object.eventsFilterModelXpath
        self.eventsFilterButton            = selector_object.eventsFilterButton
        self.eventsModelFilterCloseXpath   = selector_object.eventsModelFilterCloseXpath
        #form fields for events
        self.name_issueDescription      = selector_object.name_issueDescription
        self.reportedByFieldXPath       = selector_object.reportedByFieldXPath
        self.assignedToFieldXPath       = selector_object.assignedToFieldXPath
        self.assignedToFieldCSSSelector = selector_object.assignedToFieldCSSSelector
        self.eventDateFieldID           = selector_object.eventDateFieldID
        self.newEvent_completedDateID   = selector_object.newEvent_completedDateID
        self.editEvent_completedDateID  = selector_object.editEvent_completedDateID
        self.eventUrgentCheckBoxXPath   = selector_object.eventUrgentCheckBoxXPath
        self.eventCompletedByXPath      = selector_object.eventCompletedByXPath
        self.eventSaveButtonXPath       = selector_object.eventSaveButtonXPath
        self.eventCancelButtonXPath     = selector_object.eventCancelButtonXPath
        self.eventEditButton            = selector_object.eventEditButton
        self.assignedToBoxXPath         = selector_object.assignedToBoxXPath
        self.createdByBoxXPath          = selector_object.createdByBoxXPath
        self.resolvedByBoxXPath         = selector_object.resolvedByBoxXPath
        self.events_adminUserXpath      = selector_object.events_adminUserXpath 
        self.events_gmailUserXpath      = selector_object.events_gmailUserXpath   
        self.completedByUserXPath       = selector_object.completedByUserXPath
        self.css_CanvasFloorplan        = selector_object.css_CanvasFloorplan
        self.inServiceDatePicker        = selector_object.inServiceDatePicker
        #email fields
        self.name_Email            = selector_object.name_Email
        self.name_signIn           = selector_object.name_signIn
        self.name_Passwd           = selector_object.name_Passwd
        self.dt_contains           = selector_object.dt_contains
        self.className_emailWindow = selector_object.className_emailWindow
        self.first_unopened        = selector_object.first_unopened
        self.xyiconGridRow         = selector_object.xyiconGridRow
        #for form field verification (selected options)
        self.reportedByOptionXPath  = selector_object.reportedByOptionXPath
        self.assignedToOptionXPath  = selector_object.assignedToOptionXPath
        self.completedByOptionXPath = selector_object.completedByOptionXPath
        self.resolutionCostXPath    = selector_object.resolutionCostXPath
        self.filterTextBar1XPath    = selector_object.filterTextBar1XPath
        self.className_IconSpaces  = selector_object.className_IconSpaces
        self.galleryTileXpath      = selector_object.galleryTileXpath
        self.spaceXpath            = selector_object.spaceXPath
        self.id_floorplan          = selector_object.id_floorplan
        self.spaceXpath            = selector_object.spaceXpath
        self.columnManagerButtonXPath      = selector_object.columnManagerButtonXPath 
        self.cancelButtonXpath             = selector_object.cancelButtonXpath
        self.eventFilterButton             = selector_object.catalogFilterButton
        self.eventFilterMenuXPath        = selector_object.catalogFilterMenuXPath
        self.iconXyiconClassName   = selector_object.className_IconXyicons
        self.className_IconSpaces  = selector_object.className_IconSpaces
        self.className_IconFields          = selector_object.className_IconFields

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
                self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconProject)))
                self.selectProjectModule = self.myPyDriver.find_element_by_class_name(self.className_IconProject)
                self.selectProjectModule.click()
                time.sleep(2)
                self.wait.until(EC.presence_of_element_located((By.XPATH,self.projectTileXPath)))
                self.selectProject = self.myPyDriver.find_element_by_xpath(self.projectTileXPath)
                time.sleep(2)
                self.selectProject.click()
                time.sleep(1)             
                #self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,self.spaceFloorPlanCSSSeletor)))
                #self.projectSpaceTile = self.myPyDriver.find_element_by_css_selector(self.spaceFloorPlanCSSSeletor)
                #self.projectSpaceTile.click()
                self.assertTrue(EC.presence_of_element_located((By.XPATH,self.spacesHeaderXpath)))
            except:
                self.myPyDriver.quit()
                self.fail()
            return super(PythonSpaceRunnerEventsUnitTests, self).__init__(methodName)
        else:
            print("Unable to init webDriver!")

    def random_string(self):
        range = random.randint(10,20)
        randomString = ''.join([random.choice(string.ascii_letters +string.digits) for n in xrange(range)])
        return randomString

    def highlightElement(self,element):
        self.myPyDriver.execute_script("arguments[0].setAttribute('style', arguments[1]);",element, "color: red; border: 3px solid red;")
    
    def waitForDataLoad(self):
        self.wait = WebDriverWait(self.myPyDriver, 30)
        self.wait.until(EC.invisibility_of_element_located((By.XPATH,'//div[contains(text(),"Your project data is being loaded...")]')))
        time.sleep(1)
        self.wait = WebDriverWait(self.myPyDriver, 15)
        return
    
        
    #TODO : checkbox.isSelected() always return false
    #Average time: 
    #Precondition: a xyicon exists 
    #Status: 
    #Notes: dependant on email verification success, fails when email is too slow.
    #       checkbox.isSelected() always return false         
    def test_AddEventViaXyiconGrid(self, methodName = 'test_AddEventViaXyiconGrid'):
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconXyicons))).click()
        #self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "td")))
        self.waitForDataLoad() #Solves current project data loading issue which crashes all tests, adds ~~15 seconds
        time.sleep(3)
        #select xyicon
        table = self.myPyDriver.find_elements_by_tag_name("tr")
        last_element = table.pop()
        last_element.click()
        time.sleep(1)
        #hit edit button
        _editButton = self.myPyDriver.find_element_by_xpath(self.editButtonXpath)
        _editButton.click()
        time.sleep(3)
        #hit event button
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.eventAddButtonXPath)))
        _eventAddButton = self.myPyDriver.find_element_by_xpath(self.eventAddButtonXPath)
        _eventAddButton.click()
        time.sleep(3)
        #description
        self.wait.until(EC.element_to_be_clickable((By.NAME,self.name_issueDescription)))
        _eventDescription = self.myPyDriver.find_element_by_name(self.name_issueDescription)
        _description = 'New Event - ' + self.random_string()
        _eventDescription.clear()
        _eventDescription.send_keys(_description)
        #reported by
        _reportedBy = self.myPyDriver.find_element_by_xpath(self.reportedByFieldXPath)
        _reportedBy.click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.createdByBoxXPath)))
        time.sleep(1)
        _reportedByBox = self.myPyDriver.find_element_by_xpath(self.createdByBoxXPath)
        _reportedByBox.find_element_by_xpath(self.events_adminUserXpath).click()
        #assigned to
        _assignedTo = self.myPyDriver.find_element_by_xpath(self.assignedToFieldXPath)
        _assignedTo.click()
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.assignedToBoxXPath)))
        _assignedToBox = self.myPyDriver.find_element_by_xpath(self.assignedToBoxXPath)
        _assignedToBox.find_element_by_xpath(self.events_gmailUserXpath).click()
        #urgent
        _urgentCheckBox = self.myPyDriver.find_element_by_xpath(self.eventUrgentCheckBoxXPath)
        #if _urgentCheckBox.is_selected() == False:
        #    _urgentCheckBox.click()
        #else:
        #    pass
        #date
        _eventDateValue = '06/20/2015'
        _eventDate = self.myPyDriver.find_element_by_id(self.eventDateFieldID)
        _eventDate.click()
        _eventDate.clear()
        _eventDate.send_keys(_eventDateValue)
        #date completed
        _completedDateValue = '06/20/2015'
        _completedDateField = self.myPyDriver.find_element_by_id(self.newEvent_completedDateID)
        _completedDateField.click()
        _completedDateField.send_keys(_completedDateValue)
        #completed by
        _completedByUser = self.myPyDriver.find_element_by_xpath(self.completedByUserXPath)
        self.myPyDriver.execute_script("arguments[0].scrollIntoView(true);", _completedByUser);
        _completedByUser.click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.resolvedByBoxXPath)))
        _completedByBox = self.myPyDriver.find_element_by_xpath(self.resolvedByBoxXPath)
        _completedBy = _completedByBox.find_element_by_xpath(self.events_gmailUserXpath)
        time.sleep(1)
        _completedBy.click()
        #resoulution cost
        _resolutionCostValue = '32'
        _resolutionCostField = self.myPyDriver.find_element_by_xpath(self.resolutionCostXPath)
        #resolution cost field has to be forced visible in order to interact with it
        self.highlightElement(_resolutionCostField)
        _resolutionCostField.send_keys(_resolutionCostValue)
        #save
        time.sleep(1)
        self.myPyDriver.find_element_by_xpath(self.eventEdit_saveXpath ).click()
        time.sleep(3)
        self.myPyDriver.find_element_by_xpath(self.eventCancelButtonXPath).click()
        time.sleep(1)
        self.myPyDriver.find_element_by_class_name(self.className_IconEvents).click()
        time.sleep(3)
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'td')))
        _eventXPath = self.span_contains_start+_description+self.contains_end
        self.wait.until(EC.element_to_be_clickable((By.XPATH,_eventXPath)))
        _event = self.myPyDriver.find_element_by_xpath(_eventXPath)
        self.myPyDriver.execute_script("arguments[0].scrollIntoView(true);", _event)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,_eventXPath)))
        _event.click()
        time.sleep(2)
        self.myPyDriver.find_element_by_xpath(self.eventEditButton).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.editEventSpanXPath)))
        
        #verify fields
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable((By.NAME,self.name_issueDescription)))
        _eventDescription = self.myPyDriver.find_element_by_name(self.name_issueDescription)
        self.assertTrue(_eventDescription.get_attribute('value') == _description)
        _reportedBy = self.myPyDriver.find_element_by_xpath(self.reportedByOptionXPath)
        self.assertTrue(str(_reportedBy.text) == self.adminName)
        _assignedTo = self.myPyDriver.find_element_by_xpath(self.assignedToOptionXPath)
        self.assertTrue(str(_assignedTo.text) == self.gmailAccountOwnersName)
        _completedBy = self.myPyDriver.find_element_by_xpath(self.completedByOptionXPath)
        self.assertTrue(str(_completedBy.text) == self.gmailAccountOwnersName)
        _eventDate = self.myPyDriver.find_element_by_id(self.eventDateFieldID)
        self.assertTrue(str(_eventDate.get_attribute('value')) == _eventDateValue)
        _completedDate = self.myPyDriver.find_element_by_id(self.editEvent_completedDateID)
        self.assertTrue(str(_completedDate.get_attribute('value')) == _completedDateValue)
        _urgentCheckBox = self.myPyDriver.find_element_by_xpath(self.eventUrgentCheckBoxXPath)
        #self.assertTrue(_urgentCheckBox.isSelected())
        _resolutionCost = self.myPyDriver.find_element_by_xpath(self.resolutionCostXPath)
        self.assertTrue(str(_resolutionCost.get_attribute('value')) == _resolutionCostValue)
        
        #email verification (works only if the email is sent in time) 
        self.myPyDriver.get("https://mail.google.com/mail")
        self.wait.until(EC.element_to_be_clickable((By.NAME, self.name_Email)))
        _EmailField = self.myPyDriver.find_element_by_name(self.name_Email)
        _EmailField.send_keys(self.gmail_address)
        self.wait.until(EC.element_to_be_clickable((By.NAME, self.name_signIn)))
        _SignIn = self.myPyDriver.find_element_by_name(self.name_signIn)
        _SignIn.click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, self.name_Passwd)))
        _PassField = self.myPyDriver.find_element_by_name(self.name_Passwd)
        _PassField.send_keys(self.gmail_password)
        _SignIn = self.myPyDriver.find_element_by_id(self.name_signIn)
        _SignIn.click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.className_emailWindow)))
        time.sleep(60)
        self.myPyDriver.find_element_by_xpath(self.first_unopened).click()
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "dl")))
        _eventNotice = self.myPyDriver.find_elements_by_xpath(self.dt_contains+_description+self.contains_end)
        self.assertTrue(len(_eventNotice)>0)
        return super(PythonSpaceRunnerEventsUnitTests, self).__init__(methodName)

    #TODO : 
    #Average time: 
    #Precondition: a xyicon exists 
    #Status: 
    #Notes: dependant on email verification success, fails when email is too slow.
    #       checkbox.isSelected() always return false      
    def test_AddEventViaFloorPlanTool(self, methodName = 'test_AddEventViaFloorPlanTool'):
        time.sleep(4)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.className_IconSpaces))).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.galleryTileXpath)))
        #select a space
        project = self.myPyDriver.find_element_by_xpath(self.spaceXpath)
        project.click()
        #time.sleep(15)
        self.waitForDataLoad() #Solves current project data loading issue which crashes all tests, adds ~~15 seconds
        #Right click on the center of the floorplan
        floorplan = self.myPyDriver.find_element_by_id(self.id_floorplan)
        floorplan.click()            
        self.action.context_click(floorplan).perform()       
        #Hit event button
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.eventAddButtonXPath)))
        _eventAddButton = self.myPyDriver.find_element_by_xpath(self.eventAddButtonXPath)
        _eventAddButton.click()
        time.sleep(3)
        #description
        self.wait.until(EC.element_to_be_clickable((By.NAME,self.name_issueDescription)))
        _eventDescription = self.myPyDriver.find_element_by_name(self.name_issueDescription)
        _description = 'New Event - ' + self.random_string()
        _eventDescription.clear()
        _eventDescription.send_keys(_description)
        #reported by
        _reportedBy = self.myPyDriver.find_element_by_xpath(self.reportedByFieldXPath)
        _reportedBy.click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.createdByBoxXPath)))
        time.sleep(1)
        _reportedByBox = self.myPyDriver.find_element_by_xpath(self.createdByBoxXPath)
        _reportedByBox.find_element_by_xpath(self.events_adminUserXpath).click()
        #assigned to
        _assignedTo = self.myPyDriver.find_element_by_xpath(self.assignedToFieldXPath)
        _assignedTo.click()
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.assignedToBoxXPath)))
        _assignedToBox = self.myPyDriver.find_element_by_xpath(self.assignedToBoxXPath)
        _assignedToBox.find_element_by_xpath(self.events_gmailUserXpath).click()
        #urgent
        _urgentCheckBox = self.myPyDriver.find_element_by_xpath(self.eventUrgentCheckBoxXPath)
        #if _urgentCheckBox.is_selected() == False:
        #    _urgentCheckBox.click()
        #else:
        #    pass
        #date
        _eventDateValue = '06/20/2015'
        _eventDate = self.myPyDriver.find_element_by_id(self.eventDateFieldID)
        _eventDate.click()
        _eventDate.clear()
        _eventDate.send_keys(_eventDateValue)
        #date completed
        _completedDateValue = '06/20/2015'
        _completedDateField = self.myPyDriver.find_element_by_id(self.newEvent_completedDateID)
        _completedDateField.click()
        _completedDateField.send_keys(_completedDateValue)
        #completed by
        _completedByUser = self.myPyDriver.find_element_by_xpath(self.completedByUserXPath)
        self.myPyDriver.execute_script("arguments[0].scrollIntoView(true);", _completedByUser);
        _completedByUser.click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.resolvedByBoxXPath)))
        _completedByBox = self.myPyDriver.find_element_by_xpath(self.resolvedByBoxXPath)
        time.sleep(1)
        _completedBy = _completedByBox.find_element_by_xpath(self.events_gmailUserXpath)
        _completedBy.click()
        #resoultion cost
        _resolutionCostValue = '32'
        _resolutionCostField = self.myPyDriver.find_element_by_xpath(self.resolutionCostXPath)
        #resolution cost field has to be forced visible in order to interact with it...
        self.highlightElement(_resolutionCostField)
        _resolutionCostField.send_keys(_resolutionCostValue)
        #save
        self.myPyDriver.find_element_by_xpath(self.eventEdit_saveXpath ).click() #self.eventSubmitButton wouldn't work here for some reason
        #self.wait.until(EC.staleness_of((_completedDateField)))
        #time.sleep(3)
        #self.myPyDriver.find_element_by_xpath(self.eventCancelButtonXPath).click()
        time.sleep(3)
        self.myPyDriver.find_element_by_class_name(self.className_IconEvents).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'td')))
        _eventXPath = self.span_contains_start+_description+self.contains_end
        self.wait.until(EC.visibility_of_element_located((By.XPATH,_eventXPath)))
        _event = self.myPyDriver.find_element_by_xpath(_eventXPath)
        self.myPyDriver.execute_script("arguments[0].scrollIntoView(true);", _event)
        _event.click()
        time.sleep(2)
        self.myPyDriver.find_element_by_xpath(self.eventEditButton).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.editEventSpanXPath)))
        #verify fields
        time.sleep(10)
        self.wait.until(EC.element_to_be_clickable((By.NAME,self.name_issueDescription)))
        _eventDescription = self.myPyDriver.find_element_by_name(self.name_issueDescription)
        self.assertTrue(_eventDescription.get_attribute('value') == _description)
        _reportedBy = self.myPyDriver.find_element_by_xpath(self.reportedByOptionXPath)
        self.assertTrue(str(_reportedBy.text) == self.adminName)
        _assignedTo = self.myPyDriver.find_element_by_xpath(self.assignedToOptionXPath)
        self.assertTrue(str(_assignedTo.text) == self.gmailAccountOwnersName)
        _completedBy = self.myPyDriver.find_element_by_xpath(self.completedByOptionXPath)
        self.assertTrue(str(_completedBy.text) == self.gmailAccountOwnersName)
        _eventDate = self.myPyDriver.find_element_by_id(self.eventDateFieldID)
        self.assertTrue(str(_eventDate.get_attribute('value')) == _eventDateValue)
        _completedDate = self.myPyDriver.find_element_by_id(self.editEvent_completedDateID)
        self.assertTrue(str(_completedDate.get_attribute('value')) == _completedDateValue)
        #_urgentCheckBox = self.myPyDriver.find_element_by_xpath(self.eventUrgentCheckBoxXPath)
        #self.assertTrue(_urgentCheckBox.is_selected())
        _resolutionCost = self.myPyDriver.find_element_by_xpath(self.resolutionCostXPath)
        self.assertTrue(str(_resolutionCost.get_attribute('value')) == _resolutionCostValue)
        
        #email verification (works only if the email is sent in time) 
        self.myPyDriver.get("https://mail.google.com/mail")
        self.wait.until(EC.element_to_be_clickable((By.NAME, self.name_Email)))
        _EmailField = self.myPyDriver.find_element_by_name(self.name_Email)
        _EmailField.send_keys(self.gmail_address)
        self.wait.until(EC.element_to_be_clickable((By.NAME, self.name_signIn)))
        _SignIn = self.myPyDriver.find_element_by_name(self.name_signIn)
        _SignIn.click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, self.name_Passwd)))
        _PassField = self.myPyDriver.find_element_by_name(self.name_Passwd)
        _PassField.send_keys(self.gmail_password)
        _SignIn = self.myPyDriver.find_element_by_id(self.name_signIn)
        _SignIn.click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.className_emailWindow)))
        time.sleep(30)
        self.myPyDriver.find_element_by_xpath(self.first_unopened).click()
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "dl")))
        _eventNotice = self.myPyDriver.find_elements_by_xpath(self.dt_contains+_description+self.contains_end)
        self.assertTrue(len(_eventNotice)>0)
        
        return super(PythonSpaceRunnerEventsUnitTests, self).__init__(methodName)

    #Average time: 38 seconds
    #Precondition: an event exists
    #TODO: figure out how to click urgent checkmark box
    #Status: 
    def test_EditEventViaGridDoubleClick(self, methodName = 'test_EditEventViaGridDoubleClick'):
        self.myPyDriver.maximize_window() #resolves the double click exception, something to do with window size
        time.sleep(3)
        self.className_IconEvents = self.myPyDriver.find_element_by_class_name(self.className_IconEvents)
        self.className_IconEvents.click()
        time.sleep(2)
        self.waitForDataLoad() #Solves current project data loading issue which crashes all tests, adds ~~15 seconds
        #Select event in event grid
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editEventGridRowXPath)))
        self.eventGridRow = self.myPyDriver.find_element_by_xpath(self.editEventGridRowXPath)
        self.myPyDriver.execute_script("arguments[0].scrollIntoView(true);", self.eventGridRow);
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editEventGridRowXPath)))
        #double click
        self.action.double_click(self.eventGridRow).perform()        
        #description
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.NAME,self.name_issueDescription)))
        _eventDescription = self.myPyDriver.find_element_by_name(self.name_issueDescription)
        _description = 'Edited Event - ' + self.random_string()
        _eventDescription.clear()
        _eventDescription.send_keys(_description)
        #reported by
        time.sleep(3)
        _reportedBy = self.myPyDriver.find_element_by_xpath(self.reportedByFieldXPath)
        _reportedBy.click()
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.createdByBoxXPath)))
        _reportedByBox = self.myPyDriver.find_element_by_xpath(self.createdByBoxXPath)
        _reportedByBox.find_element_by_xpath(self.events_gmailUserXpath).click()
        #assigned to
        _assignedTo = self.myPyDriver.find_element_by_xpath(self.assignedToFieldXPath)
        _assignedTo.click()
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.assignedToBoxXPath)))
        _assignedToBox = self.myPyDriver.find_element_by_xpath(self.assignedToBoxXPath)
        _assignedToBox.find_element_by_xpath(self.events_gmailUserXpath).click()
        #urgent
        #_urgentCheckBox = self.myPyDriver.find_element_by_xpath(self.eventUrgentCheckBoxXPath)
        #_urgent = False
        #var = self.myPyDriver.find_element_by_xpath("//input[@id='option']").is_selected()
        #if self.myPyDriver.find_element_by_xpath("//input[@id='option']").is_selected():
        #    _urgent = True
        #self.highlightElement(_urgentCheckBox)
        #time.sleep(1)
        #_urgentCheckBox.click()
        #date
        _eventDateValue = '06/10/2015'
        _eventDate = self.myPyDriver.find_element_by_id(self.eventDateFieldID)
        _eventDate.click()
        _eventDate.clear()
        _eventDate.send_keys(_eventDateValue)
        #date completed
        _completedDateValue = '06/10/2015'
        _completedDateField = self.myPyDriver.find_element_by_id(self.editEvent_completedDateID)
        _completedDateField.click()
        _completedDateField.clear()
        _completedDateField.send_keys(_completedDateValue)
        #completed by
        _completedByUser = self.myPyDriver.find_element_by_xpath(self.completedByUserXPath)
        self.myPyDriver.execute_script("arguments[0].scrollIntoView(true);", _completedByUser);
        _completedByUser.click()
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.resolvedByBoxXPath)))
        _completedByBox = self.myPyDriver.find_element_by_xpath(self.resolvedByBoxXPath)
        _completedBy = _completedByBox.find_element_by_xpath(self.events_adminUserXpath)
        _completedBy.click()
        #resolution cost
        _resolutionCostValue = '64'
        _resolutionCostField = self.myPyDriver.find_element_by_xpath(self.resolutionCostXPath)
        #resolution cost field has to be forced visible in order to interact with it...
        self.highlightElement(_resolutionCostField)
        _resolutionCostField.clear()
        _resolutionCostField.send_keys(_resolutionCostValue)
        time.sleep(1)
        #save
        self.myPyDriver.find_element_by_xpath(self.eventSaveButtonXPath).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'td')))
        _eventXPath = self.span_contains_start+_description+self.contains_end
        self.wait.until(EC.element_to_be_clickable((By.XPATH,_eventXPath)))
        _event = self.myPyDriver.find_element_by_xpath(_eventXPath)
        self.myPyDriver.execute_script("arguments[0].scrollIntoView(true);", _event)
        _event.click()
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editButtonXpath)))
        self.eventEditButton = self.myPyDriver.find_element_by_xpath(self.editButtonXpath)
        self.eventEditButton.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.editEventSpanXPath)))
        
        #verify fields
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable((By.NAME,self.name_issueDescription)))
        _eventDescription = self.myPyDriver.find_element_by_name(self.name_issueDescription)
        self.assertTrue(_eventDescription.get_attribute('value') == _description)
        _reportedBy = self.myPyDriver.find_element_by_xpath(self.reportedByOptionXPath)
        self.assertTrue(str(_reportedBy.text) == self.gmailAccountOwnersName)
        time.sleep(1)
        _assignedTo = self.myPyDriver.find_element_by_xpath(self.assignedToOptionXPath)
        self.assertTrue(str(_assignedTo.text) == self.gmailAccountOwnersName)
        _completedBy = self.myPyDriver.find_element_by_xpath(self.completedByOptionXPath)
        self.assertTrue(str(_completedBy.text) == self.adminName)
        _eventDate = self.myPyDriver.find_element_by_id(self.eventDateFieldID)
        self.assertTrue(str(_eventDate.get_attribute('value')) == _eventDateValue)
        _completedDate = self.myPyDriver.find_element_by_id(self.editEvent_completedDateID)
        self.assertTrue(str(_completedDate.get_attribute('value')) == _completedDateValue)
        #_urgentCheckBox = self.myPyDriver.find_element_by_xpath(self.eventUrgentCheckBoxXPath)
        #isSelected = self.myPyDriver.find_element_by_xpath(self.eventUrgentCheckBoxXPath).is_selected()
        #self.assertTrue(_urgent != _urgentCheckBox.is_selected())
        return super(PythonSpaceRunnerEventsUnitTests, self).__init__(methodName)


    #Average time: 45 seconds
    #Precondition: an event exists
    #TODO: figure out how to click urgent checkmark box
    #Status: 
    def test_EditEventViaEditButton(self, methodName = 'test_EditEventViaEditButton'):
        time.sleep(2)
        self.className_IconEvents = self.myPyDriver.find_element_by_class_name(self.className_IconEvents)
        self.className_IconEvents.click()
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "td")))
        #self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editEventGridRowXPath)))
        time.sleep(2)
        #Select event in event grid
        self.eventGridRow = self.myPyDriver.find_element_by_xpath(self.editEventGridRowXPath)
        self.eventGridRow.click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editButtonXpath)))
        self.eventEditButton = self.myPyDriver.find_element_by_xpath(self.editButtonXpath)
        time.sleep(2)
        self.waitForDataLoad() #Solves current project data loading issue which crashes all tests, adds ~~15 seconds
        self.eventEditButton.click()
        #description
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.NAME,self.name_issueDescription)))
        _eventDescription = self.myPyDriver.find_element_by_name(self.name_issueDescription)
        _description = 'Edited Event - ' + self.random_string()
        _eventDescription.clear()
        _eventDescription.send_keys(_description)
        #reported by
        time.sleep(3)
        _reportedBy = self.myPyDriver.find_element_by_xpath(self.reportedByFieldXPath)
        _reportedBy.click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.createdByBoxXPath)))
        time.sleep(1)
        _reportedByBox = self.myPyDriver.find_element_by_xpath(self.createdByBoxXPath)
        _reportedByBox.find_element_by_xpath(self.events_gmailUserXpath).click()
        #assigned to+
        _assignedTo = self.myPyDriver.find_element_by_xpath(self.assignedToFieldXPath)
        _assignedTo.click()
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.assignedToBoxXPath)))
        _assignedToBox = self.myPyDriver.find_element_by_xpath(self.assignedToBoxXPath)
        _assignedToBox.find_element_by_xpath(self.events_adminUserXpath).click()
        #urgent
        #_urgentCheckBox = self.myPyDriver.find_element_by_xpath(self.eventUrgentCheckBoxXPath)
        
        #_urgent = False
        #if _urgentCheckBox.is_selected():
        #    _urgent = True
        
        #self.highlightElement(_urgentCheckBox)
        #actions.moveToElement(_urgentCheckBox).click().build().perform();
        #date
        _eventDateValue = '06/10/2015'
        _eventDate = self.myPyDriver.find_element_by_id(self.eventDateFieldID)
        _eventDate.click()
        _eventDate.clear()
        _eventDate.send_keys(_eventDateValue)
        #date completed
        _completedDateValue = '06/10/2015'
        _completedDateField = self.myPyDriver.find_element_by_id(self.editEvent_completedDateID)
        _completedDateField.click()
        _completedDateField.clear()
        _completedDateField.send_keys(_completedDateValue)
        time.sleep(1)
        #completed by
        _completedByUser = self.myPyDriver.find_element_by_xpath(self.completedByUserXPath)
        self.myPyDriver.execute_script("arguments[0].scrollIntoView(true);", _completedByUser);
        _completedByUser.click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.resolvedByBoxXPath)))
        time.sleep(1)
        _completedByBox = self.myPyDriver.find_element_by_xpath(self.resolvedByBoxXPath)
        _completedBy = _completedByBox.find_element_by_xpath(self.events_adminUserXpath)
        _completedBy.click()
        #resolution cost
        _resolutionCostValue = '64'
        _resolutionCostField = self.myPyDriver.find_element_by_xpath(self.resolutionCostXPath)
        time.sleep(1)
        #resolution cost field has to be forced visible in order to interact with it...
        self.highlightElement(_resolutionCostField)
        _resolutionCostField.clear()
        _resolutionCostField.send_keys(_resolutionCostValue)
        time.sleep(1)
        #save
        self.save = self.myPyDriver.find_element_by_xpath(self.eventSaveButtonXPath)
        self.save.click()
        time.sleep(2)
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'td')))
        _eventXPath = self.span_contains_start+_description+self.contains_end
        self.wait.until(EC.element_to_be_clickable((By.XPATH,_eventXPath)))
        _event = self.myPyDriver.find_element_by_xpath(_eventXPath)
        self.myPyDriver.execute_script("arguments[0].scrollIntoView(true);", _event)
        _event.click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editButtonXpath)))
        self.eventEditButton = self.myPyDriver.find_element_by_xpath(self.editButtonXpath)
        self.eventEditButton.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.editEventSpanXPath)))
        
        #verify fields
        time.sleep(10)
        self.wait.until(EC.element_to_be_clickable((By.NAME,self.name_issueDescription)))
        _eventDescription = self.myPyDriver.find_element_by_name(self.name_issueDescription)
        self.assertTrue(_eventDescription.get_attribute('value') == _description)
        _reportedBy = self.myPyDriver.find_element_by_xpath(self.reportedByOptionXPath)
        self.assertTrue(str(_reportedBy.text) == self.gmailAccountOwnersName)
        _assignedTo = self.myPyDriver.find_element_by_xpath(self.assignedToOptionXPath)
        self.assertTrue(str(_assignedTo.text) == self.adminName)
        _completedBy = self.myPyDriver.find_element_by_xpath(self.completedByOptionXPath)
        self.assertTrue(str(_completedBy.text) == self.adminName)
        _eventDate = self.myPyDriver.find_element_by_id(self.eventDateFieldID)
        self.assertTrue(str(_eventDate.get_attribute('value')) == _eventDateValue)
        _completedDate = self.myPyDriver.find_element_by_id(self.editEvent_completedDateID)
        self.assertTrue(str(_completedDate.get_attribute('value')) == _completedDateValue)
        #_urgentCheckBox = self.myPyDriver.find_element_by_xpath(self.eventUrgentCheckBoxXPath)
        #self.assertTrue(_urgent != _urgentCheckBox.is_selected())
        return super(PythonSpaceRunnerEventsUnitTests, self).__init__(methodName)
    '''
    def test_EditUrgentEvent(self, methodName = 'test_EditUgentEvent'):
        #TODO : finish edit function
        self.className_IconEvents = self.myPyDriver.find_element_by_class_name(self.className_IconEvents)
        self.className_IconEvents.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editEventGridRowXPath)))
        self.eventGridRow = self.myPyDriver.find_element_by_xpath(self.editEventGridRowXPath)
        self.action.double_click(self.eventGridRow).perform()
        return super(PythonSpaceRunnerEventsUnitTests, self).__init__(methodName)
    '''


    #Average time: 26 seconds
    #Precondition: an event exists
    #TODO: 
    #Status: ✔
    def test_DeleteEventViaEventsGrid(self, methodName = 'test_DeleteEventViaEventsGrid'):
        time.sleep(1)
        self.className_IconEvents = self.myPyDriver.find_element_by_class_name(self.className_IconEvents)
        self.className_IconEvents.click()
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))
        self.waitForDataLoad() #Solves current project data loading issue which crashes all tests, adds ~~15 seconds
        #unique XPath for _event so the eventID can be gotten from the element
        #Select event in event grid
        time.sleep(2)
        table = self.myPyDriver.find_elements_by_xpath(self.xyiconGridRow)
        table[0].click()
        time.sleep(2)
        preLineText = table[0].text 
        time.sleep(2)
        #_eventID = int(_event.find_element_by_xpath(self.eventIDXpath).text) #will cause inconsistancys if id is not column 1, change later
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.deleteButtonXPath)))
        self.deleteButton = self.myPyDriver.find_element_by_xpath(self.deleteButtonXPath)
        self.deleteButton.click()
        time.sleep(1)
        _okButtonXPath = self.okButtonXpath
        self.wait.until(EC.element_to_be_clickable((By.XPATH,_okButtonXPath)))
        _okButton = self.myPyDriver.find_element_by_xpath(_okButtonXPath)
        _okButton.click()
        #Select event in event grid
        time.sleep(2)
        table = self.myPyDriver.find_elements_by_xpath(self.xyiconGridRow)
        table[0].click()
        postLinetext = table[0].text 
        time.sleep(1)
        postLineText =  table[0].text
        self.assertTrue(preLineText != postLineText)
      
        return super(PythonSpaceRunnerEventsUnitTests, self).__init__(methodName)

    #Average time: 26 seconds
    #Precondition: center xyicon ontop of stack in floorplan has an event 
    #TODO: 
    #Status: 
    def test_DeleteEventsViaFloorplan(self, methodName = 'test_DeleteEventsViaFloorplan'):
        time.sleep(3)
        tile = self.myPyDriver.find_element_by_xpath(self.spaceXpath)
        time.sleep(1)
        tile.click()

        #self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,self.css_CanvasFloorplan)))
        #_canvas = self.myPyDriver.find_element_by_css_selector(self.css_CanvasFloorplan)
        #self.wait.until(EC.visibility_of_element_located((By.ID,self.id_navigator)))
        self.waitForDataLoad() #Solves current project data loading issue which crashes all tests, adds ~~15 seconds
        floorplan = self.myPyDriver.find_element_by_id(self.id_floorplan)
        floorplan.click()            
        time.sleep(3)
        eventList = self.myPyDriver.find_elements_by_xpath('//span[contains(text(),"Assigned")]')
        #self.wait.until(EC.presence_of_all_elements_located((By.ID,self.id_eventListItem)))
        #self.myPyDriver.find_element_by_id(self.id_eventListItem).click()
        preconditionMet = len(eventList)>0
        self.assertTrue(preconditionMet)
        time.sleep(1)
        self.action.click(eventList[0]).perform()
        #get the event ID
        time.sleep(2)
        _elementFound = False
        _parentElement = self.myPyDriver.find_element_by_xpath(self.eventRow1Xpath)
        _divList = _parentElement.find_elements_by_xpath(self.childDivXpath)
        for _div in _divList:
            _check = _div.find_elements_by_xpath(self.subElementEventId)
            if len(_check) == 1:
                _dirtyEventID = str(_div.find_element_by_xpath(self.subElementStrong).text)
                _eventID = int(''.join([i for i in _dirtyEventID if i.isdigit()]))
                _elementFound = True
                break
        #delete button xpath, can't get by text = delete or id because of the xyicon pane's delete button
        self.myPyDriver.find_element_by_xpath(self.specialCaseDeleteButton).click()
        time.sleep(2)
        _okButtonXPath = self.specialCaseOkButton
        self.wait.until(EC.element_to_be_clickable((By.XPATH,_okButtonXPath)))
        _okButton = self.myPyDriver.find_element_by_xpath(_okButtonXPath)
        _okButton.click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconEvents)))
        self.className_IconEvents = self.myPyDriver.find_element_by_class_name(self.className_IconEvents)
        self.className_IconEvents.click()
        time.sleep(2)
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))
        
        table = self.myPyDriver.find_elements_by_xpath(self.xyiconGridRow)         
        for tr in table:
            tds = tr.find_elements_by_tag_name('td')
            currentText = int(tds[0].text)
            self.assertTrue(currentText != _eventID)
        
        #self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,'td')))
        #_deleted = self.myPyDriver.find_elements_by_xpath(self.span_contains_start+str(_eventID)+self.contains_end)
        #assert the event with the specified id no longer exists in the grid
        #self.assertTrue(len(_deleted) == 0)
        return super(PythonSpaceRunnerEventsUnitTests, self).__init__(methodName)

    #TODO: FIX
    def test_EventsColumnManager(self,methodName = 'test_EventsColumnManager'):
        self.className_IconEvents = self.myPyDriver.find_element_by_class_name(self.className_IconEvents)
        self.className_IconEvents.click()
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.manageColumnsButtonXpath))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.listItemModelXpath)))
        source_element = self.myPyDriver.find_element_by_xpath(self.listItemModelXpath)
        dest_element = self.myPyDriver.find_element_by_xpath(self.columnManager_available)
        self.action.drag_and_drop(source_element, dest_element).perform()
        time.sleep(1)
        #assert Model is in available fields column
        self.assertTrue(len(self.myPyDriver.find_elements_by_xpath(self.columnManager_available_model))==1)
        self.myPyDriver.find_element_by_name(self.name_submitButton).click()
        time.sleep(2)
        #assert Model is no longer displayed
        self.assertFalse(self.myPyDriver.find_element_by_xpath(self.a_contains_Model_Xpath).is_displayed())
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.css_headerButton))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.listItemModelXpath)))
        source_element = self.myPyDriver.find_element_by_xpath(self.listItemModelXpath)
        dest_element = self.myPyDriver.find_element_by_xpath(self.columnManager_selected)
        #drag Model back
        action_chains.ActionChains(self.myPyDriver).drag_and_drop(source_element, dest_element).perform()
        time.sleep(2)
        #assert Model is in selected fields column
        self.assertTrue(len(self.myPyDriver.find_elements_by_xpath(self.columnManager_selected_model))==1)
        self.myPyDriver.find_element_by_name(self.name_submitButton).click()
        time.sleep(1)
        #assert User Status is displayed again
        self.assertTrue(self.myPyDriver.find_element_by_xpath(self.a_contains_Model_Xpath).is_displayed())
        return super(PythonSpaceRunnerEventsUnitTests, self).__init__(methodName)
    
    #TODO: FIX
    def test_EventsDragColumns(self,methodName = 'test_EventsDragColumns'):
        self.className_IconEvents = self.myPyDriver.find_element_by_class_name(self.className_IconEvents)
        self.className_IconEvents.click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.a_contains_Event_ID)))
        _eventIDHeader = self.myPyDriver.find_element_by_xpath(self.a_contains_Event_ID)
        _statusHeader = self.myPyDriver.find_element_by_xpath(self.a_contains_Status)
        #get initial array of table headers
        _table = self.myPyDriver.find_elements_by_xpath(self.eventGridTableHeaderXpath)
        _tableHeaders = []
        for th in _table:
            title = str(th.get_attribute("data-title"))
            _tableHeaders.append(title)
        #initial index of headers
        _eIndex = _tableHeaders.index("Event ID")
        _sIndex = _tableHeaders.index("Status")
        #drag status to the front of the grid
        self.action.drag_and_drop(_statusHeader, _eventIDHeader).perform()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.a_contains_Event_ID)))
        #get the new array of table headers
        _table = self.myPyDriver.find_elements_by_xpath(self.eventGridTableHeaderXpath)
        _upTableHeaders = []
        for th in _table:
            title = th.get_attribute("data-title")
            _upTableHeaders.append(title)
        #verify that status is now at index 0 and event id's index has increased by 1
        self.assertTrue(_upTableHeaders.index("Status") == 0)
        self.assertTrue(_upTableHeaders.index("Event ID") == (_eIndex + 1))
        return super(PythonSpaceRunnerEventsUnitTests, self).__init__(methodName)
        
    #Average time: 22 seconds
    #Precondition: 
    #TODO: 
    #Status: ✔
    def test_EventsExport(self, methodName = "test_EventsExport"):
        path = self.downloads_path
        init_num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
        time.sleep(2)
        self.className_IconEvents = self.myPyDriver.find_element_by_class_name(self.className_IconEvents)
        time.sleep(1)
        #click export button from events grid
        self.className_IconEvents.click()
        time.sleep(2)
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.exportButtonXpath))).click()
        time.sleep(2)
        #######system dialog handler########
        #PyAutoGuiExporter.PyAutoGuiExporter()
        ####################################
        #verify increase in # of files in 'path' by 1
        post_num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
        self.assertTrue((post_num_files - init_num_files) == 1)
        return super(PythonSpaceRunnerEventsUnitTests, self).__init__(methodName)


    #TODO :  
    #Average time:  368 seconds (dependant on which columns are present)
    #Precondition: 
    #notes: glitch with textbar is workaround by refreshing webpage after every column 
    #Status: 
    def test_filterByColumn(self,methodName= 'test_filterByColumn'):
        time.sleep(2)
        #self.myPyDriver.find_element_by_class_name(self.iconXyiconClassName).click()
        self.myPyDriver.find_element_by_class_name(self.className_IconEvents).click()
        #self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,'td')))
        time.sleep(3)


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
            intFields = ["Xyicon ID", "Event ID"]
            dateFields = ["Event Date"] 
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
                              
            #self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
            self.myPyDriver.find_element_by_class_name(self.className_IconEvents).click()
            self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,'td')))
           #Call class depending on which filterType is needed (norm, int, or date) 
            if(filterText in intFields):
                Int_Filter.Int_Filter(_intFilter, self.columnLists[col], self.myPyDriver, self.wait)
            elif("Date" in type or filterText in dateFields):
                Date_Filter.Date_Filter(_dateFilter, self.columnLists[col], self.myPyDriver, self.wait)
            else:
                Norm_Filter.Norm_Filter(_normalFilter, self.columnLists[col], "Events", self.myPyDriver, self.wait)
         
        return super(PythonSpaceRunnerEventsUnitTests, self).__init__(methodName)

    #TODO : 
    #Average time: 33
    #Precondition: Model is included in selected fields column
    #Notes: preCondition can be eliminated once drag n drop function is established  
    #Status: 
    def test_EventSortByModel(self, methodName = 'test_EventSortByModel'):
        time.sleep(3)
        self.className_IconEvents = self.myPyDriver.find_element_by_class_name(self.className_IconEvents)
        self.className_IconEvents.click()
        time.sleep(2)
        _trXPath = self.xyiconGridRow
        _sortTab = self.a_contains_Model_Xpath      
        time.sleep(2)
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "td")))
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
        return super(PythonSpaceRunnerEventsUnitTests, self).__init__(methodName)
    
    def tearDown(self):
        #if(self.myPyDriver.title == "SpaceRunner"):
        #    self.signOutLink = self.myPyDriver.find_element_by_xpath(self.logoutLinkXPath)
        #    self.signOutLink.click()
        self.myPyDriver.quit()
        return super(PythonSpaceRunnerEventsUnitTests, self).tearDown()

if __name__ == '__main__':
    unittest.main()
