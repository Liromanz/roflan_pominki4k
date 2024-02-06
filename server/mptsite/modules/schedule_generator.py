from ..models import Schedules, Group, DaySchedule
from .date_helper import DateHelper
from datetime import date, timedelta

class ScheduleGenerator:

    @staticmethod
    def generate_by_day(group : Group, selected_date : date = date.today()):
        schedule = Schedules.objects.filter(date=date.today(), group=group)
        day = [DaySchedule(date.today(), schedule)]
        return day

    @staticmethod
    def generate_current_week(group : Group):
        helper = DateHelper(date.today())

        dates = helper.get_week_by_date()
        schedule = Schedules.objects.filter(date__gte=helper.get_first_day_week(), date__lte=helper.get_last_day_week(),
                                            group=group)
        day = []
        for d in dates:
            day.append(DaySchedule(d,  schedule.filter(date=d).order_by('number_pair')))
        return day

    @staticmethod
    def generate_next_week(group : Group):
        helper = DateHelper(date.today() + timedelta(weeks=1))

        dates = helper.get_week_by_date()
        schedule = Schedules.objects.filter(date__gte=helper.get_first_day_week(), date__lte=helper.get_last_day_week(),
                                            group=group)
        day = []
        for d in dates:
            day.append(DaySchedule(d, schedule.filter(date=d).order_by('number_pair')))
        return day

    @staticmethod
    def generate_by_two_dates(group : Group, start_date : date, end_date : date):
        schedule = Schedules.objects.filter(date__gte=start_date, date__lte=end_date,
                                            group=group)
        day = []
        for d in range((end_date-start_date).days):
            cur_date = start_date + timedelta(d)
            day.append(DaySchedule(start_date + timedelta(days=1), schedule.filter(date=cur_date).order_by('number_pair')))
        return day
