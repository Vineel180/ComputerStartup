# Python's libraries
# Vineel's libraries
import vinDateTime
import vinTextFiles
import vinOpenTarget as a
import vinAppWindow
# Program's libraries
import Settings.Settings as Settings
import Settings.LIST as b

def main():
    a.openApp_viaSubprocessPopen("start ticktick://")
    a.openApp_viaSubprocessPopen(b.DAILY_APPS)
    a.openSites_inList(b.DAILY_SITES)
    vinAppWindow.appWindow_restoreYaMaximizeYaActivate("Microsoft Teams", activate=False)
    vinAppWindow.appWindow_restoreYaMaximizeYaActivate("TickTick")

if __name__ == "__main__":
    dateTimeWeekday = vinDateTime.getDateTimeWeekday()
    date = dateTimeWeekday[0:8]
    time = dateTimeWeekday[8:12]
    weekday = dateTimeWeekday[-1]
    if int(time) > int(Settings.startAppAfterTime):
        lastDate = vinTextFiles.readFile( Settings.lastDate_filePath )
        if date != lastDate:
            vinTextFiles.writeFile( Settings.lastDate_filePath, date )
            main()
