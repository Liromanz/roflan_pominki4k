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
