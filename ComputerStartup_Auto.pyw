import Settings.Settings as s
import Settings.Library as a
from datetime import datetime, timedelta
import pygetwindow
from time import sleep
from pyautogui import hotkey, press
from pyperclip import copy as p_copy
from webbrowser import open as openSite
from os import startfile as openTarget
from subprocess import run as runTerminalCommand

def getDateTimeWeekdayNow():
    now = datetime.now()
    date = now.strftime("%Y%m%d")
    time = now.strftime("%H%M%S")
    weekday = now.weekday()
    return date, time, weekday, now
def readFile(filePath):
    with open(filePath, "rt") as file:
        return file.read()
def writeFile(filePath, dataToWrite):
    with open(filePath, "wt") as file:
        file.write(dataToWrite)
def maximizeAppWindow(windowName, sleepTime=s., totalRetries):
    if totalRetries>0:
        window = pygetwindow.getWindowsWithTitle(windowName)
        if window:
            if not window[0].isMaximized:
                window[0].maximize()
            return True
        else:
            sleep(sleepTime)
            return maximizeAppWindow(windowName, sleepTime, totalRetries-1)
    else:
        return False
def convertToQuarterlyDate(dateAs_mmdd):
    date = dateAs_mmdd[2:]
    month = dateAs_mmdd[:2]
    if int(month) % 3 == 1:
        month = "A"
    elif int(month) % 3 == 2:
        month = "B"
    else:
        month = "C"
    return (month + date)

def openSite_s(sites):
    for i in sites:
        openSite(i)
def openFolder_s(folders):
    openTarget(folders[0])
    for i in folders[1:]:
        hotkey("ctrl", "t")
        press("f4")
        p_copy(i)
        hotkey("ctrl", "v")
        press("enter")
def openApp_s_viaFilePath(apps):
    for i in apps:
        openTarget(i[2])
def openApp_s_viaTerminalCommand(apps):
    for i in apps:
        runTerminalCommand(i[2])

def openSite_sIfMatch(sites, value):
    for i in sites:
        if i[0] == value:
            openSite(i[1])
def openFolder_sIfMatch(folders, value):
    newFolders = []
    for i in folders:
        if i[0] == value:
            newFolders.append(i[1])
    openFolder_s(newFolders)
def openApp_s_viaFilePathIfMatch(apps, value):
    for i in apps:
        if i[0] == value:
            openTarget(i[2])
def openApp_s_viaTerminalCommandIfMatch(apps, value):
    for i in apps:
        if i[0] == value:
            runTerminalCommand(i[2])

def main(date, weekday):
    #FOLDERS
    #weekly
    openFolder_sIfMatch(a.WEEKLY_FOLDERS, weekday)
    #quarterly
    openFolder_sIfMatch(a.QUARTERLY_FOLDERS, convertToQuarterlyDate(date))

    #APPS stage 1
    openApp_s_viaFilePath(a.FOREVER_APPS__filePath) #forever
    openApp_s_viaTerminalCommand(a.DAILY_APPS__terminalCommand)
    openApp_s_viaTerminalCommand(a.WEEKLY_APPS_terminalCommand)

    #SITES
    openSite_s(a.DAILY_SITES)
    openSite_sIfMatch(a.WEEKLY_SITES, weekday)
    openSite_sIfMatch(a.MONTHLY_SITES, date[0:2])
    openSite_sIfMatch(a.QUARTERLY_SITES, convertToQuarterlyDate(date))
    openSite_sIfMatch(a.YEARLY_SITES, date)

    #APPS stage 2
    for i in a.FOREVER_APPS__filePath: #forever
        maximizeAppWindow(i[0])
    for i in a.DAILY_APPS__terminalCommand:
        maximizeAppWindow(i[0])
    for i in a.WEEKLY_APPS_terminalCommand:
        maximizeAppWindow(i[0])

if __name__=="__main__":
    date, time, weekday, now = getDateTimeWeekdayNow()
    ticktickOpenedQ = False
    ### ### ###
    if int(time) > int(s.minimumStartupTime):
        lastDate = readFile(s.lastDate_filePath)
        if lastDate != date:
            writeFile(s.lastDate_filePath, date)
            main(date[4:], weekday)
            ticktickOpenedQ = True
    ### ### ###
    lastTime_pure = datetime.fromisoformat(readFile(s.lastTime_filePath).strip())
    writeFile(s.lastTime_filePath, now.isoformat())
    if not ticktickOpenedQ:
        if (now - lastTime_pure) >= timedelta(seconds=0):
            if (now - lastTime_pure) > timedelta(seconds=s.minimumTimeGap):
                openApp_s_viaFilePath(a.FOREVER_APPS__filePath)
        else:
            if (now + timedelta(seconds=s.minimumTimeGap) - lastTime_pure) > timedelta(seconds=s.minimumTimeGap):
                openApp_s_viaFilePath(a.FOREVER_APPS__filePath)
