from ...models import Schedules, Group, DaySchedule
from .date_helper import DateHelper
from datetime import date, timedelta


class ScheduleGenerator:

    ### Принцип:
    # Есть 4 блока расписания - с 1 по 14 сентября. 15-28 сентября | 12-25 января.  26 янв- 1 февраля. 2-8 февраля.
    # Если сегодня 1 или 3 блок даты - тогда нужно просто показать расписание на эти дни
    # Если сегодня дата в промежутке от 2 блока до 28 января, или от 4 блока до 28 июля,
    # то дублировать расписание из 2 или 4 блока
    # TODO: подумать над схематикой сессии и отметкой расписания. сделать более наглядную модель работы с расписанием
    ###

    @staticmethod
    def generate_by_day(group: Group, selected_date: date = date.today()):
        schedule = Schedules.objects.filter(date=date.today(), group=group)
        day = [DaySchedule(date.today(), schedule)]
        return day

    @staticmethod
    def generate_current_week(group: Group):
        helper = DateHelper(date.today())

        dates = helper.get_week_by_date()
        schedule = Schedules.objects.filter(date__gte=helper.get_first_day_week(), date__lte=helper.get_last_day_week(),
                                            group=group)
        day = []
        for d in dates:
            day.append(DaySchedule(d, schedule.filter(date=d).order_by('number_pair')))
        return day

    @staticmethod
    def generate_next_week(group: Group):
        helper = DateHelper(date.today() + timedelta(weeks=1))

        dates = helper.get_week_by_date()
        schedule = Schedules.objects.filter(date__gte=helper.get_first_day_week(), date__lte=helper.get_last_day_week(),
                                            group=group)
        day = []
        for d in dates:
            day.append(DaySchedule(d, schedule.filter(date=d).order_by('number_pair')))
        return day

    @staticmethod
    def generate_by_two_dates(group: Group, start_date: date, end_date: date):
        helper = DateHelper(start_date)

        dates = helper.get_all_days_until(end_date)
        schedule = Schedules.objects.filter(date__gte=start_date, date__lte=end_date,
                                            group=group)
        day = []
        for d in dates:
            day.append(DaySchedule(d, schedule.filter(date=d).order_by('number_pair')))

        return day
