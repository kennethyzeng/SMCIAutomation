#############################
#Author: Kenneth Zeng
#Date: 3/12/2022
#Purpose: AutoLog in WEB GUI; AUTO Power CYCLE; AUTO CLEAR EVENT LOg; AUTO Output Event Log
#############################

from selenium import webdriver

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import linecache
from selenium.webdriver import DesiredCapabilities

BMCIP = str("https://172.30.111.12/")
Name = str("ADMIN")
Pwd = str("ADMIN")
subString = "ERR_CERT_INVALID"

def WEBGUI_AutoLogin(URL, Name,Pwd):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')
    ##Method 1 to Hangle Certificate error 
    # options.add_argument('--allow-running-insecure-content')  ##handle certificate error
    # options.add_argument('--ignore-certificate-errors')  ##handle certificate error
    
    #Method 2 Create a desired capabilities object as a starting point.
    # capabilities = DesiredCapabilities.FIREFOX.copy()
    # capabilities['platform'] = "WINDOWS"
    # capabilities['version'] = "10"
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['acceptInsecureCerts'] = True
    
    #https://www.youtube.com/watch?v=e4H3W4YNFhQ

    # Provide the path of chromedriver present on your system.
    driver = webdriver.Chrome(executable_path="chromedriver",
                            chrome_options=options,
                            desired_capabilities=capabilities
                            )

    driver.set_window_size(1080,720)
    #print(URL + Name + Pwd)

    driver.get(URL)
    sleep(5)
            
    Username= driver.find_element_by_id('usrName')
    Username.send_keys(Name)
    sleep(2)

    Password= driver.find_element_by_id('pwd')
    Password.send_keys(Pwd)
    sleep(2)

    Login_Button =driver.find_element_by_xpath ('//button[text()="Login"]')   ##search Button with Login text
    sleep(2)
    Login_Button.click()
    
    
#######Power Cycle System#####
    Post_URL = BMCIP + "cgi/url_redirect.cgi?url_name=topmenu" 
    driver.get(Post_URL)
    sleep(10)
    # storing the current window handle to get back to dashboard
    #main_page = driver.current_window_handle

    power_Button= driver.find_element_by_id('powerBgColor')  #powerBgColor powerId
    power_Button.click()
    sleep(5)

    # # changing the handles to access login page
    # popup_page = None
    # for handle in driver.window_handles:
    #     if handle != main_page:
    #         popup_page = handle
    #         break
         
    # # change the control to signin page       
    #driver.switch_to.window(popup_page)
    obj = driver.switch_to_alert
    #driver.find_element_by_id("p2").click()
    
    sleep(5)
    # print(driver.current_url)
    obj.find_element_by_id('p2').click()
    #driver.find_element_by_xpath('//*[@id ="powerStateBtn"]').click() 
    sleep(5)
    obj.find_element_by_xpath('//*[@id ="powerStateBtn"]').click() 

    print("Login Successful")
    sleep(100)


# def Power_Cycle():
#     AutoLogin = WEBGUI_AutoLogin(BMCIP, Name,Pwd)
#     Post_URL = BMCIP + "cgi/url_redirect.cgi?url_name=topmenu"
#     print(Post_URL)
    #X12_URL = BMCIP + "cgi/url_redirect.cgi?url_name=topmenu"
    #Action1 = AutoLogin.driver.get(Post_URL)
    #Power_Button= Action1.driver.find_element_by_id('powerId')  #powerState_icontxt
    
    

# Main Function
if __name__ == '__main__':
    x = WEBGUI_AutoLogin(BMCIP, Name,Pwd)
    #y = Power_Cycle()


