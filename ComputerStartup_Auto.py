import Settings.Settings as Settings
import vinDateTime

if __name__ == "__main__":
    dateTimeWeekday = vinDateTime.getDateTimeWeekday()
    date = dateTimeWeekday[0:8]
    time = dateTimeWeekday[8:12]
    weekday = dateTimeWeekday[-1]
