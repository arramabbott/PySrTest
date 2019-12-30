import unittest, config, Selectors
import string
import sys
import random
import datetime
import time
from selenium.webdriver.common import action_chains  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PythonSpaceRunnerProjectsUnitTest(unittest.TestCase):

    def __init__(self, methodName = 'runTest'):

        #init config and Selector objects
        config_object       = config.config()
        selectors_object    = Selectors.Selectors()

        #Screenshot dir
        self.imageDir       = config_object.imageDir

        #Login information
        self.url            = config_object.url
        self.adminUserName   = config_object.adminUserName
        self.adminPassword   = config_object.adminPassword

        #Application Buttons and links
        self.excelButtonClassName           = selectors_object.excelButtonClassName
        self.eventsButtonClassName          = selectors_object.eventsButtonClassName
        self.className_IconProject          = selectors_object.className_IconProject
        self.catalogLinkClass               = selectors_object.className_IconCatalog
        self.catalogGridLinkClass           = selectors_object.catalogGridLinkClass
        self.catalogGridRowXPath            = selectors_object.catalogGridRowXPath
        self.logoutLinkXPath                = selectors_object.logoutLinkXPath
        self.projectsLinkClassName          = selectors_object.projectsLinkClassName
        self.projectTileXPath               = selectors_object.projectTileXPath
        self.projectSubmitButtonName        = selectors_object.projectSubmitButtonName
        self.projectSubmitButtonCSSSelector = selectors_object.projectSubmitButtonCSSSelector
        self.projectNameFieldXPath          = selectors_object.projectNameFieldXPath
        self.projectNameEditFieldXPath      = selectors_object.projectNameEditFieldXPath
        self.editTileXPath                  = selectors_object.editTileXPath
        self.deleteTileXPath                = selectors_object.deleteTileXPath
        self.projectDeleteButtonXPath       = selectors_object.projectDeleteButtonXPath
        self.projectEditButtonXPath         = selectors_object.projectEditButtonXPath
        self.name_userName                  = selectors_object.name_userName
        self.name_pwInput                   = selectors_object.name_pwInput
        self.name_submit                    = selectors_object.name_submit
        self.name_submitButton              = selectors_object.name_submitButton
        self.doneButton                     = selectors_object.doneButton #close walk-me window
        self.projectGearButtonCSSSelector   = selectors_object.projectGearButtonCSSSelector
        self.addProjectXPath                = selectors_object.addProjectXPath
        self.projectGalleryHeaderClassName  = selectors_object.projectGalleryHeaderClassName
        self.spacesHeaderXPath              = selectors_object.spacesHeaderXPath


        self.westOfficeXpath                = selectors_object.westOfficeXpath
        self.eastOfficeXpath                = selectors_object.eastOfficeXpath
        self.newProjectName                 = "West Office - " + self.random_string()
        self.validSaveTileXPath             = '//div/h5[contains(text(),"'+self.newProjectName+'")]'

        self.chromDriverEXE = os.path.dirname(os.path.realpath(__file__)) + "\\webDriver\\chromedriver.exe"
        self.myPyDriver = webdriver.Chrome(self.chromDriverEXE)
        self.myPyDriver.maximize_window()

        #wait setup
        self.wait = WebDriverWait(self.myPyDriver,45)
        
        #init Action chains
        self.action = action_chains.ActionChains(self.myPyDriver)

        #set the browser to max window size
        self.myPyDriver.maximize_window()

        #init time stamp 
        self.now = datetime.datetime.now()
        self.date = self.now.strftime('%H%M%S_%m%d%y')

        if self.myPyDriver:
            try:
                self.myPyDriver.get(self.url)
                self.assertTrue(self.myPyDriver.title == "SpaceRunner")
                self.wait.until(EC.presence_of_element_located((By.NAME,self.name_userName)))
                self.userNameField = self.myPyDriver.find_element_by_name(self.name_userName)
                self.userNameField.send_keys(self.adminUserName)
                self.userPassword = self.myPyDriver.find_element_by_name(self.name_pwInput)
                self.userPassword.send_keys(self.adminPassword)
                self.loginSubmitButton = self.myPyDriver.find_element_by_name(self.name_submitButton)
                self.loginSubmitButton.click()
                #self.wait.until(EC.element_to_be_clickable((By.XPATH,self.doneButton))).click()
                self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconProject)))
                self.selectProjectModule = self.myPyDriver.find_element_by_class_name(self.projectsLinkClassName)
                self.selectProjectModule.click()
                self.wait.until(EC.presence_of_element_located((By.XPATH,self.projectTileXPath)))
            except:
                self.myPyDriver.quit()
                self.fail()
            return super(PythonSpaceRunnerProjectsUnitTest, self).__init__(methodName)
        else:
            print("Unable to init webDriver!")

    def random_string(self):
        range = random.randint(6,12)
        randomString = ''.join([random.choice(string.ascii_letters +string.digits) for n in xrange(range)])
        return randomString
            
    def highlightElement(self,element):
        self.myPyDriver.execute_script("arguments[0].setAttribute('style', arguments[1]);",element, "color: red; border: 3px solid red;")
    
    def test_SelectProjects(self, methodName = 'test_SelectProjects'):
        _projectTile  = self.myPyDriver.find_element_by_xpath(self.projectTileXPath)
        _projectTile.click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,self.projectGalleryHeaderClassName)))
        self.assertTrue(len(self.myPyDriver.find_elements_by_xpath(self.spacesHeaderXPath))>0)
        return super(PythonSpaceRunnerProjectsUnitTest, self).__init__(methodName)

    #TODO :  
    #Average time: 19
    #Precondition: 
    #Status: 
    def test_AddProjects(self, methodName = 'test_AddProjects'):
        #TODO : Finish AddProject test - Add ID to Gear Dom element
        time.sleep(2)
        preTiles = self.myPyDriver.find_elements_by_xpath(self.westOfficeXpath)
        _projectGearButton = self.myPyDriver.find_elements_by_xpath('//span[@title = "Manage Account"]')
        gearIndex = len(_projectGearButton)-1
        self.myPyDriver.execute_script("arguments[0].click()", _projectGearButton[gearIndex])
        time.sleep(2)
        #self.wait.until(EC.presence_of_element_located((By.XPATH,self.addProjectXPath)))
        _addProject = self.myPyDriver.find_element_by_xpath(self.addProjectXPath)
        _addProject.click()
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.projectNameFieldXPath)))
        _projectNameField = self.myPyDriver.find_element_by_xpath(self.projectNameFieldXPath )
        _projectNameField.send_keys(self.newProjectName)
        _projectSubmitButton = self.myPyDriver.find_element_by_name(self.projectSubmitButtonName)
        _projectSubmitButton.click()
        time.sleep(3)
        postTiles = self.myPyDriver.find_elements_by_xpath(self.westOfficeXpath)
        self.assertTrue((len(postTiles)-len(preTiles)) == 1)
        #self.assertTrue(len(self.myPyDriver.find_elements_by_xpath(self.validSaveTileXPath))>0)
        return super(PythonSpaceRunnerProjectsUnitTest, self).__init__(methodName)


    #TODO :  
    #Average time: 21
    #Precondition: tile list on projects page contains a "West Office"
    #Status: 
    def test_EditProject(self, methodName = 'test_EditProject'):
        _editProjectString = "East Office - " + self.random_string()
        preTiles = self.myPyDriver.find_elements_by_xpath(self.eastOfficeXpath)
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.editTileXPath)))
        _projectToEdit = self.myPyDriver.find_element_by_xpath(self.editTileXPath)
        #self.highlightElement(_projectToEdit)
        _projectContainer = _projectToEdit.find_element_by_xpath("..")
        #self.highlightElement(_projectContainer)
        _projectEditButton = _projectContainer.find_element_by_xpath(self.projectEditButtonXPath)
        #self.highlightElement(_projectEditButton)
        self.myPyDriver.execute_script("arguments[0].click()", _projectEditButton)
        
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.projectNameEditFieldXPath)))
        _projectNameField = self.myPyDriver.find_element_by_xpath(self.projectNameEditFieldXPath)
        _projectNameFieldValueOld = _projectNameField.get_attribute('value')
        _projectNameField.clear()
        _projectNameField.send_keys(_editProjectString)
        _projectNameFieldValueNew = _projectNameField.get_attribute('value')
        self.assertTrue(_projectNameFieldValueOld != _projectNameFieldValueNew)
        self.projectSubmitbutton = self.myPyDriver.find_element_by_css_selector(self.projectSubmitButtonCSSSelector)
        self.projectSubmitbutton.click()
        time.sleep(5)
        postTiles = self.myPyDriver.find_elements_by_xpath(self.eastOfficeXpath)
        self.assertTrue((len(postTiles)-len(preTiles)) == 1)
        return super(PythonSpaceRunnerProjectsUnitTest, self).__init__(methodName)


    #TODO :  
    #Average time: 20
    #Precondition: tile list on projects page contains a "West Office"
    #Status: 
    def test_DeleteProjects(self, methodName = 'test_DeleteProjects'):
        #self.wait.until(EC.presence_of_element_located((By.XPATH,self.deleteTileXPath)))
        _projectToDelete = self.myPyDriver.find_element_by_xpath(self.deleteTileXPath)
        #self.highlightElement(_projectToDelete)
        _projectTitle = _projectToDelete.text
        _projectContainer = _projectToDelete.find_element_by_xpath("..")
        #self.highlightElement(_projectContainer)
        _projectDeleteButton = _projectContainer.find_element_by_xpath(self.projectDeleteButtonXPath)
        #self.highlightElement(_projectDeleteButton)
        self.myPyDriver.execute_script("arguments[0].click()", _projectDeleteButton)
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.NAME,self.projectSubmitButtonName)))
        _submitButton = self.myPyDriver.find_element_by_name(self.projectSubmitButtonName)
        _submitButton.click()
        time.sleep(5)
        self.assertTrue(len(self.myPyDriver.find_elements_by_xpath('//div/h5[contains(text(),"'+_projectTitle+'")]'))==0)
        return super(PythonSpaceRunnerProjectsUnitTest, self).__init__(methodName)

    def tearDown(self):
        #self.signOutLink = self.myPyDriver.find_element_by_xpath(self.logoutLinkXPath)
        #self.signOutLink.click()
        self.myPyDriver.quit()
        return super(PythonSpaceRunnerProjectsUnitTest, self).tearDown()

if __name__ == '__main__':
    unittest.main()
