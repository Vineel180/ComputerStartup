# python imports
from datetime import datetime
from webbrowser import open as openSite
from os import startfile as openTarget
# my imports
import Settings.Settings as Settings
import Settings.LIST as a

def getDateTimeWeekday():
    now = datetime.now()
    date = now.strftime("%Y%m%d")
    time = now.strftime("%H%M")
    weekday = now.weekday()
    return date, time, str(weekday)

def readFile(filePath):
    with open(filePath, 'r') as file:
        return file.read()
def writeFile(filePath, dataToWrite):
    with open(filePath, 'w') as file:
        file.write(dataToWrite)

def openSiteS(List):
    for i in List:
        openSite(i)
def openTargetS(List):
    for i in List:
        openTarget(i)

def openSiteS_ifMatch(List, Match):
    for date, i in List:
        if date == Match:
            openSite(i)
def openTargetS_ifMatch(List, Match):
    for date, i in List:
        if date == Match:
            openTarget(i)

def convertToQuarterly(Date):
    month = Date[0:2]
    day = Date[2:]
    if int(month) % 3 == 1:
        return "A" + day
    elif int(month) % 3 == 2:
        return "B" + day
    else:
        return "C" + day

if __name__ == "__main__":
    date, time, weekday = getDateTimeWeekday()
    if int(time) > int(Settings.startAppAfterTime):
        lastDate = readFile(Settings.lastDate_filePath)
        if date != lastDate:
            writeFile(Settings.lastDate_filePath, date)

            ### ### ### ### ###
            
            # daily 1/2
            openTargetS(a.DAILY_APPS)

            # weekly
            openTargetS_ifMatch(a.WEEKLY_FOLDERS, weekday)
            openSiteS_ifMatch(a.WEEKLY_SITES, weekday)

            # monthly
            openSiteS_ifMatch(a.MONTHLY_SITES, date[6:])

            # quarterly
            openTargetS_ifMatch(a.QUARTERLY_FOLDERS, convertToQuarterly(date[4:]))
            openSiteS_ifMatch(a.QUARTERLY_SITES, convertToQuarterly(date[4:]))

            # yearly
            openSiteS_ifMatch(a.YEARLY_SITES, date[4:])

            # daily 2/2
            openSiteS(a.DAILY_SITES)
