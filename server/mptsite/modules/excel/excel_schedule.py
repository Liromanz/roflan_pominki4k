import xlrd
import re
from datetime import datetime, timedelta

from ...models import *


class ExcelParser:

    @staticmethod
    def __generate_disciplines(discipline_set: set):
        for item in discipline_set:
            try:
                Disciplines.save(Disciplines(discipline_name=item))
            except Exception as error:
                print(error)

        print(discipline_set)

    @staticmethod
    def __generate_teacher_disciplines(discipline_teacher_set: set):
        for item in discipline_teacher_set:
            discip, teacher_ab = item
            teacher_ab = teacher_ab.split(',')
            for one_teacher in teacher_ab:
                result_dis: Disciplines
                result_emp: Employees

                fio = one_teacher.split('.')
                if len(fio) != 1:
                    try:
                        fio[2] = fio[2].replace('ё', 'е')
                        prepods_variant = Employees.objects.filter(surname=fio[2].strip())
                        for prepod in prepods_variant:
                            if prepod.name.startswith(fio[0].strip()) and prepod.patronymic.startswith(fio[1].strip()):
                                result_emp = prepod
                                break

                        if len(prepods_variant) == 0 and (fio[2].strip() != "" or fio[2].strip() != " "):
                            created_employee = Employees(surname=fio[2].strip(), name=fio[0], patronymic=fio[1])
                            created_employee.save()

                        result_dis = Disciplines.objects.filter(discipline_name=discip).first()
                        result = Teacher_Disciplines(discipline=result_dis, employee=result_emp)
                        result.save()
                        print('гуд')
                    except Exception as error:
                        print(error)

                # в случае, если это какая-нибудь практика, у которой нет препода
                elif len(fio) == 1 and discip != '':
                    try:
                        result_dis = Disciplines.objects.filter(discipline_name=discip).first()
                        result = Teacher_Disciplines(discipline=result_dis, employee=None)
                        result.save()
                        print('гуд')
                    except Exception as error:
                        print(error)

            print(item)

    @staticmethod
    def __generate_day_schedule(schedule: list):
        print("ошибки при генерации расписания:")
        for para in schedule:
            try:
                para.make_db_schedule().save()
            except Exception as error:
                print(para)
                print(error)


    @staticmethod
    def import_schedule():
        discipline_set = set()
        discipline_teacher_set = set()
        result_schedule = []
        days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
        index_week : int
        pair_number : int

        book = xlrd.open_workbook("D:\\pipon\\roflan_pominki4k\\rasp.xls")

        # ОГРОМНАЯ строка чипсов лейс для того, чтобы взять данные из ячейки первого листа, а потом переконверить ее в дату
        starting_date = datetime.strptime(
            re.findall(r"\d{1,2}.\d{1,2}.\d{2,4}", book.sheet_by_index(0).cell_value(rowx=7, colx=0))[0], "%d.%m.%Y")
        # 0 пн 1 вт 2 ср 3 чт 4 пт 5 сб 6 вс
        starting_week_day = starting_date.weekday()
        print(starting_week_day)
        print(starting_date)

        for sheet in range(book.nsheets):
            sh = book.sheet_by_index(sheet)
            for groupColumn in range(2, sh.ncols + 1, 3):
                # группа:
                print("------------------------------------------------------------")
                print("Группа: ", sh.cell_value(rowx=8, colx=groupColumn))
                index_week = 0

                for rx in range(9, 93, 14):
                    # здание
                    print(days_of_week[index_week])
                    building = "Нежинская"  # изначально здание нежка
                    # если здание поставлено, то ставим его
                    building_cell = sh.row(rx)[groupColumn].value.capitalize()
                    if building_cell != "":
                        building = building_cell
                    print(building)

                    pair_number = 1
                    for paraCell in range(rx + 2, rx + 14, 2):
                        # внутри одной записи есть две ячейки
                        # в общей паре - верхняя и нижняя
                        # в числителе - только верхняя
                        # в знаменателе - только нижняя
                        upper_cell = sh.row(paraCell)[groupColumn].value
                        lower_cell = sh.row(paraCell + 1)[groupColumn].value

                        # если в верхней есть фио (значит числитель) или если верхняя пустая а нижняя нет (знаменатель)
                        if re.search(r".\..\. .*$", upper_cell) or (upper_cell == "" and lower_cell != ""):
                            disc: str
                            teacher: str
                            para_date: datetime
                            # числитель
                            if upper_cell != "":
                                disc = re.sub(r".\..\. .*$", "", upper_cell).strip()
                                teacher = re.findall(r".\..\. .*$", " ".join(upper_cell.split()))[0]
                                para_date = starting_date + timedelta(days=index_week)
                                print(pair_number, "Числитель: ", disc, teacher)

                                discipline_set.add(disc)
                                discipline_teacher_set.add((disc, teacher))

                                angl = teacher.split(",")
                                for prepod in angl:
                                    result_schedule.append(
                                        ExcelSchedule(pair_number, sh.cell_value(rowx=8, colx=groupColumn), building,
                                                      para_date, prepod, disc))

                            # знаменатель
                            if lower_cell != "":
                                disc = re.sub(r".\..\. .*$", "", lower_cell).strip()
                                teacher = re.findall(r".\..\. .*$", " ".join(lower_cell.split()))[0]
                                para_date = starting_date + timedelta(days=index_week + 7)
                                print(pair_number, "Знаменатель:", disc, teacher)

                                discipline_set.add(disc)
                                discipline_teacher_set.add((disc, teacher))

                                angl = teacher.split(",")
                                for prepod in angl:
                                    result_schedule.append(
                                        ExcelSchedule(pair_number, sh.cell_value(rowx=8, colx=groupColumn), building,
                                                      para_date, prepod, disc))
                        else:
                            # общая пара
                            disc = " ".join(upper_cell.split())
                            teacher = " ".join(lower_cell.split())
                            if disc != "":
                                discipline_set.add(disc)
                                discipline_teacher_set.add((disc, teacher))

                                angl = teacher.split(",")
                                for prepod in angl:
                                    # и для числителя
                                    result_schedule.append(
                                        ExcelSchedule(pair_number, sh.cell_value(rowx=8, colx=groupColumn), building,
                                                      starting_date + timedelta(days=index_week), prepod, disc))

                                    # и для знаменателя
                                    result_schedule.append(
                                        ExcelSchedule(pair_number, sh.cell_value(rowx=8, colx=groupColumn), building,
                                                      starting_date + timedelta(days=index_week+7), prepod, disc))

                                print(pair_number, disc, teacher)

                        pair_number += 1

                    index_week += 1
                    print("----------")

        # вот здесь, основываясь на сете из дисциплин, которые мы набрали выше, делаются дисциплины
        ExcelParser.__generate_disciplines(discipline_set)

        # вот тут тусятся список дисциплин и их преподов
        ExcelParser.__generate_teacher_disciplines(discipline_teacher_set)

        # после добавления всего того, что было выше, генерится расписание на день
        ExcelParser.__generate_day_schedule(result_schedule)
