import pyautogui
import time
from datetime import date, timedelta
import pandas as pd
import datetime
count=0


def testpgm(): 
    #read Date File 
    date =open('datenext.txt','r').read()
    print(dat)
    #convert in Date -- enddate
    enddate = pd.to_datetime(date) + pd.DateOffset(days=1)
    print(enddate)
    #Date format to '/"
    date2 = enddate.strftime('%m/%d/%Y')
    print(date2)
    #removing "/" from date to create file name 
    filename1 = enddate.strftime('%m%d%Y')
    print(filename1)                            
    #date1.close()
    #read Date File 
    file1 = open('datenext.txt','w')
    #New Date write in file
    file1.write(date2)
    #file1.close()

def autoclose(): 
    #mouse moving to 'X' place
    pyautogui.moveTo (778, 140)
    # mouse click to close
    pyautogui.click()
    # keyborad function (alt+f4) to cole completely
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')
    #keyboard key "y"
    pyautogui.press('y')

def autoopen():
    #mouse moving to 'X' place
    pyautogui.moveTo (1188, 152)
    # mouse click to open application
    pyautogui.doubleClick()
    time.sleep(10)
    pyautogui.typewrite('your_User_name')
    pyautogui.press('tab')
    pyautogui.typewrite('your_Password')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(5)
    #mouse moving to 'X' place
    pyautogui.moveTo (1905, 30)
    pyautogui.click()
    time.sleep(1)
    
def autoprogram():
    print('started')
    #read Date File 
    date1 =open('datenext.txt','r').read()
    date1.strip()
    
    print(date1)
    #date_1 = datetime.datetime.strptime('date1', "%m/%d/%y")
    #print(date_1)
    #end_date = date_1 + datetime.timedelta(days=1)
    #print(end_date)
    enddate = pd.to_datetime(date1) + pd.DateOffset(days=1)
    print(enddate)
    filedate = pd.to_datetime(date1)
    filename = filedate.strftime('%m%d%Y')
    print(filename)                            
    #date1.close()
    
    
    #file1.close()
    pyautogui.moveTo (634, 32)
    pyautogui.click()
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('right')
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('backspace')
    pyautogui.typewrite(date1)
    pyautogui.press('tab')
    pyautogui.typewrite(date1)
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.moveTo (853, 563)
    pyautogui.click()
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(60)
    pyautogui.moveTo (19, 95)
    pyautogui.click()
    time.sleep(7)
    pyautogui.typewrite(filename)
    pyautogui.press('tab')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(40)
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.moveTo (1917, 29)
    pyautogui.click()
    date2 = enddate.strftime('%m/%d/%Y')
    file1 = open('datenext.txt','w')
    file1.write(date2)

autoprogram()

while True:
    #program continues run upto 30 time 

    if ( count < 30 ): 
      autoprogram()
      count = count + 1 
    #if program reach 30 times it will close program,opeprogram,again make count 0
    if  ( count == 30):
        #testpgm()
        autoclose()
        autoopen()
        count = 0
#print(pyautogui.position())




