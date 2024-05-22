import xlrd
import re
from datetime import datetime, timedelta

from ...models import *


class ExcelParser:

    @staticmethod
    def __generate_teacher_disciplines():
        pass

    @staticmethod
    def __generate_one_day(pair_number: int, group: str, building: str, date: datetime, teacher: str):
        group_schedule = Schedules()
        group_schedule.group = Groups.objects.get(group_name=group)
        group_schedule.building = Buildings.objects.get(name=building)
        group_schedule.pair_number = Pair_numbers.objects.get(id=pair_number)
        group_schedule.date = date

        # тут надо поебаться с преподом
        # group_schedule.teacher = Teacher_Disciplines.objects.get()

        group_schedule.save()

    @staticmethod
    def import_schedule():
        days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
        index_week = 0
        pair_number = 1

        book = xlrd.open_workbook("rasp.xls")
        # print("The number of worksheets is {0}".format(book.nsheets))
        # print("Worksheet name(s): {0}".format(book.sheet_names()))

        # ОГРОМНАЯ строка чипсов лейс для того, чтобы взять данные из ячейки первого листа, а потом переконверить ее в дату
        starting_date = datetime.strptime(
            re.findall(r"\d{1,2}.\d{1,2}.\d{2,4}", book.sheet_by_index(0).cell_value(rowx=7, colx=0))[0], "%d.%m.%Y")
        print(starting_date)

        for sheet in range(book.nsheets):
            sh = book.sheet_by_index(sheet)
            # print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
            # print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=5)))
            for groupColumn in range(2, sh.ncols + 1, 3):
                # группа:
                print("------------------------------------------------------------")
                print("Группа: ", sh.cell_value(rowx=8, colx=groupColumn))
                index_week = 0

                for rx in range(9, 93, 14):
                    # здание
                    print(days_of_week[index_week])
                    building = "Нежинская"  # изначально здание нежка
                    if sh.row(rx)[groupColumn].value != "":
                        print(sh.row(rx)[groupColumn].value.capitalize())  # если здание поставлено, то ставим его
                        building = sh.row(rx)[groupColumn].value.capitalize()

                    pair_number = 1
                    for paraCell in range(rx + 2, rx + 14, 2):
                        upper_cell = sh.row(paraCell)[groupColumn].value
                        lower_cell = sh.row(paraCell + 1)[groupColumn].value

                        if re.search(r".\..\. .*$", upper_cell) or (upper_cell == "" and lower_cell != ""):
                            # числитель
                            if upper_cell != "":
                                print(pair_number, "В числитель: ",
                                      " ".join(sh.row(paraCell)[groupColumn].value.split()))
                                ExcelParser.__generate_one_day(pair_number, sh.cell_value(rowx=8, colx=groupColumn),
                                                               building, starting_date + timedelta(days=index_week), "")

                            # знаменатель
                            if lower_cell != "":

                                print("  В знаменатель: ", " ".join(sh.row(paraCell + 1)[groupColumn].value.split()))
                                ExcelParser.__generate_one_day(pair_number, sh.cell_value(rowx=8, colx=groupColumn),
                                                               building, starting_date + timedelta(days=index_week+7), "")
                        else:
                            # общая пара
                            print(pair_number, " ".join(sh.row(paraCell)[groupColumn].value.split()),
                                  " ".join(sh.row(paraCell + 1)[groupColumn].value.split()))
                            #и для числителя
                            ExcelParser.__generate_one_day(pair_number, sh.cell_value(rowx=8, colx=groupColumn),
                                                           building, starting_date + timedelta(days=index_week), "")
                            #и для знаменателя
                            ExcelParser.__generate_one_day(pair_number, sh.cell_value(rowx=8, colx=groupColumn),
                                                           building, starting_date + timedelta(days=index_week + 7), "")

                        pair_number += 1

                    index_week += 1
                    print("----------")
