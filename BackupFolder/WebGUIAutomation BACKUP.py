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

    driver.set_window_size(1920,1080)
    print(URL + Name + Pwd)

    driver.get(URL)
    sleep(10)
            
    Username= driver.find_element_by_id('usrName')
    Username.send_keys(Name)
    sleep(5)

    Password= driver.find_element_by_id('pwd')
    Password.send_keys(Pwd)
    sleep(2)

    Login_Button =driver.find_element_by_xpath ('//button[text()="Login"]')   ##search Button with Login text
    sleep(5)
    Login_Button.click()
    print("Login Successful")
    
    sleep(10)
    driver.quit()
    print("All the command Lines from exeLines.txt are excuated at 172.30.0.1 already")


# Main Function
if __name__ == '__main__':
    x = WEBGUI_AutoLogin(BMCIP, Name,Pwd)


