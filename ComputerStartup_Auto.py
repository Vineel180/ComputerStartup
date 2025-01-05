# Python's libraries
import keyboard
# Vineel's libraries
import vinDateTime
import vinTextFiles
import vinOpenTarget as a
import vinAppWindow
import vinAppProcess
# Program's libraries
import Settings.Settings as Settings
import Settings.LIST as b

def openTickTick():
    keyboard.press('windows')
    keyboard.press_and_release('3')
    keyboard.release('windows')

def convertToQuarterlyDate(date_MMDD):
    """
    returns: XDD,
        where X = A/B/C
        and DD is day
    """
    pass

def main():
    # always 1/2
    openTickTick()

    # daily 1/2
    a.openApps_inList__viaSubprocessPopen(b.DAILY_APPS)

    # weekly

    # monthly

    # quarterly

    #yearly

    # daily 2/2
    a.openSites_inList(b.DAILY_SITES)
    vinAppWindow.appWindow_restoreYaMaximizeYaActivate_withRetry("Microsoft Teams", activate=False)

    # always 2/2
    if Settings.ifRestoreMaximizeActivate_ticktick:
        vinAppWindow.appWindow_restoreYaMaximizeYaActivate_withRetry("TickTick")

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

main()
