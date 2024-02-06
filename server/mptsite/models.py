from django.db import models

# Create your models here.

class Pairs(models.Model):
    number = models.IntegerField(verbose_name="Номер пары")
    time_start = models.TimeField(verbose_name="Время начала")
    time_end = models.TimeField(verbose_name="Время оконччания")

    def __str__(self):
        return f"{self.number} {self.time_start} - {self.time_end}"

    class Meta():
        verbose_name = "Пару"
        verbose_name_plural = "Пары"


class Direction (models.Model):
    code = models.CharField(max_length=20, verbose_name="Код направления")
    name = models.TextField(verbose_name="Наименование направления")

    def __str__(self):
        return f"{self.code} {self.name}"

    class Meta():
        verbose_name = "Направление"
        verbose_name_plural = "Направления"


class Group(models.Model):
    directions = models.ForeignKey(Direction, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.directions} {self.name}"

    class Meta():
        verbose_name = "Группу"
        verbose_name_plural = "Группы"


class Building (models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    address = models.TextField(verbose_name="Адрес")

    def __str__(self):
        return f"{self.name}"

    class Meta():
        verbose_name = "Корпус"
        verbose_name_plural = "Корпуса"


class Teachers(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя")
    surname = models.CharField(max_length=30, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=30, verbose_name="Отчество", null=True, default="")
    education = models.TextField(verbose_name="Образование")
    kvalificationsUp = models.TextField(verbose_name="Данные о повышении квалификации")
    post = models.CharField(max_length=100,verbose_name="Должность")
    disciplins = models.TextField(verbose_name="Преподаваемые дисциплины")
    workTime = models.IntegerField(verbose_name="Общий трудовой стаж")
    studyTime = models.IntegerField(verbose_name="Педагогический стаж")
    techTtime = models.IntegerField(verbose_name="Стаж работы в техникуме")
    # contacts = models.TextField(verbose_name="Контактная информация")
    degree = models.TextField(verbose_name="Учёная степень", default="нет")

    def __str__(self):
        return f"{self.surname} {self.name[0]}. {self.patronymic[0]}"

    class Meta():
        verbose_name = "Преподавателя"
        verbose_name_plural = "Преподаватели"


class Disciplines(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название дисциплины")


    def __str__(self):
        return f"{self.name}"

    class Meta():
        verbose_name = "Дисциплину"
        verbose_name_plural = "Дисциплины"



class Schedules(models.Model):
    number_pair = models.ForeignKey(Pairs, on_delete=models.CASCADE, verbose_name="Номер пары")
    discipline = models.ForeignKey(Disciplines, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    prepod = models.ForeignKey(Teachers, on_delete=models.CASCADE, verbose_name="Преподаватель")
    audience_number = models.CharField(max_length=10, verbose_name="Номер аудитории")
    date = models.DateField(verbose_name="Дата")
    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name="Корпус")

    def __str__(self):
        return f"{self.date} {self.group} {self.discipline} {self.prepod}"

    class Meta():
        verbose_name = "Строку расписания"
        verbose_name_plural = "Расписание"



# -------------------------------- Модели, которые не идут в базу данных

class DaySchedule:
    # инит и переменные внутри были основаны на элементе из миро
    def __init__(self, day, schedules_list):
        self.cur_date = day
        self.lessons = schedules_list

    def __str__(self):
        return  f"{self.cur_date} | {self.lessons}"

