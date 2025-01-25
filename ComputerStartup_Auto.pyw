import Settings.Settings as Settings
from datetime import datetime, timedelta

def getDateTimeWeekday():
    now = datetime.now()
    date = now.strftime("%d%m%Y")
    time = now.strftime("%H%M%S")
    weekday = now.weekday()
    return date, time, weekday

def writeFile(filePath, dataToWrite):
    with open(filePath, "wt") as file:
        file.write(dataToWrite)

def readFile(filePath):
    with open(filePath, "rt") as file:
        return file.read()

if __name__=="__main__":
    date, time, weekday = getDateTimeWeekday()
    lastTime = readFile(Settings.lastTime_filePath)
    writeFile(Settings.lastTime_filePath, time)
    ticktickOpened = False
    if (time - lastTime) < 0:
        timeGap = time + timedelta(days=1) - lastTime
    else:
        timeGap = time - lastTime
    print(timeGap)

#    if int(time) > int(Settings.minimumStartupTime):
