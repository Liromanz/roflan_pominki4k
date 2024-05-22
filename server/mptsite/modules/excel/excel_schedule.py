import xlrd
import re

from ...models import Schedules


class ExcelParser:

    @staticmethod
    def import_schedule():
        days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
        index_week = 0
        pair_number = range(1, 7)
        index_pair = 0

        book = xlrd.open_workbook("rasp.xls")
        # print("The number of worksheets is {0}".format(book.nsheets))
        # print("Worksheet name(s): {0}".format(book.sheet_names()))

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
                    if sh.row(rx)[groupColumn].value == "":
                        print("НЕЖИНСКАЯ")  # если пусто, то ставим нежку
                    else:
                        print(sh.row(rx)[groupColumn].value)  # если нет, то то здание, которое написано

                    index_pair = 0
                    for paraCell in range(rx + 2, rx + 14, 2):
                        if (re.search(r".\..\. .*$", sh.row(paraCell)[groupColumn].value)
                                or (sh.row(paraCell)[groupColumn].value == "" and sh.row(paraCell + 1)[
                                    groupColumn].value != "")):
                            print(pair_number[index_pair], "В числитель: ",
                                  " ".join(sh.row(paraCell)[groupColumn].value.split()))
                            print("  В знаменатель: ", " ".join(sh.row(paraCell + 1)[groupColumn].value.split()))
                        else:
                            print(pair_number[index_pair], " ".join(sh.row(paraCell)[groupColumn].value.split()),
                                  " ".join(sh.row(paraCell + 1)[groupColumn].value.split()))
                        index_pair += 1

                    index_week += 1
                    print("----------")

                # часть для знаменателя
