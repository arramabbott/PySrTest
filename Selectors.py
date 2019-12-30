import random,string,config

class Selectors(object):
    """description of class"""
    def __init__(self):

        conf = config.config()
        
        #Navigation
        self.className_IconHome     = "icon-home"
        self.className_IconProject  = "icon-project"
        self.className_IconEvents   = "icon-events"
        self.className_IconSpaces   = "icon-spaces"
        self.className_IconXyicons  = "icon-xyicon"
        self.className_IconCatalog  = "icon-catalog"
        self.className_IconUser     = "icon-admin"
        self.className_IconSupport  = "icon-walkMe"
        self.className_IconFields   = "icon-fields"

        #Login
        self.name_userName          = "userName"
        self.name_pwInput           = "pwInput"
        self.name_submit            = "submit"
        self.name_submitButton      = "submitButton"

        #Common
        self.randomNumber          = random.randrange(1,10)
        self.randomLetter          = random.choice(string.ascii_letters)
        self.doneButton            = '//span[contains(text(),"Done")]' #to close walk me window
        self.id_navigator          = "navigator"
        self.logoutLinkXPath       = "//ul[@id='topNavBarLinks']/li[2]/a"
        self.downloadsPath         = 'C:\\Users\\jklinkhammer\\Downloads'
        self.exportAutoItPath      = "C:\\Users\\jklinkhammer\\Documents\\Visual Studio 2013\\Projects\\SpaceRunnerUnitTests\\PySPUnitTest\\AutoITScripts\\export.exe"
        self.editButtonXpath       = '//button[@title="Edit"]'
        self.deleteButtonXPath     = '//button[@title="Delete"]'
        self.editDeleteButtonXPath = '//button[contains(text(),"Delete")]'
        self.spaceDeleteButtonXPath= "//ul[@id='panel-header-buttons-list']/li[2]"
        self.deleteRightClickXPath = "//li[@id='deleteSelection']/span"
        self.exportButtonXpath     = '//button[@title="Export"]'
        self.okButtonXpath         = '//button[contains(text(),"Ok")]'
        self.OKButtonXpath         = '//button[contains(text(),"OK")]'
        self.className_ngScope     = "ng-scope"
        self.kendoGridClass        = 'k-grid-content'
        self.spaceXpath            = '//p[contains(text(),"'+conf.mainSpaceTitle+'")]'
        self.excelButtonClassName  = "k-i-excel"
        self.id_floorplan          = "floorplan"
        self.modelFilterFieldXPath = '//th[3]/a/span'
        self.gridFirstRow          = "//table[@role='grid']/tbody/tr[1]/td[3]/span"
        self.westOfficeXpath       = '//div/h5[contains(text(),"West Office")]'
        self.eastOfficeXpath       = '//div/h5[contains(text(),"East Office")]'
        
        #Catalog Selectors
        self.excelButtonClassName          = "k-i-excel"
        self.catalogLinkCSSSelector        = "li.icon-catalog"
        self.catalogGridLinkClass          = "k-grid-content"
        self.catalogGridRowXPath           = "//td[1]"       
        self.projectsLinkClassName         = "icon-project"
        self.createButtonCSSSelector       = "span.k-icon.k-i-create"
        self.catalogAddClassXPATH        = "//div[@id='catalog-left']/div/div/span/span/span[2]" 
        self.electricalSelectXpath         = '//li[contains(text(),"Electrical")]'
        self.iconSearchXPath               = "//div[@id='svgIconAutoComplete']/div/input"
        self.svgIconCSSSelector            = "#iconContainer > div > div > div.xySvgLayer2 > svg"
        self.IconColorXPath                = "//div[@id='colorPaletteHolder']/div/table/tbody/tr/td[" + str(self.randomNumber) + "]"
        self.spaceXPath                    = '//p[contains(text(),"'+conf.mainSpaceTitle+'")]'
        self.filterProjectXPath            = '//p[contains(text(),"'+conf.filterSpaceTitle+'")]'
        self.name_make                     = 'make'
        self.name_model                    = 'model'
        self.catalogHeaderXPath            = '//span/ng-binding[contains(text(),"Catalog")]'
        self.name_description              = 'description'
        self.name_iconText                 = 'iconText'
        self.td_span_xpath                 = '//td/span'
        self.td_span_contains_start        = '//td/span[contains(text(),"'
        self.span_contains_start           = '//span[contains(text(),"'
        self.tr_contains_start             = '//tr[contains(text(),"'
        self.contains_end                  = '")]'
        self.class_lightingXPath           = "//td/span[contains(text(),'Lighting')]"
        self.ui_saveButtonXpath            = "//ui-button-submit[@text='Save']"
        self.catalogItem12057_Xpath        = "//td/span[contains(text(),'12057')]"
        self.css_editCatalogTitle          = ".k-window-titlebar.k-header"
        self.css_deleteButton              = "span.k-icon.k-i-delete"
        self.css_okButton                  = "button.btn.btn-sm.btn-info.ng-binding"
        self.css_headerButton              = "button.headerButton"
        self.newCatalogItemXpath           = '//td/span[contains(text(),"New - ")]'
        self.cancelButtonXpath             = '//button[contains(text(),"Cancel")]' #'//ui-button[@text="Cancel"]'
        self.catalogCloneButtonXpath       = '//button[@title="Clone"]'
        self.catalogGridBodyXpath          = '//*[@id="catalogClientGrid"]/div[2]/div[1]/table/tbody/tr[1]'
        self.saveButtonXpath               = '//button[contains(text(),"Save")]'
        self.catEditSaveID                 = "catEditSav"
        self.catalog_exportButtonXpath     = "//button[@title = 'Export']"
        self.catalogGridTableHeaderXpath   = '//*[@id="catalogClientGrid"]/div[1]/div/table/thead/tr[1]/th'
        self.catalogGridTableRowXpath      =  '//*[@id="catalogClientGrid"]/div[2]/div[1]/table/tbody' #'//*[@id="catalogClientGrid"]/div[2]/div[1]/table/tbody/tr'
        self.a_contains_Class_Xpath        = '//a[contains(text(),"Class")]'
        self.a_contains_Model_Xpath        = '//a[contains(text(),"Model")]' 
        self.a_contains_Email_Xpath        = '//a[contains(text(),"Email")]'
        self.a_contains_EventID_Xpath      = '//a[contains(text(),"Event ID")]' 
        self.listItemModelXpath            = '//li[contains(text(), "Model")]'
        self.columnManager_available       = '//div[2]/div/div/ul'
        self.columnManager_selected        = '//div[2]/div/div[2]/ul'
        self.manageColumnsButtonXpath      = '//button[@title="Manage Columns"]'
        self.columnManager_available_model = '//div[2]/div/div/ul/li[contains(text(), "Model")]'
        self.columnManager_selected_model  = '//div[2]/div/div[2]/ul/li[contains(text(), "Model")]'
        self.catalogFilterModelXpath       = '//div[@id="catalogClientGrid"]/div/div/table/thead/tr[2]/th[3]/span/span/span/input'
        self.catalogModelFilterCloseXpath  = '//th[3]/span/span/button'
        self.catalogFilterButton           = '//div/span/span/span[2]' #'//th[3]/span/span/span[2]/span/span[2]/span'
        self.columnManagerButtonXPath      = "//div[@id='contentWrapper']/div/div/div/div/div/div/div/span/button"
        self.catalogFilterMenuXPath        = "//div[2]/div/ul/li"
        self.filterTextBar1XPath           = "//input[@type='text'][1]"
        #Default ports
        self.singlePort = '[{"Type":"Data","Group":"1","Label":"A","DisplayOrder":1}'
        self.twoPorts = '[{"Type":"Data","Group":"1","Label":"A","DisplayOrder":1},{"Type":"Data","Group":"1","Label":"B","DisplayOrder":2}'
        self.threePorts = '[{"Type":"Data","Group":"1","Label":"A","DisplayOrder":1},{"Type":"Data","Group":"1","Label":"B","DisplayOrder":2},{"Type":"Data","Group":"1","Label":"C","DisplayOrder":3}]'
        self.fourPorts = '[{"Type":"Data","Group":"1","Label":"A","DisplayOrder":1},{"Type":"Data","Group":"1","Label":"B","DisplayOrder":2},{"Type":"Data","Group":"1","Label":"C","DisplayOrder":3},{"Type":"Data","Group":"1","Label":"D","DisplayOrder":4}]'
        self.fourPortsOutcome = '[{"Type":"Data","Group":"1","Label":"A"},{"Type":"Data","Group":"1","Label":"B"},{"Type":"Data","Group":"1","Label":"C"},{"Type":"Data","Group":"1","Label":"D"}]'
        self.fourPortsSplit = '[{"Type":"Data","Group":"1","Label":"A","DisplayOrder":1},{"Type":"Data","Group":"1","Label":"B","DisplayOrder":2},{"Type":"Data","Group":"2","Label":"A","DisplayOrder":1},{"Type":"Data","Group":"2","Label":"B","DisplayOrder":2}]'
        self.sixPortsSplit = '[{"Type":"Data","Group":"1","Label":"A","DisplayOrder":1},{"Type":"Data","Group":"1","Label":"B","DisplayOrder":2},{"Type":"Data","Group":"1","Label":"C","DisplayOrder":3},{"Type":"Data","Group":"2","Label":"A","DisplayOrder":1},{"Type":"Data","Group":"2","Label":"B","DisplayOrder":2},{"Type":"Data","Group":"2","Label":"C","DisplayOrder":3}]'
        self.eightPortsSplit = '[{"Type":"Data","Group":"1","Label":"A","DisplayOrder":1},{"Type":"Data","Group":"1","Label":"B","DisplayOrder":2},{"Type":"Data","Group":"1","Label":"C","DisplayOrder":3},{"Type":"Data","Group":"1","Label":"D","DisplayOrder":4},{"Type":"Data","Group":"2","Label":"A","DisplayOrder":1},{"Type":"Data","Group":"2","Label":"B","DisplayOrder":2},{"Type":"Data","Group":"2","Label":"C","DisplayOrder":3},{"Type":"Data","Group":"2","Label":"D","DisplayOrder":4}]'

        #Events
        self.spacesHeaderXpath            = '//span/ng-binding[contains(text(),"Spaces")]'
        self.excelButtonClassName         = "k-i-excel"
        self.editEventGridRowXPath        = "//td[2]/span"
        self.spaceFloorPlanTileXPath      = "//p[contains(text(),'"+conf.mainSpaceTitle+"')]"
        self.spaceFloorPlanCSSSeletor     = "img.ng-isolate-scope"
        self.xyiconQuickEditXPath         = '//li[@id="liQuick"]'
        self.eventAddButtonXPath          = "//input[@value='+']"
        self.reportedByListSelectorXPath  = "//ul[@id='userCreatedBy_listbox']/li[3])[2]"
        self.editEventSpanXPath           = '//span[contains(text(),"Edit Event")]'
        self.name_issueDescription        = 'issueDescription'
        self.reportedByFieldXPath         = "//div[3]/div/span/span/span"
        self.assignedToFieldXPath         = "//div[2]/span/span/span"
        self.assignedToFieldCSSSelector   = 'span.k-input.ng-scope[1]'
        self.eventDateFieldID             = "issueDateCreated"
        self.editEvent_completedDateID    = "issueDateResolved"
        self.newEvent_completedDateID     = "DateResolved"
        self.eventUrgentCheckBoxXPath     = '//label[contains(text(),"Urgent")]'   #previously "//input[@id='option']"
        self.eventCompletedByXPath        = "//span[contains(text(),'Please select a user')]"
        self.eventSaveButtonXPath         = '//button[contains(text(),"Save")]' #"(//button[@name='submitButton'])[2]"
        self.eventCancelButtonXPath       = "//ui-button[@id='equipEditCan']/button"
        self.eventEditButton              = '//button[@title="Edit"]'
        self.assignedToBoxXPath           = "//ul[@id='userAssignedTo_listbox']"
        self.createdByBoxXPath            = "//ul[@id='userCreatedBy_listbox']"
        self.resolvedByBoxXPath           = "//ul[@id='userResolvedBy_listbox']"
        self.events_adminUserXpath        = ".//li[contains(text(),'"+conf.adminFullName+"')]" 
        self.events_gmailUserXpath        = ".//li[contains(text(),'"+conf.gmailUserFullName+"')]"   
        self.completedByUserXPath         = '//div[5]/div[2]/span/span/span[2]/span'
        self.eventEdit_saveXpath          = '//ui-button-submit[@id="EventCreateSave"]/button'
        self.css_CanvasFloorplan          = 'canvas#floorplan'
        self.eventGrid_firstItem          = '//*[@id="eventGrid"]/div[3]/div[1]/table/tbody/tr[1]'
        self.eventIDXpath                 = './/td/span'
        self.id_eventListItem             = "eventListItem"
        self.editEventsButtonXpath        = '//span[contains(text(),"Edit Events")]'
        self.eventRow1Xpath               = '//div[@class = "row event-row-1"]'
        self.childDivXpath                = './/div'
        self.subElementEventId            = './/label[contains(text(),"Event ID")]'
        self.subElementStrong             = './/strong'
        self.specialCaseDeleteButton      = '//div[7]/ui-button[2]/button'
        self.specialCaseOkButton          = '//div/div[2]/ui-button-submit/button'
        self.a_contains_Event_ID          = '//a[contains(text(),"Event ID")]'
        self.a_contains_Status            = '//a[contains(text(),"Status")]'
        self.eventGridTableHeaderXpath    = '//*[@id="eventGrid"]/div[2]/div/table/thead/tr[1]/th'
        self.eventGridTableRowXpath       = '//*[@id="eventGrid"]/div[3]/div[1]/table/tbody/tr'
        self.sortMenuButtonsXpath         = '//div[@class="k-list-container k-popup k-group k-reset k-state-border-up"]/ul/li'
        self.eventsFilterModelXpath       = '//input[@data-text-field = "Model"]'
        self.eventsFilterIDXpath          = '//span/span/span[1]/span/input[1]'
        self.eventsFilterButton           = '//th[5]/span/span/span[2]/span/span[2]/span'
        self.eventsModelFilterCloseXpath  = "//th[5]/span/span/button"
        #for form field verification (selected options)
        self.reportedByOptionXPath  = '//div/div[2]/form/div[3]/div[1]/span/span/span[1]'
        self.assignedToOptionXPath  = '//div/div[2]/form/div[3]/div[2]/span/span/span[1]'
        self.completedByOptionXPath = '//div/div[2]/form/div[5]/div[2]/span/span/span[1]'
        self.resolutionCostXPath    = '//*[@id="resolutionCost"]'

        #Email
        self.name_Email            = "Email"
        self.name_signIn           = "signIn"
        self.name_Passwd           = "Passwd"
        self.dt_contains           = '//dt[contains(text(),"'
        self.className_emailWindow = "UI"
        self.first_unopened        = '//div/div/span/b'
        self.resetPassLinkXpath    = '//a[contains(text(),"Reset your SpaceRunner password")]'
        
        #Spaces
        self.iconSpacesClassName    = "icon-spaces"
        self.createButtonXpath      = "//ui-button-icon[@id='btnAdd']/button" #'//button[@title="Create"]'
        self.id_dropZone            = "dropzone"
        self.drawingWindowXpath     = '//*[@id="uploadWizardContent"]/div[2]/div[2]/img'
        self.id_drawingName         = "drawingName"
        self.id_drawingNotes        = "drawingNotes"
        self.spacesSaveButtonXpath  = "//button[contains(text(),'SAVE')]"
        self.pElementContainsStart  = './/p[contains(text(),"'
        self.id_drawEdit            = "drawEdit"
        self.id_drawDelete          = "drawDelete"
        self.id_drawingEditNotes    = "drawingsEditNoteLabel"
        self.testProjectXpath       = './/p[contains(text(),"test")]'
        self.id_drawingEditName        = "drawingsEditNameLabel"
        self.pdfExportButtonXpath   = '//li[@title="PDF Export"]'
        self.EXPORTbuttonXpath      = '//button[contains(text(),"EXPORT")]'

        #Project
        self.eventsButtonClassName          = "icon-events"
        self.catalogLinkClass               = "icon-catalog"
        self.catalogGridLinkClass           = "k-grid-content"
        self.catalogGridRowXPath            = "//td[1]"
        self.projectsLinkClassName          = "icon-project"
        self.projectTileXPath               = "//div/h5[contains(text(),'"+conf.mainProjectTitle+"')]"
        self.projectSubmitButtonName        = "submitButton"
        self.projectSubmitButtonCSSSelector = 'button[name="submitButton"]'
        self.projectNameFieldXPath          = "//input[@id='projectCreateLabel']"
        self.projectNameEditFieldXPath      = "//input[@id='projectEditLabel']"
        self.editTileXPath                  = '//div/h5[contains(text(),"West Office - ")]'
        self.deleteTileXPath                = '//div/h5[contains(text(),"West Office - ")]'
        self.projectDeleteButtonXPath       = './/span[@title="Delete Project"]'
        self.projectEditButtonXPath         = './/span[@title="Edit Project"]'
        self.projectGearButtonCSSSelector   = "span.client-context-menu.manage-glyph"
        self.addProjectXPath                = "//li/span[contains(text(),'Add')]"
        self.projectGalleryHeaderClassName  = "grid-header"
        self.spacesHeaderXPath              = "//span[contains(text(),'Spaces : "+conf.mainProjectTitle+"')]"
        
        #Users
        self.usersGridLinkClass         = "k-grid-content"
        self.usersGridRowXPath          = '//span[contains(text(),"'+conf.permissionsUserEmail+'")]'
        self.radioButtonsXPath          = "//*[@type='radio']"
        self.inputSubmitXPath           = "//button[@name='submitButton']"
        self.editUsersButtonXPath       = "//*[@id='contentWrapper']/div/div/div/div/div/div/div[1]/span[2]/ui-button-icon/button/span"
        self.deleteUserButtonXPath      = "//*[@id='contentWrapper']/div/div/div/div/div/div/div[1]/span[2]/ui-button-icon[2]/button/span"
        self.addUserButtonXPath         = "//*[@id='contentWrapper']/div/div/div/div/div/div/div[1]/span[2]/ui-button-icon[3]/button/span"
        self.editAccountLinkXPath       = '//span[contains(text(),"Welcome,")]'
        self.editAccountSaveButtonXPath = '//button[contains(text(),"Save")]'
        self.accountChangedToastXPath   = '//div[contains(text(),"Your profile has been changed")]'
        self.name_createUserEmail       = "createUserEmail"
        self.name_userEmail             = '//input[@name="userEmail"]' #'//input[@type="email"]' #'//input[@name="userEmail"]'
        self.head_XyiconIncXpath        = '//h4[contains(text(),"'+conf.companyName+'")]'
        self.invalidEmailToastXpath     = '//span[contains(text(),"Invalid Email Address.")]'
        self.arramUserXpath             = '//span[contains(text(),"'+conf.adminEmail+'")]'
        self.className_resendEmail      = "resend-email-link"
        self.XyiconIncProjectHeader     = '//span[contains(text(),"'+conf.companyName+'")]'
        self.name_password              = "password"
        self.name_confirmPassword       = "confirmPassword"
        self.name_userFirstName         = "userFirstName"
        self.name_userLastName          = "userLastName"
        self.css_projectGearButton      = "span.client-context-menu.manage-glyph"
        self.listItemUserStatusXpath    = '//li[contains(text(), "User Status")]'
        self.a_contains_User_Status     = '//a[contains(text(),"User Status")]'
        self.columnManager_available_US = '//div[2]/div/div/ul/li[contains(text(), "User Status")]'
        self.columnManager_selected_US  = '//div[2]/div/div[2]/ul/li[contains(text(), "User Status")]'
        self.userGridTableRowXpath      = '//*[@id="userGrid"]/div[2]/div[1]/table/tbody/tr'
        self.userGridEmailFilter        = '//*[@id="userGrid"]/div[1]/div/table/thead/tr[2]/th[1]/span/span/span[1]/input'
        self.userFilterButton           = "span.k-icon.k-filter"
        self.userFilterEqualTo          = self.sortMenuButtonsXpath
        self.userFilterNotEqual         = self.sortMenuButtonsXpath + '[2]'
        self.userFilterStartsWith       = self.sortMenuButtonsXpath + '[3]'
        self.userFilterContains         = self.sortMenuButtonsXpath + '[4]'
        self.userFilterDoesNotContain   = self.sortMenuButtonsXpath + '[5]'
        self.userFilterEndsWith         = self.sortMenuButtonsXpath + '[6]'
        self.a_contains_Email           = '//a[contains(text(),"Email")]'
        self.userGridTableHeaderXpath   = '//*[@id="userGrid"]/div[1]/div/table/thead/tr[1]/th'
        self.userGridEmailTabXpath      = '//th[@data-title="Email"]'
        self.userEmailFilterCloseXpath  = '//div[@id="userGrid"]/div/div/table/thead/tr[2]/th/span/span/button'
        
        #Xyicons 
        self.galleryTileXpath            = "project-gallery-tile-content"
        self.catalogItemXpath            = "draggable-catalog-icon"
        self.xyiconSubmitXpath           = "//ui-button-submit[@id='equipEditSav']/button"
        self.xyiconGridRowXpath          = '//*[@id="equipmentGrid"]/div[2]/div[1]/table/tbody/tr'
        self.xyiconModelFilterXpath      = '//th[5]/span/span/span/input'
        self.xyiconFilterButtonXpath     = "//th[5]/span/span/span[2]/span/span[2]/span"
        self.xyiconModelFilterCloseXpath = '//div[@id="equipmentGrid"]/div/div/table/thead/tr[2]/th[5]/span/span/button'
        self.xyiconGridHeaderXpath       = '//*[@id="equipmentGrid"]/div[1]/div/table/thead/tr[1]/th'
        self.xyiconDepartmentHeader      = '//a[contains(text(),"Department")]'
        self.xyiconSpaceHeader           = '//a[contains(text(),"Space")]'
        self.xyiconForms                 = '//form[@name="formEquipmentEdit"]'
        self.xyiconFormInput             = './/div/input'
        self.xyiconFormNotes             = './/textarea'
        self.inServiceDatePicker         = '//input[@data-role="datepicker"]'
        

        #Xyicon Edit Page
        self.className_xyiconForms = "formEquipmentEdit"
        self.editorDepartmentId    = "xyiconDepartment"
        self.editorRoomId          = "xyiconRoom"
        self.editorNotesId         = "xyiconNotes"
        self.editorXyiconNameId    = "xyiconName"
        self.editorAssetTagId      = "xyiconAssetTag"
        self.editorSerialNumberId  = "xyiconSerialNumber"
        self.editorOwnerId         = "xyiconOwner"
        self.editorContactId       = "xyiconContact"
        self.editorPlacementId     = "xyiconPlacement"
        self.editorInServiceDateId = "xyiconInServiceDate"
        #self.xyiconGridRow         = '//*[@id="equipmentGrid"]/div[2]/div[1]/table/tbody/tr[1]'
        self.xyiconGridRow         = "//table[@role='grid']/tbody/tr"
        self.xyiconEditDeleteXpath = '//button[contains(text(),"Delete")]'
        self.editDateButtonXPath    = '//div/span[2]/span/span/span'
        self.selectDateXPath       = '//a[contains(text(),"13")]'
        self.notesFieldXPath       = '//textarea[@role="textbox"]'
        self.datePickerXPath       = '//input[@data-role="datepicker"]'
        self.xyiconSpaceEditSaveXPath= '//ui-button-submit[@id="equipEditSav"]/button'    
        self.filterTextBarXPath    = "//input[@type='text'][1]"
        self.filterTextBarXPath2   = "//input[@type='text'][2]"
        self.filterSubmitButtonXPath= "//div[2]/button"
        self.filterClearButtonXPath = '//button[contains(text(),"Clear")]'
        



        #walkMe
        self.walkMeCloseXXPath                      = "//div[@id='walkme-menu']/div"
        self.launchPadTabXPath                      = "//div[contains(text(), 'Launch Pad')]"
        self.helpTabXPath                           = "//div[contains(text(),'Help')]"
        self.walkMeSupport                          = 'icon-walkMe'
        self.WelcomToSpaceRunnerXPath               = "//div[contains(text(),'Welcome to SpaceRunner!')]"
        self.ExploreDataXPath                       = "//div[contains(text(),'Explore with Sample Data')]"
        self.LaunchWithOwnDataXPath                 = "//div[contains(text(),'Launch with Your Own Data')]"
        self.ExploreXyiconCatalogXPath              = "//div[contains(text(),'Explore the Xyicon Catalog')]"
        self.InviteNewMembersXPath                  = "//div[contains(text(),'Invite New Crew Members')]"
        self.WalkMeDoneButtonXPath                  = "//span[contains(text(),'Done')]"
        self.VideoPlayButtonXPath                   = "//button[@title='Play']"
        self.VideoPlayFullScreenButtonClassName     = ""
        self.buttonNextXPath                        = "//span[contains(text(),'Next')]"
        self.walkMeCloseButtonXPath                 = "//div[6]/div/div/div[2]/div/div"