import Settings.Settings as Settings
from datetime import datetime, timedelta
import pygetwindow

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

def maximizeAppWindow(windowName):
    window = pygetwindow.getWindowsWithTitle(windowName)
    if window:
        if not window[0].isMaximized:
            window[0].maximize()    
        return True
    else:
        return False

def startTicktick():


if __name__=="__main__":
    date, time, weekday, now = getDateTimeWeekdayNow()
    ###
    if int(time) > int(Settings.minimumStartupTime):
        lastDate = readFile(Settings.lastDate_filePath)
        if lastDate != date:
            writeFile(Settings.lastDate_filePath, date)
            startTicktick()
            ticktickOpenedQ = True

            # MAIN

    ###
    ticktickOpenedQ = False
    lastTime_pure = datetime.fromisoformat(readFile(Settings.lastTime_filePath).strip())
    writeFile(Settings.lastTime_filePath, now.isoformat())
    if not ticktickOpenedQ:
        if (now - lastTime_pure) >= 0:
            if (now - lastTime_pure) > timedelta(seconds=Settings.minimumTimeGap):
                startTicktick()
        else:
            if (now + timedelta(seconds=Settings.minimumTimeGap) - lastTime_pure) > timedelta(seconds=Settings.minimumTimeGap):
                startTicktick()
