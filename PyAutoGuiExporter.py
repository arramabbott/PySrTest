import config
import os
import pyautogui
import time
class PyAutoGuiExporter(object):
    def __init__(self, *args, **kwargs):
        conf        = config.config()
        system_info = conf.system_info
        win_dir     = conf.win_scrn_dir
        lin_dir     = conf.lin_scrn_dir
        ok_button   = conf.ok_button
        save_button = conf.save_radio_button
        #pyautogui replacing autoit script
        #get screenshots for OS
        if system_info == "Windows":
            save_file_path = os.path.join(win_dir,save_button)
            ok_file_path = os.path.join(win_dir,ok_button)
        if system_info == "Linux":
            save_file_path = os.path.join(lin_dir,save_button)
            ok_file_path = os.path.join(lin_dir,ok_button)
        #complete system dialog
        save_file_location = pyautogui.locateOnScreen(save_file_path, grayscale=True)
        buttonx, buttony = pyautogui.center(save_file_location)
        pyautogui.click(buttonx, buttony)
        ok_location = pyautogui.locateOnScreen(ok_file_path, grayscale=True)
        buttonx, buttony = pyautogui.center(ok_location)
        pyautogui.click(buttonx, buttony)
        time.sleep(5)
        return


