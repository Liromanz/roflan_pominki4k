from django.shortcuts import get_object_or_404

from ...models import Schedules, Group, DaySchedule, DateTemplates
from .date_helper import DateHelper
from datetime import datetime, timedelta


class ChangeScheduleChecker:
    def __init__(self, changed: list):
        self.changed = changed

    def was_changed(self, cur_para: Schedules):
        for change in self.changed:
            if change.number_pair == cur_para.number_pair and change.ischange and not change.iscanceled:
                return True
        return False

    def was_canceled(self, cur_para: Schedules):
        for change in self.changed:
            if change.number_pair == cur_para.number_pair and change.iscanceled:
                return True
        return False


class ScheduleGenerator:

    ### Принцип:
    # Есть 4 блока расписания - с 1 по 14 сентября. 15-28 сентября | 12-25 января.  26 янв- 1 февраля. 2-8 февраля.
    # Если сегодня 1 или 3 блок даты - тогда нужно просто показать расписание на эти дни
    # Если сегодня дата в промежутке от 2 блока до 28 января, или от 4 блока до 28 июля,
    # то дублировать расписание из 2 или 4 блока
    # TODO: подумать над схематикой сессии и отметкой расписания. сделать более наглядную модель работы с расписанием
    ###

    @staticmethod
    def generate_by_day(group: Group, selected_date: datetime = datetime.today()):
        schedule = ScheduleGenerator.__get_base_schedule__(group, selected_date).order_by('number_pair')
        day = [DaySchedule(datetime.today(), schedule)]
        return day

    @staticmethod
    def generate_current_week(group: Group):
        helper = DateHelper(datetime.today())

        dates = helper.get_week_by_date()
        day = []
        for d in dates:
            day.append(DaySchedule(d, ScheduleGenerator.__get_base_schedule__(group, d).order_by('number_pair')))
        return day

    @staticmethod
    def generate_next_week(group: Group):
        helper = DateHelper(datetime.today() + timedelta(weeks=1))

        dates = helper.get_week_by_date()

        day = []
        for d in dates:
            day.append(DaySchedule(d, ScheduleGenerator.__get_base_schedule__(group, d).order_by('number_pair')))
        return day

    @staticmethod
    def generate_by_two_dates(group: Group, start_date: datetime, end_date: datetime):
        helper = DateHelper(start_date)

        dates = helper.get_all_days_until(end_date)

        day = []
        for d in dates:
            day.append(DaySchedule(d, ScheduleGenerator.__get_base_schedule__(group, d)))

        return day

    # ------------------------------ Главный метод по генерации расписания

    @staticmethod
    def __get_base_schedule__(group: Group, selected_date: datetime):
        selected_date = datetime(2024, selected_date.month, selected_date.day)

        blocks = get_object_or_404(DateTemplates, date_from__lte=selected_date, date_end__gte=selected_date)
        is_even_week = selected_date.isocalendar().week % 2
        weekday = selected_date.isoweekday()

        rasp = list(Schedules.objects.filter(group=group, date=selected_date, ischange=True))
        print(rasp)
        change_checker = ChangeScheduleChecker(rasp)

        for para in Schedules.objects.filter(group=group, block_rasp=blocks, date__iso_week_day=weekday):
            if change_checker.was_changed(para):
                continue
            if para.date.isocalendar().week % 2 == is_even_week and not change_checker.was_canceled(para):
                rasp.append(para)

        return sorted(filter(lambda x: not x.iscanceled, rasp), key=lambda x: x.number_pair.id)
