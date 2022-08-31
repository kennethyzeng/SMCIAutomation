from selenium import webdriver
import time
  
# Main Function
if __name__ == '__main__':
  
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')
  
    # Provide the path of chromedriver present on your system.
    driver = webdriver.Chrome(executable_path="chromedriver",
                              chrome_options=options)
    driver.set_window_size(1920,1080)
  
    # Send a get request to the url
    driver.get('http://172.30.0.1/cgi-bin/autopxe-v2.php')
    time.sleep(60)
    driver.quit()
    print("Done")

    #######
    #############################
#Author: Kenneth Zeng
#Date: 3/12/2022
#Purpose: Automatically place command lines to 172.30.0.1 to run AC, DC , Cburn Stress
#############################

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.options import Options



# Main Function
if __name__ == '__main__':
  
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')
  
    # Provide the path of chromedriver present on your system.
    driver = webdriver.Chrome(executable_path="chromedriver",
                              chrome_options=options)
    driver.set_window_size(1920,1080)
  
   
    driver.get('http://172.30.0.1/cgi-bin/autopxe-v2.php')
    sleep(10)

    PXE_Command_Input = driver.find_element_by_name('command')
    PXE_Command_Input.send_keys("helllo")

    Mac_Address_Input= driver.find_element_by_name('address')
    Mac_Address_Input.send_keys("00:25:90:36")

 
    Update_Button_Click =driver.find_element_by_xpath("//input[@value ='Update']")
    
    print("gonint to press button")
    sleep(30)
    Update_Button_Click.click()
    
    sleep(5)
    driver.quit()
    print("Done")

#username = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")


# brower = webdriver.Chrome("/Users/SMCI/Dropbox/Mac/Desktop/SMCIAutomation/chromedriver.exe")
# driver.get('http://172.30.0.1/cgi-bin/autopxe-v2.php')
# print ("complete")
# sleep(15)
# print("sleep complete")
  
# username_box = driver.find_element_by_id('email')
# username_box.send_keys(usr)
# print ("Email Id entered")
# sleep(1)

# password_box = driver.find_element_by_id('pass')
# password_box.send_keys(pwd)
# print ("Password entered")

# login_box = driver.find_element_by_id('loginbutton')
# login_box.click()

# print ("Done")
# input('Press anything to quit')
# driver.quit()
# print("Finished")
