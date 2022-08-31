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
import linecache

def Run_CommandLine_From_exeLines():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')

    # Provide the path of chromedriver present on your system.
    driver = webdriver.Chrome(executable_path="chromedriver",
                            chrome_options=options)
    driver.set_window_size(1920,1080)


    driver.get('http://172.30.0.1/cgi-bin/autopxe-v2.php')
    sleep(10)

    with open("exeLines.txt", "r") as my_file:
        for line in my_file:
            commandLine = line.split('>=')[1].strip()
            mac_address = line.split('>=')[0].strip()
            # print(commandLine)
            # print(mac_address)
            # store =[]
            # store.append(commandLine)
            # store.append(mac_address)
            # print(store)
            
            PXE_Command_Input = driver.find_element_by_name('command')
            PXE_Command_Input.send_keys(commandLine)
            sleep(2)

            Mac_Address_Input= driver.find_element_by_name('address')
            Mac_Address_Input.send_keys(mac_address)
            sleep(2)

            Update_Button_Click =driver.find_element_by_xpath("//input[@value ='Update']")
            sleep(5)
            Update_Button_Click.click()
            print("MB with Mac_Address" + mac_address +" was executed")
            
        sleep(10)
        driver.quit()
        print("All the command Lines from exeLines.txt are excuated at 172.30.0.1 already")


# Main Function
if __name__ == '__main__':
    x = Run_CommandLine_From_exeLines()


