import unittest, config, Selectors
import string
import sys
import random
import datetime
import time
import os
import platform
from selenium.webdriver.common import action_chains  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import PyAutoGuiExporter

class PythonSpaceRunnerSpacesUnitTest(unittest.TestCase):

    def __init__(self, methodName = 'runTest'):
        
        #init config  and selectors object
        config_object       = config.config()
        selector_object    = Selectors.Selectors()
        
        #system info
        self.system_info    = config_object.system_info
        self.downloads_path = config_object.downloads_path
        self.pdf_dir        = config_object.pdf_dir
        
        #Screenshot dir
        self.imageDir        = config_object.imageDir
        self.windows_scr_dir = config_object.win_scrn_dir
        self.linux_scr_dir   = config_object.lin_scrn_dir
        self.pdf             = config_object.new_pdf
        self.cancel_button   = config_object.cancel_button
        
        #Login information
        self.url            = config_object.url
        self.adminUserName   = config_object.adminUserName
        self.adminPassword   = config_object.adminPassword 

        #Application Buttons and links
        self.excelButtonClassName  = selector_object.excelButtonClassName
        self.eventsButtonClassName = selector_object.className_IconEvents
        self.catalogLinkClass      = selector_object.className_IconCatalog
        self.logoutLinkXPath       = selector_object.logoutLinkXPath
        self.name_userName         = selector_object.name_userName
        self.name_pwInput          = selector_object.name_pwInput
        self.name_submit           = selector_object.name_submit
        self.doneButton            = selector_object.doneButton
        self.className_IconHome    = selector_object.className_IconHome
        self.galleryTileXpath      = selector_object.galleryTileXpath
        self.name_submitButton     = selector_object.name_submitButton

        #Spaces selectors
        self.className_IconSpaces  = selector_object.className_IconSpaces
        self.createButtonXpath     = selector_object.createButtonXpath
        self.id_dropZone           = selector_object.id_dropZone
        self.drawingWindowXpath    = selector_object.drawingWindowXpath
        self.id_drawingName        = selector_object.id_drawingName
        self.id_drawingNotes       = selector_object.id_drawingNotes
        self.spacesSaveButtonXpath = selector_object.spacesSaveButtonXpath
        self.pElementContainsStart = selector_object.pElementContainsStart
        self.contains_end          = selector_object.contains_end
        self.id_drawEdit           = selector_object.id_drawEdit
        self.id_drawDelete         = selector_object.id_drawDelete
        self.id_drawingNotes       = selector_object.id_drawingNotes
        self.id_drawingEditNotes   = selector_object.id_drawingEditNotes
        self.testProjectXpath      = selector_object.testProjectXpath
        self.id_drawingEditName    = selector_object.id_drawingEditName
        self.spaceXpath            = selector_object.spaceXpath
        self.catalogItemXpath      = selector_object.catalogItemXpath
        self.pdfExportButtonXpath  = selector_object.pdfExportButtonXpath
        self.EXPORTbuttonXpath     = selector_object.EXPORTbuttonXpath
        

        #webDriver setup
        self.chromDriverEXE = os.path.dirname(os.path.realpath(__file__)) + "\\webDriver\\chromedriver.exe"

        #self.chromDriverEXE = "C:\\chromedriver_win32\\chromedriver.exe"
        self.myPyDriver = webdriver.Chrome(self.chromDriverEXE)
        #self.myPyDriver = webdriver.Firefox()
        
        #wait setup
        self.wait = WebDriverWait(self.myPyDriver, 45)
        
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
                self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconHome)))
                _spacesLink = self.myPyDriver.find_element_by_class_name(self.className_IconSpaces)
                _spacesLink.click()
            except:
                self.myPyDriver.quit()
                self.fail()
            return super(PythonSpaceRunnerSpacesUnitTest, self).__init__(methodName)
        else:
            print("Unable to init webDriver!")

    def random_string(self):
        range = random.randint(6,12)
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
        
    def goToFilterProject(self):
        time.sleep(2)
        self.selectProjectModule = self.myPyDriver.find_element_by_class_name(self.className_IconProject)
        self.selectProjectModule.click()
        time.sleep(2)
        project = self.myPyDriver.find_element_by_xpath('//h5[contains(text(),"Office")]')
        project.click()
        time.sleep(3)

    #Average time: 
    #TODO: 
    #Notes: pyAutoGui.locate methods currently do not work due to the flashing UI of windows buttons
    #Status:            
    def test_AddSpaces(self, methodName = 'teC:\Users\Tbrochard\Dost_AddSpaces'):
        spaceName = "test" + " - " + self.random_string()       
        time.sleep(3)
        createButton = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.createButtonXpath)))
        createButton.click()
        #self.wait.until(EC.element_located_to_be_selected((By.CLASS_NAME,"walkme-action-destroy-1"))).click()
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.ID, self.id_dropZone)))
        #click dropzone
        dz = self.myPyDriver.find_element_by_id(self.id_dropZone)
        dz.click()
        #pyautogui for system dialog
        time.sleep(5)
        cwd = os.getcwd()
        pdf_path = os.path.join(cwd,self.pdf_dir,self.pdf)
        pyautogui.typewrite(pdf_path)
        if self.system_info == "Windows":
            cancel_file_path = os.path.join(self.windows_scr_dir,self.cancel_button)
            open_location = pyautogui.locateOnScreen(cancel_file_path, grayscale=False)
            buttonx, buttony = pyautogui.center(open_location)           
            pyautogui.click(buttonx-100, buttony)
        if self.system_info == "Linux":
            pass #TODO: add linux screenshots + directory
        time.sleep(10)
        
        #click drawing
        drawingWindowXPath = self.drawingWindowXpath
        self.wait.until(EC.visibility_of_element_located((By.XPATH,drawingWindowXPath)))
        darwingWindow = self.myPyDriver.find_element_by_xpath(drawingWindowXPath).click()
        #fill fields
        time.sleep(2)
        #change xyicon size via + and -
        self.wait.until(EC.element_to_be_clickable((By.ID,self.id_drawingName)))
        drawingName = self.myPyDriver.find_element_by_id(self.id_drawingName)
        self.wait.until(EC.element_to_be_clickable((By.ID,self.id_drawingNotes)))
        drawingNotes = self.myPyDriver.find_element_by_id(self.id_drawingNotes)
        drawingName.send_keys(spaceName)
        drawingNotes.send_keys("added")
        #test back button 
        #save
        time.sleep(1)
        self.myPyDriver.find_element_by_xpath(self.spacesSaveButtonXpath).click()
        time.sleep(1)
        projectXPath = self.pElementContainsStart+spaceName+self.contains_end
        self.wait.until(EC.element_to_be_clickable((By.XPATH,projectXPath)))
        projectTileList = self.myPyDriver.find_elements_by_class_name(self.galleryTileXpath)
        projectFound = False      
        for project in projectTileList:
            if (len(project.find_elements_by_xpath(projectXPath))>0):
                self.highlightElement(project)
                projectToEdit = project
                projectFound = True
                break
        if(projectFound == True): 
            self.assertTrue(True)
        else:
            self.assertFalse(True)
        #editButton = projectToEdit.find_element_by_id(self.id_drawEdit)
        #self.highlightElement(editButton)
        #editButton.click()
        #time.sleep(1)
        #self.wait.until(EC.element_to_be_clickable((By.ID,self.id_drawingEditNotes)))
        #spaceNotes = self.myPyDriver.find_element_by_id(self.id_drawingEditNotes)
        #self.assertTrue(spaceNotes.get_attribute('value') == 'added')
        return super(PythonSpaceRunnerSpacesUnitTest, self).__init__(methodName)



    #Average time: 11 seconds
    #TODO: 
    #Status: 
    def test_SelectSpaces(self, methodName = 'test_SelectSpaces'):
        spaceName = "test -"
        projectXPath = self.pElementContainsStart + spaceName + self.contains_end
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.galleryTileXpath)))
        projectTileList = self.myPyDriver.find_elements_by_class_name(self.galleryTileXpath)
        projectFound = False  
       
        for project in projectTileList:
            if (len(project.find_elements_by_xpath(projectXPath))>0):
                self.highlightElement(project)
                projectToSelect = project
                projectTitle = project.text 
                projectFound = True
                break
        time.sleep(2)
        if(projectFound==True):
            project.click()
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH,"//span")))
            time.sleep(2)
            testName = "//span[contains(text(),'"+str(projectTitle)+"')]"
           
            if(self.myPyDriver.find_element_by_xpath(testName)):
                self.assertTrue(True)  
            else:
                self.assertTrue(False)
        else:
            self.assertTrue(False)
        return super(PythonSpaceRunnerSpacesUnitTest, self).__init__(methodName)



    #Average time: 13 seconds
    #TODO: 
    #Status: 
    def test_ChangeSpaces(self, methodName = 'test_ChangeSpaces'):
        spaceName = "test -"
        projectXPath = self.pElementContainsStart + spaceName + self.contains_end
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.galleryTileXpath)))
        self.projectTileList = self.myPyDriver.find_elements_by_class_name(self.galleryTileXpath)
        firstProjectFound = False 
        projectLen = len(self.projectTileList)
        if projectLen > 1:            
            #find first tile & info
            self.highlightElement(self.projectTileList[0])
            self.firstProjectTitle = self.projectTileList[0].text 
            
            #click and check if it's the correct tile, or fail
            self.projectTileList[0].click()      
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH,"//span[contains(text(),'"+str(self.firstProjectTitle)+"')]")))
            if(self.myPyDriver.find_element_by_xpath("//span[contains(text(),'"+str(self.firstProjectTitle)+"')]")):
                self.assertTrue(True)  
            else:
                self.assertTrue(False)
            
           
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconSpaces))).click() 
            
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.galleryTileXpath)))
            self.secondProjectTileList = self.myPyDriver.find_elements_by_class_name(self.galleryTileXpath)
            
            secondTile = self.secondProjectTileList[1]       
            #find second tile & info
            self.highlightElement(secondTile)
            self.secondProjectTitle = self.secondProjectTileList[1].text 

            #click and check if it's the correct tile, or fail
            self.secondProjectTileList[1].click()                    
            self.wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'"+str(self.secondProjectTitle)+"')]")))
            if(self.myPyDriver.find_element_by_xpath("//span[contains(text(),'"+str(self.secondProjectTitle)+"')]")):
                self.assertTrue(True)  
            else:
                self.assertTrue(False)
        else:
            assertTrue(False)
        return super(PythonSpaceRunnerSpacesUnitTest, self).__init__(methodName)        


 
    
    #Average time: 15 seconds
    #TODO: 
    #Status:    
    def test_DeleteSpaces(self, methodName = 'test_DeleteSpaces'):
        spaceName = "test"
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconSpaces))).click()
        self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,self.galleryTileXpath)))
        projectTileList = self.myPyDriver.find_elements_by_class_name(self.galleryTileXpath)
        pNum = len(projectTileList)
        projectFound = False      
        for project in projectTileList:
            if (len(project.find_elements_by_xpath(self.pElementContainsStart+spaceName+self.contains_end))>0):
                projectToDelete = project
                projectFound = True
        if(projectFound == False): 
            self.assertTrue(False)
        self.highlightElement(projectToDelete)
        #js force click not necessary for firefox, but currently works in chrome driver
        deleteButton = projectToDelete.find_element_by_id(self.id_drawDelete)
        self.highlightElement(deleteButton)
        self.myPyDriver.execute_script("arguments[0].click()", deleteButton)
        self.wait.until(EC.element_to_be_clickable((By.NAME, self.name_submitButton))).click()
        time.sleep(5)
        self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,self.galleryTileXpath)))
        newPList = self.myPyDriver.find_elements_by_class_name(self.galleryTileXpath)
        newPNum = len(newPList)
        self.assertTrue((pNum - newPNum) == 1)
        return super(PythonSpaceRunnerSpacesUnitTest, self).__init__(methodName)



    #Average time: 13 seconds
    #TODO: 
    #Status: 
    def test_EditSpaces(self, methodName = 'test_EditSpaces'):
        spaceName = "test"
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconSpaces))).click()
        self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,self.galleryTileXpath)))
        #get test project
        projectTileList = self.myPyDriver.find_elements_by_class_name(self.galleryTileXpath)
        projectFound = False      
        for project in projectTileList:
            if (len(project.find_elements_by_xpath(self.pElementContainsStart+spaceName+self.contains_end))>0):
                self.highlightElement(project)
                projectToEdit = project
                projectFound = True
                break
        if(projectFound == False): 
            self.assertTrue(False)
        
        editButton = projectToEdit.find_element_by_id(self.id_drawEdit)
        self.highlightElement(editButton)
        #editButton.click()
        self.myPyDriver.execute_script("arguments[0].click()", editButton)
        #edit name and notes + save
        self.wait.until(EC.element_to_be_clickable((By.ID,self.id_drawingEditName)))
        spaceName = self.myPyDriver.find_element_by_id(self.id_drawingEditName)
        newName = "test" + " - " + self.random_string()
        spaceName.clear()
        spaceName.send_keys(newName)
        self.wait.until(EC.element_to_be_clickable((By.ID,self.id_drawingEditNotes)))
        spaceNotes = self.myPyDriver.find_element_by_id(self.id_drawingEditNotes)
        newNotes = self.random_string()
        spaceNotes.clear()
        spaceNotes.send_keys(newNotes)
        self.myPyDriver.find_element_by_name(self.name_submitButton).click()
        #get the project again
        time.sleep(2)
        self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,self.galleryTileXpath)))
        projectTileList = self.myPyDriver.find_elements_by_class_name(self.galleryTileXpath)
        projectFound = False      
        for project in projectTileList:
            if (len(project.find_elements_by_xpath(self.pElementContainsStart+newName+self.contains_end))>0):
                self.highlightElement(project)
                projectToEdit = project
                projectFound = True
                break
        if(projectFound == False): 
            self.assertTrue(False)
        editButton = projectToEdit.find_element_by_id(self.id_drawEdit)
        
        self.highlightElement(editButton)
        self.myPyDriver.execute_script("arguments[0].click()", editButton)
        self.wait.until(EC.element_to_be_clickable((By.ID,self.id_drawingEditName)))
        #verify that the fields have changed
        spaceName = self.myPyDriver.find_element_by_id(self.id_drawingEditName)
        spaceNotes = self.myPyDriver.find_element_by_id(self.id_drawingEditNotes)
        self.assertTrue(spaceName.get_attribute('value') == newName)
        self.assertTrue(spaceNotes.get_attribute('value') == newNotes)
        return super(PythonSpaceRunnerSpacesUnitTest, self).__init__(methodName)

    #Average time: 49 seconds
    #notes: (30 sec) time based solely on the wait time for the pdf to export
    #TODO: 
    #Status: 
    def test_ExportSpaces(self, methodName = 'test_ExportSpaces'):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconSpaces))).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.galleryTileXpath)))
        time.sleep(2)
        project = self.myPyDriver.find_elements_by_tag_name("img") #self.myPyDriver.find_element_by_xpath(self.spaceXpath)
        project[0].click()
        time.sleep(2)
        self.waitForDataLoad()
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,self.catalogItemXpath)))
        pdfExporter = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.pdfExportButtonXpath)))
        time.sleep(2)
        self.myPyDriver.execute_script("arguments[0].click()", pdfExporter)
        time.sleep(2)
        path = self.downloads_path
        init_num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.EXPORTbuttonXpath))).click()
        time.sleep(30)
        #######system dialog handler########
         #PyAutoGuiExporter.PyAutoGuiExporter()
        ####################################
        post_num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
        self.assertTrue((post_num_files - init_num_files) == 1)
        return super(PythonSpaceRunnerSpacesUnitTest, self).__init__(methodName)
    
    def tearDown(self):
        #self.signOutLink = self.myPyDriver.find_element_by_xpath(self.logoutLinkXPath)
        ##self.signOutLink.click()
        #self.navArrowID = "navArrow"
        #self.logoutID = "//ul[@id='droplistSub']/li[4]/a"
        #self.logoutXpath = "//button[contains(text(),'Sign Out')]"

        #navArrow = self.myPyDriver.find_element_by_id(self.navArrowID)
        #self.highlightElement(navArrow)
        #navArrow.click()
        #logoutButton = self.myPyDriver.find_element_by_id(self.logoutID) ##error is with argument info
        #self.highlightElement(logoutButton)
    
 
        self.myPyDriver.quit() 
        return super(PythonSpaceRunnerSpacesUnitTest, self).tearDown()

if __name__ == '__main__':
    unittest.main()
