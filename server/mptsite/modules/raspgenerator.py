from ..models import Schedules, Group, DaySchedule
from datetime import date

class RaspGenerator():
    def GenerateCurrentDay(self, group : Group):
        schedule = Schedules.objects.filter(date=date.today(), group=group)
        day = [DaySchedule(date.today(), schedule)] #TODO: какого-то хуя не работает передача даты
        print(day)
        return day


    def GenerateCurrentWeek(self):
        pass

    def GenerateNextWeek(self):
        pass

    def GenerateByTwoDates(self):
        pass


