from datetime import date, timedelta

class DateHelper:
    def __init__(self, selected_date : date):
        self.selected_date = selected_date

    def get_week_by_date(self):
        self.selected_date -= timedelta(days=self.selected_date.weekday())
        week = [self.selected_date]
        for _ in range(6):
            self.selected_date += timedelta(days=1)
            week.append(self.selected_date)
        return week

    def get_first_day_week(self):
        self.selected_date -= timedelta(days=self.selected_date.weekday())
        return self.selected_date

    def get_last_day_week(self):
        self.selected_date += timedelta(days=6-self.selected_date.weekday())
        return self.selected_date

    def get_all_days_until(self, end_date : date):
        if end_date < self.selected_date:
            return #TODO: сделать собственную обработку ошибок

        delta = end_date - self.selected_date

        day = []
        for i in range(delta.days + 1):
            if (self.selected_date + timedelta(days=i)).weekday() == 6:
                continue
            day.append(self.selected_date + timedelta(days=i))
        return day
