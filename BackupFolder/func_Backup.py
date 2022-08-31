######################
#Author: Kenneth Zeng
#Date: 03/12/2022
#Purpose: -Generate AutoRun elemenet for AC, DC, Cburn test 
#         -Generate rough autoRun command Line for AC, DC, Cburn (need to replace DIR inorder to complete)
#         -Function to grap current weeknumber and Year
#         -function to grap username
######################
import linecache
import datetime
import re

def DC_para():
    DCVar = []
    with open("DConoff.txt", "r") as my_file:
      for line in my_file:
          str = line.split()
          DCVar.append(str)
    return DCVar
##Output for DC_Para:[['X12DDW', '0025909182', '172.30.183.254', 'ADMIN', 'ADMIN'], ['X13DDW', '00259dfad82', '172.30.183.254', 'ADMIN', 'ADMIN']]

def AC_para():
    DCVar = []
    with open("AConoff.txt", "r") as my_file:
      for line in my_file:
          str = line.split()
          DCVar.append(str)
    return DCVar
##Output for DC_Para:[['X12DDW', '0025909182', '172.30.183.254', 'ADMIN', 'ADMIN'], ['X13DDW', '00259dfad82', '172.30.183.254', 'ADMIN', 'ADMIN']]

def Cburn_para():
    DCVar = []
    with open("CburnStress.txt", "r") as my_file:
      for line in my_file:
          str = line.split()
          DCVar.append(str)
    return DCVar
##Output for DC_Para:[['X12DDW', '0025909182', '172.30.183.254', 'ADMIN', 'ADMIN'], ['X13DDW', '00259dfad82', '172.30.183.254', 'ADMIN', 'ADMIN']]

#when uselincache, have \n at the end. need strip() to remove
def Cburn_Run():
    f = "Config.txt"
    DCVar0 = linecache.getline(f, 1).strip()
    DCVar1 = linecache.getline(f, 9).strip()
    DCVar2 = linecache.getline(f, 7).strip()
    DCVar3 = linecache.getline(f, 2).strip()
    DCVar4 = linecache.getline(f, 4).strip()
    DCVar5 = linecache.getline(f, 3).strip()
    CburnCom = DCVar0 + ' ' + DCVar1 + ' ' + DCVar2 + ' '+ DCVar3+ ' '+ DCVar4 +' '+ DCVar5
    return CburnCom
####Output for Cburn_Run :cburn-r83 I_WILL_DEBUG SAT=8 LIN=8 MPM=8 MDELT=10256 DIR= NBMCK

def DC_Run():
    f = "Config.txt"
    DCVar0 = linecache.getline(f, 1).strip()
    DCVar1 = linecache.getline(f, 9).strip()
    DCVar2 = linecache.getline(f, 5).strip()
    DCVar3 = linecache.getline(f, 2).strip()
    DCVar4 = linecache.getline(f, 4).strip()
    DCVar5 = linecache.getline(f, 3).strip()
    CburnCom = DCVar0 + ' ' + DCVar1 + ' ' + DCVar2 + ' '+ DCVar3+ ' '+ DCVar4 +' '+ DCVar5
    return CburnCom
####Output of DC_Run: cburn-r83 I_WILL_DEBUG ONOFF=500 MDELT=10256 DIR= NBMCK

def AC_Run():
    f = "Config.txt"
    DCVar0 = linecache.getline(f, 1).strip()
    DCVar1 = linecache.getline(f, 9).strip()
    DCVar2 = linecache.getline(f, 6).strip()
    DCVar3 = linecache.getline(f, 2).strip()
    DCVar4 = linecache.getline(f, 4).strip()
    DCVar5 = linecache.getline(f, 3).strip()
    CburnCom = DCVar0 + ' ' + DCVar1 + ' ' + DCVar2 + ' '+ DCVar3+ ' '+ DCVar4 +' '+ DCVar5
    return CburnCom
####Output of DC_Run: cburn-r83 I_WILL_DEBUG ACOFF=172.30.71.6:1 MDELT=10256 DIR= NBMCK

def CurrentWeekYear():
    today = datetime.date.today()
    year, weekNum, day_of_week =today.isocalendar()
    if weekNum < 10:
        weekNum = '0'+ str(weekNum)
    return (str(weekNum)+ str(year))

def getUserName():
    with open("Config.txt", "r") as f:
        name = f.readlines()[7:8]   ##Type list; need to change to string, and remove uncessary head and tail
        name = str(name)
        t=name.strip("\\n']")
        t= t.strip("['")[9:]
        return t

# def GenComLine():
#     Week_Num =func.CurrentWeekYear()
#     cburn = func.Cburn_Run()
#     para = func.DC_para()
#     name = func.getUserName()
#     mbname = func.DC_para()
#     for i,x in enumerate(para):
#          with open("CommandLines.txt", "r") as f:
#              res = cburn.replace("DIR=", "DIR="+ name +'\\'+ Week_Num +'\\'+"cburn"+'\\'+ mbname[i][0])
#              print(res)
