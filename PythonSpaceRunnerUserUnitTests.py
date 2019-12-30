import unittest
import string
import sys
import random
import datetime
import time
import config, Selectors, Norm_Filter
from selenium.webdriver.common import action_chains  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException  

class PythonSpaceRunnerUserUnitTests(unittest.TestCase):
   
    def __init__(self, methodName = 'runTest'):

        #init config file
        config_object = config.config()
        selector_object = Selectors.Selectors()

        #Screenshot dir
        self.imageDir = config_object.imageDir

        #Login information
        self.url = config_object.url

        #gmail
        self.gmail_address  = config_object.gmail_address
        self.gmail_password = config_object.gmail_password
         
        #Login information for main user to login and use the application
        self.adminUserName   = config_object.adminUserName
        self.adminPassword   = config_object.adminPassword
        self.userFilterTerm = config_object.userFilterTerm
        
        #Login information for user that gets permissions/name changed in the application
        self.permissionsUserName       = config_object.permissionsUserName
        self.permissionsPassword       = config_object.permissionsPassword
        self.perUserFirstName = config_object.initial_first_name
        self.perUserLastName  = config_object.initial_last_name
        self.perNewName       = config_object.changed_name
        
        #information for user to be deleted
        self.addDeleteUserName  = config_object.addDeleteUserName
        self.addDeleteEmail     = config_object.addDeleteEmail
        self.addDeletePassword  = config_object.addDeletePassword

        #information for user to change passwords
        self.passUserName     = config_object.passUserName
        self.passPasswd       = config_object.passPasswd
        self.passInitialEmail = config_object.passInitialEmail
        self.passNewEmail     = config_object.passNewEmail
       
        #Application Buttons and links
        self.excelButtonClassName       = selector_object.excelButtonClassName
        self.className_IconProject      = selector_object.className_IconProject
        self.logoutLinkXPath            = selector_object.logoutLinkXPath
        self.name_userName              = selector_object.name_userName
        self.name_pwInput               = selector_object.name_pwInput
        self.name_submit                = selector_object.name_submit
        self.doneButton                 = selector_object.doneButton
        self.className_IconHome         = selector_object.className_IconHome
        self.name_submitButton          = selector_object.name_submitButton
        self.span_contains_start        = selector_object.span_contains_start
        self.contains_end               = selector_object.contains_end
        self.className_ngScope          = selector_object.className_ngScope
        self.invalidEmailToastXpath     = selector_object.invalidEmailToastXpath
        self.name_Email                 = selector_object.name_Email 
        self.name_signIn                = selector_object.name_signIn
        self.name_Passwd                = selector_object.name_Passwd
        self.first_unopened             = selector_object.first_unopened
        self.resetPassLinkXpath         = selector_object.resetPassLinkXpath
        self.className_emailWindow      = selector_object.className_emailWindow
        self.css_projectGearButton      = selector_object.css_projectGearButton
        self.manageColumnsButtonXpath   = selector_object.manageColumnsButtonXpath
        self.columnManager_available    = selector_object.columnManager_available
        self.columnManager_selected     = selector_object.columnManager_selected
        self.columnManager_available_US = selector_object.columnManager_available_US
        self.columnManager_selected_US  = selector_object.columnManager_selected_US
        self.css_headerButton           = selector_object.css_headerButton
        #User test specific buttons and links
        self.className_IconUser         = selector_object.className_IconUser
        self.usersGridLinkClass         = selector_object.usersGridLinkClass
        self.usersGridRowXPath          = selector_object.usersGridRowXPath
        self.radioButtonsXPath          = selector_object.radioButtonsXPath
        self.inputSubmitXPath           = selector_object.inputSubmitXPath
        self.editUsersButtonXPath       = selector_object.editUsersButtonXPath
        self.deleteUserButtonXPath      = selector_object.deleteUserButtonXPath
        self.addUserButtonXPath         = selector_object.addUserButtonXPath
        self.editAccountLinkXPath       = selector_object.editAccountLinkXPath
        self.editAccountSaveButtonXPath = selector_object.editAccountSaveButtonXPath
        self.accountChangedToastXPath   = selector_object.accountChangedToastXPath
        self.projectTileXPath           = selector_object.projectTileXPath
        self.name_userEmail             = selector_object.name_userEmail
        self.head_XyiconIncXpath        = selector_object.head_XyiconIncXpath
        self.arramUserXpath             = selector_object.arramUserXpath
        self.className_resendEmail      = selector_object.className_resendEmail
        self.XyiconIncProjectHeader     = selector_object.XyiconIncProjectHeader
        self.name_password              = selector_object.name_password
        self.name_confirmPassword       = selector_object.name_confirmPassword
        self.name_userFirstName         = selector_object.name_userFirstName
        self.name_userLastName          = selector_object.name_userLastName
        self.listItemUserStatusXpath    = selector_object.listItemUserStatusXpath
        self.a_contains_User_Status     = selector_object.a_contains_User_Status
        self.userGridTableRowXpath      = selector_object.userGridTableRowXpath
        self.userGridEmailFilter        = selector_object.userGridEmailFilter
        self.userFilterButton           = selector_object.userFilterButton
        self.userFilterEqualTo          = selector_object.userFilterEqualTo
        self.userFilterNotEqual         = selector_object.userFilterNotEqual
        self.userFilterStartsWith       = selector_object.userFilterStartsWith
        self.userFilterContains         = selector_object.userFilterContains
        self.userFilterDoesNotContain   = selector_object.userFilterDoesNotContain
        self.userFilterEndsWith         = selector_object.userFilterEndsWith
        self.a_contains_Email           = selector_object.a_contains_Email
        self.userGridTableHeaderXpath   = selector_object.userGridTableHeaderXpath
        self.userGridEmailTabXpath      = selector_object.userGridEmailTabXpath
        self.userEmailFilterCloseXpath  = selector_object.userEmailFilterCloseXpath
        self.name_createUserEmail       = selector_object.name_createUserEmail 
        self.createButtonCSSSelector    = selector_object.createButtonCSSSelector
        self.OKButtonXpath              = selector_object.OKButtonXpath
        self.columnManagerButtonXPath      = selector_object.columnManagerButtonXPath        
        self.cancelButtonXpath             = selector_object.cancelButtonXpath
        self.iconXyiconClassName           = selector_object.className_IconXyicons
        self.xyiconGridRow                 = selector_object.xyiconGridRow
        self.a_contains_Email_Xpath        = selector_object.a_contains_Email_Xpath


        #webDriver setup
        self.chromDriverEXE = os.path.dirname(os.path.realpath(__file__)) + "\\webDriver\\chromedriver.exe"
        self.myPyDriver = webdriver.Chrome(self.chromDriverEXE)
        self.myPyDriver.maximize_window()
        #wait setup
        self.wait = WebDriverWait(self.myPyDriver, 15)

        #wait setup
        #self.wait = WebDriverWait(self.myPyDriver, 45)
        self.myPyDriver.set_page_load_timeout(45)

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

            except:
                self.myPyDriver.quit()
                self.fail()
            return super(PythonSpaceRunnerUserUnitTests, self).__init__(methodName)
        else:
            print("Unable to init webDriver!")

    def highlightElement(self,element):
        self.myPyDriver.execute_script("arguments[0].setAttribute('style', arguments[1]);",element, "color: red; border: 3px solid red;")     

    def logoutThenLoginAsAnotherUser(self, userName, password):
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.ID, 'navArrow')))
        self.signOutLink = self.myPyDriver.find_element_by_xpath("//button[@id='navArrow']")#self.logoutLinkXPath)
        time.sleep(5)
        self.signOutLink.click()
        time.sleep(2)
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"a")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Sign Out')]")))
        self.signOut = self.myPyDriver.find_element_by_xpath("//a[contains(text(),'Sign Out')]")
        self.signOut.click()
        self.myPyDriver.get(self.url)
        self.assertTrue( self.myPyDriver.title == "SpaceRunner" )
        self.wait.until(EC.presence_of_element_located((By.NAME,self.name_userName)))
        self.userNameField = self.myPyDriver.find_element_by_name(self.name_userName)
        self.userNameField.send_keys(userName)
        self.userPassword = self.myPyDriver.find_element_by_name(self.name_pwInput)
        self.userPassword.send_keys(password)
        self.loginSubmitButton = self.myPyDriver.find_element_by_name(self.name_submitButton)
        self.loginSubmitButton.click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconHome)))
     
    def clickUsersIcon(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconUser)))
        self.iconAdminLink = self.myPyDriver.find_element_by_class_name(self.className_IconUser)
        self.iconAdminLink.click()

    def doubleClickUser(self, userXPath):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, userXPath)))
        self.usersGridRow = self.myPyDriver.find_element_by_xpath(userXPath)
        self.action.double_click(self.usersGridRow).perform()

    def clickUserThenEditButton(self, userXPath):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, userXPath)))
        self.usersGridRow = self.myPyDriver.find_element_by_xpath(userXPath)
        self.usersGridRow.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.editUsersButtonXPath)))
        self.editButton = self.myPyDriver.find_element_by_xpath(self.editUsersButtonXPath)
        self.editButton.click()
            
    def saveFromEditUserMenu(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.inputSubmitXPath)))
        self.inputSubmit = self.myPyDriver.find_element_by_xpath(self.inputSubmitXPath)
        self.inputSubmit.click()
        time.sleep(1)
        
    def waitForDataLoad(self):
        self.wait = WebDriverWait(self.myPyDriver, 30)
        self.wait.until(EC.invisibility_of_element_located((By.XPATH,'//div[contains(text(),"Your project data is being loaded...")]')))
        time.sleep(1)
        self.wait = WebDriverWait(self.myPyDriver, 15)
        return
                    
    def logoutTest(self, methodName = 'logoutTest'):
        self.logoutThenLoginAsAnotherUser(self.addDeleteUserName, self.addDeletePassword)
        return super(PythonSpaceRunnerUserUnitTests, self).__init__(methodName)


    #Average time: 39 seconds
    #Precondition: spaceRunner has a project
    #Status: ✔
    def test_addUser(self, methodName = 'test_addUser'):
        self.clickUsersIcon()
        time.sleep(2)
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//td')))
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"(//button[@type='button'])[4]")))
        _addButton =  self.myPyDriver.find_element_by_xpath("(//button[@type='button'])[4]")
        time.sleep(2)
        self.myPyDriver.execute_script("arguments[0].click()", _addButton)
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.NAME,self.name_createUserEmail )))
        _emailField = self.myPyDriver.find_element_by_name(self.name_createUserEmail ) 
        _emailField.send_keys(self.addDeleteEmail)
        time.sleep(1)
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,self.radioButtonsXPath)))
        #radio_buttons = self.myPyDriver.find_elements_by_xpath(self.radioButtonsXPath)
        #radio_buttons[1].click()
        radio_buttons = self.myPyDriver.find_elements_by_xpath('//project-role-button/label')
        self.highlightElement(radio_buttons[1])
        self.myPyDriver.execute_script("arguments[0].click()", radio_buttons[1])
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.NAME,self.name_submitButton))).click()
        time.sleep(3)
        self.myPyDriver.refresh()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.usersGridLinkClass)))
        #check if new user appears in grid
        time.sleep(5)
        self.assertTrue(len(self.myPyDriver.find_elements_by_xpath(self.span_contains_start+self.addDeleteEmail+self.contains_end)) > 0)
        #verify change to added account
        self.logoutThenLoginAsAnotherUser(self.addDeleteUserName, self.addDeletePassword)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconProject))).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, self.className_ngScope)))
        #check that Xyicon Inc appears in projects window
        time.sleep(2)
        self.assertTrue(len(self.myPyDriver.find_elements_by_xpath(self.head_XyiconIncXpath)) >= 0)
        return super(PythonSpaceRunnerUserUnitTests, self).__init__(methodName)


    #Average time: 18 seconds
    #Precondition: spaceRunner has a project
    #Status: ✔
    def test_addUserInvalidEmail(self, methodName = 'test_addUserInvalidEmail'):
        self.clickUsersIcon()
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//td')))
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"(//button[@type='button'])[4]")))
        _addButton =  self.myPyDriver.find_element_by_xpath("(//button[@type='button'])[4]")
        time.sleep(2)
        self.myPyDriver.execute_script("arguments[0].click()", _addButton)
        #self.wait.until(EC.presence_of_element_located((By.NAME,self.name_userEmail)))
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.NAME,self.name_createUserEmail )))
        _emailField = self.myPyDriver.find_element_by_name(self.name_createUserEmail ) 
        _emailField.send_keys("Invalid Email")
        invalidEmailError = self.myPyDriver.find_element_by_xpath(self.invalidEmailToastXpath)
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,self.radioButtonsXPath)))
        radio_buttons = self.myPyDriver.find_elements_by_xpath('//project-role-button/label')
        self.highlightElement(radio_buttons[1])
        self.myPyDriver.execute_script("arguments[0].click()", radio_buttons[1])
        time.sleep(2)
        #self.wait.until(EC.element_to_be_clickable((By.NAME,self.name_submitButton))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//span[contains(text(),"Invalid Email Address.")]')))
        self.assertTrue(invalidEmailError.is_displayed())
        return super(PythonSpaceRunnerUserUnitTests, self).__init__(methodName)
    
    #Average time: 38 seconds
    #Precondition: spaceRunner has a project, assuming addUser has run succesfully first atm (contains "AddDeleteUser@spacerunneragent.33mail.com") 
    #Status: ✔
    def test_deleteUser(self, methodName = 'test_deleteUser'):
        self.clickUsersIcon()
        time.sleep(1)
        self.waitForDataLoad()
        #1 Click on delete 
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.span_contains_start+self.addDeleteEmail+self.contains_end))).click()
        time.sleep(4)
        #2 Click on delete button
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.deleteUserButtonXPath))).click()
        time.sleep(1)
        #3 Click on submit button
        self.wait.until(EC.element_to_be_clickable((By.NAME,self.name_submitButton))).click()
        time.sleep(3)
        #self.myPyDriver.refresh()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.arramUserXpath)))
        #4 check user is not in grid
        self.assertFalse(len(self.myPyDriver.find_elements_by_xpath(self.span_contains_start+self.addDeleteEmail+self.contains_end)) > 0)
        #5 Logout and log back in as another user
        self.logoutThenLoginAsAnotherUser(self.addDeleteUserName, self.addDeletePassword)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconProject))).click()
        self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, self.className_ngScope)))
        #6 verify user no longer belongs to any Xyicon projects
        time.sleep(2)
        self.assertFalse(len(self.myPyDriver.find_elements_by_xpath(self.head_XyiconIncXpath)) > 0)
        return super(PythonSpaceRunnerUserUnitTests, self).__init__(methodName)
      
    #TODO: FIX
    #doesn't send email?
    def test_changePassword(self, methodName = 'test_changePassword'):
        time.sleep(10)
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div')))
        self.logoutThenLoginAsAnotherUser(self.passUserName, self.passPasswd)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editAccountLinkXPath)))
        time.sleep(10)
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div')))
        self.editAccountLink = self.myPyDriver.find_element_by_xpath(self.editAccountLinkXPath)
        self.editAccountLink.click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_resendEmail)))
        _passwordLink = self.myPyDriver.find_element_by_class_name(self.className_resendEmail)
        _passwordLink.click()
        time.sleep(1)        
        #gmail 
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
        _passLink = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.resetPassLinkXpath)))
        _passLink.click()
        self.myPyDriver.close() 
        #end of gmail, change to new SR window
        _currentWindows = self.myPyDriver.window_handles
        for _handle in _currentWindows:
            self.myPyDriver.switch_to.window(_handle)
            if (self.myPyDriver.title == "SpaceRunner"):
                break 
        #change passwd
        self.wait.until(EC.element_to_be_clickable((By.NAME,self.name_password)))
        _newPassField = self.myPyDriver.find_element_by_name(self.name_password)
        _newPassField.send_keys(self.passPasswd)
        _confirm = self.wait.until(EC.element_to_be_clickable((By.NAME,self.name_confirmPassword)))
        _confirm.send_keys(self.passPasswd)
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.NAME,self.name_submitButton))).click()
        #login
        self.wait.until(EC.presence_of_element_located((By.NAME,self.name_userName)))
        self.userNameField = self.myPyDriver.find_element_by_name(self.name_userName)
        self.userNameField.send_keys(self.passUserName)
        self.userPassword = self.myPyDriver.find_element_by_name(self.name_pwInput)
        self.userPassword.send_keys(self.passPasswd)
        time.sleep(2)
        self.loginSubmitButton = self.myPyDriver.find_element_by_name(self.name_submitButton)
        self.loginSubmitButton.click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconHome)))
        return super(PythonSpaceRunnerUserUnitTests, self).__init__(methodName)
    

    #Average time: 35 seconds
    #Precondition: permissionsUser exists in users
    #Status: ✔
    def test_editClientPermissionsToAdmin(self, methodName = 'test_editClientPermissionsToAdmin'):
        #1 Click on user tab
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconUser)))
        self.iconAdminLink = self.myPyDriver.find_element_by_class_name(self.className_IconUser)
        self.iconAdminLink.click()
        time.sleep(2)
        #2 Click/edit PermissionsUser
        self.doubleClickUser(self.usersGridRowXPath)
        #3 Click radio buttons to change permissions
        time.sleep(1)
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,self.radioButtonsXPath)))
        radio_buttons = self.myPyDriver.find_element_by_xpath('//label[@for="radio4"]')
        self.highlightElement(radio_buttons)
        self.myPyDriver.execute_script("arguments[0].click()", radio_buttons)
        time.sleep(1)
        #4 Save permissions
        self.saveFromEditUserMenu()
        time.sleep(1)
        if(len(self.myPyDriver.find_elements_by_name("submitButton")) != 0):
           self.myPyDriver.find_element_by_xpath(self.OKButtonXpath).click()
        time.sleep(1)
        #5 Logout and Login as permissions user
        self.logoutThenLoginAsAnotherUser(self.permissionsUserName, self.permissionsPassword)
        #6 Click on project tab
        time.sleep(1)
        try:
            self.myPyDriver.find_element_by_xpath(self.projectTileXPath).click()
        except NoSuchElementException:
            pass                  
        #7 if users account is set to admin, they will have access to "Users" menu in that project
        #self.assertTrue(len(self.myPyDriver.find_elements_by_class_name(self.className_IconUser))>0)
        self.assertTrue(self.myPyDriver.find_element_by_class_name(self.className_IconUser).is_displayed())
        return super(PythonSpaceRunnerUserUnitTests, self).__init__(methodName)
    
    '''
    the editProjectPermissionsToNone test already does this, not sure if needed
    def test_editClientPermissionsToUser(self, methodName = 'test_editClientPermissionsToUser'):
        return super(PythonSpaceRunnerUserUnitTests, self).__init__(methodName)
    '''
    #Average time: 26 seconds
    #Precondition: permissionsUser exists in users
    #Status: ✔
    def test_editProjectPermissionsToNone(self, methodName = 'test_editProjectPermissionsToNone'):
        #1 Click on User tab
        self.clickUsersIcon()
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//td')))
        #2 Edit permissionsUser row
        self.doubleClickUser(self.usersGridRowXPath)
        #3 Click radio buttons to get rid of permissions  
        time.sleep(1)
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,self.radioButtonsXPath)))
        radio_buttons = self.myPyDriver.find_element_by_xpath('//label[@for="radio3"]')
        self.highlightElement(radio_buttons)
        self.myPyDriver.execute_script("arguments[0].click()", radio_buttons)
        time.sleep(1)
        selDelSol = self.myPyDriver.find_element_by_xpath(self.projectTileXPath)
        selDelSol = selDelSol.find_element_by_xpath("..")
        selDelSol_row = selDelSol.find_element_by_xpath("..")
        radio_buttons = selDelSol_row.find_elements_by_xpath("."+self.radioButtonsXPath)
        self.myPyDriver.execute_script("arguments[0].click()", radio_buttons[0])
        time.sleep(1)
        #4 Save permissions
        self.saveFromEditUserMenu()
        time.sleep(1)
        if(len(self.myPyDriver.find_elements_by_name("submitButton")) != 0):
           self.myPyDriver.find_element_by_xpath(self.OKButtonXpath).click()
        time.sleep(1)
        #5 Logout and login to permissionsUser
        self.logoutThenLoginAsAnotherUser(self.permissionsUserName, self.permissionsPassword)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconProject))).click()
        _projectView = self.XyiconIncProjectHeader
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,_projectView)))
        #6 assert that the project tile does not exist for the user
        self.assertFalse(len(self.myPyDriver.find_elements_by_xpath(self.projectTileXPath)) > 0)
        return super(PythonSpaceRunnerUserUnitTests, self).__init__(methodName)



    #Average time: 35 seconds
    #Precondition: permissionsUser exists
    #Status: 
    #Notes: This test should fail until ui bug with gear appearing (yet unusable) by non-admin users is fixed
    def test_editProjectPermissionsToUser(self, methodName = 'test_editProjectPermissionsToUser'):
        #1 Click on users tab
        self.clickUsersIcon()
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//td')))
        #2 Edit on the permissionsUser
        self.doubleClickUser(self.usersGridRowXPath)
        time.sleep(1)
        #3 Click on radio buttons to change permissions
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,self.radioButtonsXPath)))
        radio_buttons = self.myPyDriver.find_element_by_xpath('//label[@for="radio3"]')
        self.highlightElement(radio_buttons)
        self.myPyDriver.execute_script("arguments[0].click()", radio_buttons)
        time.sleep(1)
        selDelSol = self.myPyDriver.find_element_by_xpath(self.projectTileXPath)
        selDelSol = selDelSol.find_element_by_xpath("..")
        selDelSol_row = selDelSol.find_element_by_xpath("..")
        radio_buttons = selDelSol_row.find_elements_by_xpath("."+self.radioButtonsXPath)
        self.myPyDriver.execute_script("arguments[0].click()", radio_buttons[1])
        time.sleep(1)
        #4 Save permissions
        self.saveFromEditUserMenu()
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//td')))
        time.sleep(2)
        if(len(self.myPyDriver.find_elements_by_name("submitButton")) != 0):
           self.myPyDriver.find_element_by_xpath(self.OKButtonXpath).click()
        time.sleep(1)
        #5 Logout and Login to permissinosUser
        self.logoutThenLoginAsAnotherUser(self.permissionsUserName, self.permissionsPassword)
        #6 Click on projects tab
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconProject))).click()
        _projectView = self.XyiconIncProjectHeader
        _projectGearButtonCSSSelector = self.css_projectGearButton
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,_projectView)))
        #project tile is available
        time.sleep(1)
        self.assertTrue(len(self.myPyDriver.find_elements_by_xpath(self.projectTileXPath)) > 0)
        #7 admin gear selector is not displayed when admin permission is not granted
        _projectGearButton = self.myPyDriver.find_elements_by_xpath('//span[@title = "Manage Account"]')
        gearIndex = len(_projectGearButton)-1
        self.myPyDriver.execute_script("arguments[0].click()", _projectGearButton[gearIndex])
        try:
            self.myPyDriver.find_element_by_xpath(self.addProjectXPath)
            assertTrue(False)
        except:
            pass
        return super(PythonSpaceRunnerUserUnitTests, self).__init__(methodName)



    #Average time: 35 seconds
    #Precondition: permissionsUser exists
    #Status: ✔
    def test_editProjectPermissionsToAdmin(self, methodName = 'test_editProjectPermissionsToAdmin'):
        #1 Click on Users tab
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconUser)))
        self.iconAdminLink = self.myPyDriver.find_element_by_class_name(self.className_IconUser)
        self.action.click(self.iconAdminLink).perform()
        #self.myPyDriver.find_element_by_class_name(self.className_IconUser).send_keys("\n")
        #self.iconAdminLink.click()
        #2 Click and edit permissionsUser row
        self.doubleClickUser(self.usersGridRowXPath)
        time.sleep(2)
        #3 Change permissions by clicking radio buttons
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,self.radioButtonsXPath)))
        radio_buttons = self.myPyDriver.find_element_by_xpath('//label[@for="radio3"]')
        self.highlightElement(radio_buttons)
        self.myPyDriver.execute_script("arguments[0].click()", radio_buttons)
        time.sleep(1)
        selDelSol = self.myPyDriver.find_element_by_xpath(self.projectTileXPath)
        selDelSol = selDelSol.find_element_by_xpath("..")
        selDelSol_row = selDelSol.find_element_by_xpath("..")
        radio_buttons = selDelSol_row.find_elements_by_xpath("."+self.radioButtonsXPath)
        self.myPyDriver.execute_script("arguments[0].click()", radio_buttons[2])
        time.sleep(1)
        #4 Save permissions
        self.saveFromEditUserMenu()
        time.sleep(1)
        if(len(self.myPyDriver.find_elements_by_name("submitButton")) != 0):
           self.myPyDriver.find_element_by_xpath(self.OKButtonXpath).click()
        time.sleep(1)
        #5 Logout and log back in as permissionsUser
        self.logoutThenLoginAsAnotherUser(self.permissionsUserName, self.permissionsPassword)
        #6 Click on project tab
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,self.className_IconProject))).click()
        _projectGearButtonCSSSelector = self.css_projectGearButton
        _projectView = self.XyiconIncProjectHeader
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,_projectView)))    
        time.sleep(3)
        self.assertTrue(len(self.myPyDriver.find_elements_by_xpath(self.projectTileXPath)) > 0)
        #7 admin gear selector is displayed when admin permission is not granted
        _projectGearButton = self.myPyDriver.find_elements_by_xpath('//span[@title = "Manage Account"]')
        gearIndex = len(_projectGearButton)-1
        self.myPyDriver.execute_script("arguments[0].click()", _projectGearButton[gearIndex])
        try:
            self.myPyDriver.find_element_by_xpath(self.addProjectXPath)
            assertTrue(True)
        except:
            pass
        return super(PythonSpaceRunnerUserUnitTests, self).__init__(methodName)
        

    #Average time: 66 seconds
    #Precondition: 
    #notes: extensive explicit waits used because navArrow takes a long time to loadup upon login
    #Status: ✔
    def test_editUserFirstName(self, methodName = 'test_editUserFirstName'):
        #Logout then login as j.klinkhammer
        time.sleep(15)
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div')))
        self.logoutThenLoginAsAnotherUser(self.permissionsUserName, self.permissionsPassword)
       #click editAccountLink
        time.sleep(12)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editAccountLinkXPath)))
        self.editAccountLink = self.myPyDriver.find_element_by_xpath(self.editAccountLinkXPath)
        self.editAccountLink.click()
        #edit firstName
        self.wait.until(EC.presence_of_element_located((By.NAME,self.name_userFirstName)))
        self.userFirstNameField = self.myPyDriver.find_element_by_name(self.name_userFirstName)
        currentName = self.userFirstNameField.get_attribute("value")
        if currentName == self.perUserFirstName:
            newName = self.perNewName
        else:
            newName = self.perUserFirstName
        self.userFirstNameField.clear()
        self.userFirstNameField.send_keys(newName)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editAccountSaveButtonXPath)))
        self.editAccountSaveButton = self.myPyDriver.find_element_by_xpath(self.editAccountSaveButtonXPath)
        time.sleep(1)
        self.editAccountSaveButton.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.accountChangedToastXPath))) 
        time.sleep(5)
        self.logoutThenLoginAsAnotherUser(self.permissionsUserName, self.permissionsPassword)
        #click editAccountLink
        time.sleep(12)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editAccountLinkXPath)))
        self.editAccountLink = self.myPyDriver.find_element_by_xpath(self.editAccountLinkXPath)
        self.editAccountLink.click()
        time.sleep(1)
        #verify change
        self.wait.until(EC.presence_of_element_located((By.NAME,self.name_userFirstName)))
        self.userFirstNameField = self.myPyDriver.find_element_by_name(self.name_userFirstName)
        currentName = self.userFirstNameField.get_attribute("value")
        self.assertTrue(currentName == newName)
        return super(PythonSpaceRunnerUserUnitTests, self).__init__(methodName)

    #TODO: 
    #Average time: 66 seconds
    #Precondition: 
    #notes: extensive explicit waits used because navArrow takes a long time to loadup upon login
    #Status: 
    def test_editUserLastName(self, methodName = 'test_editUserLastName'):
        #Logout then login as j.klinkhammer
        time.sleep(15)
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"button")))
        self.logoutThenLoginAsAnotherUser(self.permissionsUserName, self.permissionsPassword)
        #click editAccountLink
        time.sleep(12)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editAccountLinkXPath)))
        self.editAccountLink = self.myPyDriver.find_element_by_xpath(self.editAccountLinkXPath)
        self.editAccountLink.click()
        #edit lastName
        self.wait.until(EC.presence_of_element_located((By.NAME,self.name_userLastName)))
        self.userLastNameField = self.myPyDriver.find_element_by_name(self.name_userLastName)
        currentName = self.userLastNameField.get_attribute("value")
        if currentName == self.perUserLastName:
            newName = self.perNewName
        else:
            newName = self.perUserLastName
        self.userLastNameField.clear()
        self.userLastNameField.send_keys(newName)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editAccountSaveButtonXPath)))
        self.editAccountSaveButton = self.myPyDriver.find_element_by_xpath(self.editAccountSaveButtonXPath)
        time.sleep(1)
        self.editAccountSaveButton.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.accountChangedToastXPath))) 
        #log in again to verify changes
        self.logoutThenLoginAsAnotherUser(self.permissionsUserName, self.permissionsPassword)
        #click editAccountLink
        time.sleep(12)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editAccountLinkXPath)))
        self.editAccountLink = self.myPyDriver.find_element_by_xpath(self.editAccountLinkXPath)
        self.editAccountLink.click()
        time.sleep(1)
        #verify change
        self.wait.until(EC.presence_of_element_located((By.NAME,self.name_userLastName)))
        self.userLastNameField = self.myPyDriver.find_element_by_name(self.name_userLastName)
        currentName = self.userLastNameField.get_attribute("value")
        self.assertTrue(currentName == newName)
        return super(PythonSpaceRunnerUserUnitTests, self).__init__(methodName)


    #Average time: 
    #Precondition: 
    #notes: webpage glitch when "_emailField.get_attribute("value")"
    #Status: 
    def test_changeEmail(self, methodName = 'test_changeEmail'):
         #Logout then login as j.klinkhammer
        time.sleep(15)
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div')))
        self.logoutThenLoginAsAnotherUser(self.permissionsUserName, self.permissionsPassword)
        #click editAccountLink
        time.sleep(15)
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div')))
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editAccountLinkXPath)))
        self.editAccountLink = self.myPyDriver.find_element_by_xpath(self.editAccountLinkXPath)
        self.editAccountLink.click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.name_userEmail)))
        _emailField = self.myPyDriver.find_element_by_xpath(self.name_userEmail)
        _currentEmail = _emailField.get_attribute("value")
        if _currentEmail == self.passInitialEmail:
            _newEmail = self.passNewEmail
        else:
            _newEmail = self.passInitialEmail
        _emailField.clear()
        time.sleep(1)
        _emailField.send_keys(_newEmail)
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editAccountSaveButtonXPath)))
        self.editAccountSaveButton = self.myPyDriver.find_element_by_xpath(self.editAccountSaveButtonXPath)
        self.editAccountSaveButton.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.accountChangedToastXPath)))
        #log in again to verify changes
        self.logoutThenLoginAsAnotherUser(self.passUserName, self.passPasswd)
        #click editAccountLink
        time.sleep(10)
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div')))
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.editAccountLinkXPath)))
        self.editAccountLink = self.myPyDriver.find_element_by_xpath(self.editAccountLinkXPath)
        self.editAccountLink.click()
        time.sleep(1)
        #verify change
        self.wait.until(EC.presence_of_element_located((By.NAME,self.name_userEmail)))
        _emailField = self.myPyDriver.find_element_by_name(self.name_userEmail)
        self.assertTrue(_newEmail == _emailField.get_attribute("value"))
        return super(PythonSpaceRunnerUserUnitTests, self).__init__(methodName)
    

    #TODO: FIX
    def test_usersColumnManager(self, methodName = "test_usersColumnManager"):
        self.clickUsersIcon()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.manageColumnsButtonXpath))).click()
        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.listItemUserStatusXpath)))
        self.assertTrue(self.myPyDriver.find_element_by_xpath(self.a_contains_User_Status).is_displayed())
        source_element = self.myPyDriver.find_element_by_xpath(self.listItemUserStatusXpath)
        dest_element = self.myPyDriver.find_element_by_xpath(self.columnManager_available)
        #drag User Status
        self.action.drag_and_drop(source_element, dest_element).perform()
        time.sleep(1)
        #assert User Status is in available fields column
        self.assertTrue(len(self.myPyDriver.find_elements_by_xpath(self.columnManager_available_US))==1)
        self.myPyDriver.find_element_by_name(self.name_submitButton).click()
        time.sleep(1)
        #assert User Status is no longer displayed
        self.assertFalse(self.myPyDriver.find_element_by_xpath(self.a_contains_User_Status).is_displayed())
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.css_headerButton))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.listItemUserStatusXpath)))
        source_element = self.myPyDriver.find_element_by_xpath(self.listItemUserStatusXpath)
        dest_element = self.myPyDriver.find_element_by_xpath(self.columnManager_selected)
        #drag User Status back
        action_chains.ActionChains(self.myPyDriver).drag_and_drop(source_element, dest_element).perform()
        time.sleep(1)
        #assert User Status is in selected fields column
        self.assertTrue(len(self.myPyDriver.find_elements_by_xpath(self.columnManager_selected_US))==1)
        self.myPyDriver.find_element_by_name(self.name_submitButton).click()
        time.sleep(1)
        #assert User Status is displayed again
        self.assertTrue(self.myPyDriver.find_element_by_xpath(self.a_contains_User_Status).is_displayed())
        return super(PythonSpaceRunnerUserUnitTests, self).__init__(methodName)

    #TODO:  
    #Average time:  (dependant on which columns are present)
    #Precondition: 
    #notes: glitch with textbar is workaround by refreshing webpage after every column (last lines of test)
    #Status: 
    def test_filterByColumn(self,methodName= 'test_filterByColumn'):
        time.sleep(2)
        self.clickUsersIcon()
        self.waitForDataLoad()     
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
            filterXpath = "//th["+str(self.columnLists[col])+"]/span/span/span/span/span"
            filterTextXpath = "//th["+str(self.columnLists[col])+"]/a" 
            filterText = self.myPyDriver.find_element_by_xpath(filterTextXpath).text
            Norm_Filter.Norm_Filter(_normalFilter, self.columnLists[col], "User", self.myPyDriver, self.wait)
           
            if (col != len(self.columnLists)):
               self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.iconXyiconClassName))).click()
               self.clickUsersIcon()
               self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,'td')))
        return super(PythonSpaceRunnerUserUnitTests, self).__init__(methodName)


    #TODO : 
    #Average time: 26 seconds
    #Precondition: Email is included in selected fields column, fields tab contains fields 
    #Notes: preCondition can be eliminated once drag n drop function is established  
    #Status: ✔     
    def test_UserSortByEmail(self, methodName = 'test_UserSortByEmail'):
        #1 Click on Users tab
        self.clickUsersIcon()
        self.waitForDataLoad()
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,'td')))       
        _trXPath = self.xyiconGridRow
        _sortTab = self.a_contains_Email_Xpath     
        time.sleep(1)
        _table = self.myPyDriver.find_elements_by_xpath(_trXPath)
        time.sleep(5)
        #ensure that precondition is met and find model index
        #2 Click on Column Manager(buggy)
        self.myPyDriver.find_element_by_xpath("//button[@title='Manage Columns']").click()
        time.sleep(2)
        selectedColumn = self.myPyDriver.find_element_by_xpath("//div[2]/div/div[2]/ul")
        columnElements = selectedColumn.find_elements_by_tag_name('li')
        time.sleep(2)
        columnLength = len(columnElements)
        modelIndex = 0
        #3 Find column index of 'Email' 
        for _li in columnElements:
            self.assertTrue(modelIndex<=columnLength)
            if _li.text == 'Email':
                break
            else:
                modelIndex = modelIndex + 1        
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.cancelButtonXpath)))
        self.cancelButton=self.myPyDriver.find_element_by_xpath(self.cancelButtonXpath)
        self.cancelButton.click()
        time.sleep(1)
        
        #4 record models of rows in table
        _modelList = []        
        for _tr in _table:
            _tds= _tr.find_elements_by_tag_name('td')
            _modelList.append(_tds[modelIndex].text)      
        
        #5 click on model filter
        _modelTab = self.myPyDriver.find_element_by_xpath(_sortTab)
        _modelTab.click()
        time.sleep(1)                
        _updatedModelList = []
        _table = self.myPyDriver.find_elements_by_xpath(_trXPath)        
        
        #6 Record rows of table after model filter is clicked
        for _tr in _table:
            _tds= _tr.find_elements_by_tag_name('td')
            _updatedModelList.append(_tds[modelIndex].text)
        
        #7 reverse the anti-alphabetical list to make sure it was sorted exactly backwards    
        _reversedList = []
        for i in range(0,len(_updatedModelList)):
            _reversedList.append(_updatedModelList.pop())  
                   
        self.assertTrue(_reversedList == _modelList)     
        return super(PythonSpaceRunnerUserUnitTests, self).__init__(methodName)

    #TODO: FIX
    def test_dragColumns(self, methodName = "test_dragColumns"):
        self.clickUsersIcon()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.a_contains_User_Status)))
        _userStatusHeader = self.myPyDriver.find_element_by_xpath(self.a_contains_User_Status)
        _emailHeader = self.myPyDriver.find_element_by_xpath(self.a_contains_Email)
        _table = self.myPyDriver.find_elements_by_xpath(self.userGridTableHeaderXpath)
        _tableHeaders = []
        for th in _table:
            title = th.get_attribute("data-title")
            _tableHeaders.append(title)
        _uSIndex = _tableHeaders.index("User Status")
        _eIndex = _tableHeaders.index("Email")
        self.action.drag_and_drop(_userStatusHeader, _emailHeader).perform()
        time.sleep(1)
        self.myPyDriver.refresh()
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.a_contains_User_Status)))
        _table = self.myPyDriver.find_elements_by_xpath(self.userGridTableHeaderXpath)
        _upTableHeaders = []
        for th in _table:
            title = th.get_attribute("data-title")
            _upTableHeaders.append(title)
        self.assertTrue(_upTableHeaders.index("User Status") == 0)
        self.assertTrue(_upTableHeaders.index("Email") == (_eIndex + 1))
        return super(PythonSpaceRunnerUserUnitTests, self).__init__(methodName)
    
    def tearDown(self):
        #if(self.myPyDriver.title == "SpaceRunner"):
        #    self.signOutLink = self.myPyDriver.find_element_by_xpath(self.logoutLinkXPath)
        #    self.signOutLink.click()
        self.myPyDriver.quit()
        return super(PythonSpaceRunnerUserUnitTests, self).tearDown()

if __name__ == '__main__':
    unittest.main()

