"""
Config file for the Python UnitTest
"""
import os,platform
#from azure.storage import BlobService
class config(object):

    def __init__(self):
        """
        Config setting for test go here
        """
        #system information/downloads path
        self.system_info = platform.uname()[0]
        cwd = os.getcwd()
        cwd = cwd.split(os.sep)
        if self.system_info == "Windows":
            dl_folder = os.path.join(cwd[1],cwd[2],'Downloads')
            path = "C:\\"+dl_folder
        if self.system_info == "Linux":
            dl_folder = os.path.join(cwd[0],cwd[1],'Downloads')
            path = dl_folder 
        self.downloads_path = path

        #pyautogui screenshot paths
        self.pdf_dir           = 'sample_pdf'
        self.win_scrn_dir      = 'pyautogui_screenshots_windows'
        self.lin_scrn_dir      = 'pyautogui_screenshots_linux'
        self.save_radio_button = 'save_file_radio.PNG'
        self.ok_button         = 'ok.PNG'
        self.cancel_button     = 'cancel.PNG'
        self.new_pdf           = 'sample.pdf'
        
        """
        Config for image blob env
        """
        self.blobAccountName = ""
        self.blobContainerName = ""
        self.blobAccountKey = ""

        """
        Config for Develop env
        """
 
        #SpaceRunner Test Environment info
        self.mainProjectTitle = ""
        self.mainSpaceTitle   = ""
        self.filterSpaceTitle = ""
        self.companyName      = ""
        
        #Screenshot dir
        self.imageDir = ""

        #Gmail account for checking email verifications
        #email address must be associated with the passUser
        self.gmail_address  = ""
        self.gmail_password = ""
        
        #Login information for main user (project owner) to login and use the application
        self.url            = ""
        self.adminUserName  = ""
        self.adminPassword  = ""
        self.adminEmail     = ""
        self.adminFullName  = ""
        self.userFilterTerm = "" 

        #Login information for user that has its permissions and first/last name changed in the application
        self.permissionsUserName  = ""
        self.permissionsPassword  = ""
        self.permissionsUserEmail = ""
        self.initial_first_name   = ""
        self.initial_last_name    = ""
        self.changed_name         = ""
        
        #information for user that is added and deleted from the project
        #email address can be anything, email verification not performed with this user.
        self.addDeleteUserName  = ""
        self.addDeleteEmail     = "" 
        self.addDeletePassword  = "" 

        #information for user that has its password and email changed.
        #email address must be either the gmail address or an alias of the gmail address
        self.passUserName       = ""
        self.passPasswd         = ""
        self.passInitialEmail   = ""
        self.passNewEmail       = ""
        self.gmailUserFullName  = ""
        

