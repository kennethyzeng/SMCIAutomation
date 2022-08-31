############################
#Author: Kenneth Zeng
#Date: 3/11/2022
#Purpose: It generate complete command line for AC, DC , Cburn test and store in exeLine.txt 
############################


import func

Week_Num =func.CurrentWeekYear()
name = func.getUserName()

def CburnStressCompleteCommand():
    cburn = func.Cburn_Run()
    para = func.Cburn_para()
    for i,x in enumerate(para):
        with open("exeLines.txt", "a") as f:
            mbname =para[i-1][0]
            #print(mbname)
            res = cburn.replace("DIR=", "DIR="+ name +'\\'+ Week_Num +'\\'+"cburn"+'\\'+ mbname)
            f.writelines(res+'\n')
            f.close()

def DCONOFFCompleteCommand():
    cburn = func.DC_Run()
    para = func.DC_para()

    for i,x in enumerate(para):
        with open("exeLines.txt", "a") as f:
            mbname =para[i-1][0]
            res = cburn.replace("DIR=", "DIR="+ name +'\\'+ Week_Num +'\\'+"DCONOFF"+'\\'+ mbname)
            f.writelines(res+'\n')
            f.close()

def ACONOFFCompleteCommand():
    cburn = func.AC_Run()
    para = func.AC_para()
    for i,x in enumerate(para):
        with open("exeLines.txt", "a") as f:
            mbname =para[i-1][0]
            res = cburn.replace("DIR=", "DIR="+ name +'\\'+ Week_Num +'\\'+"DCONOFF"+'\\'+ mbname)
            f.writelines(res+'\n')
            f.close()

#DCTest = DCONOFFCompleteCommand()
#ACTest = ACONOFFCompleteCommand()
#CburnStressTest = CburnStressCompleteCommand()
