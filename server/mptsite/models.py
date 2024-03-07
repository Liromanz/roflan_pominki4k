from django.db import models
from django.db.models import UniqueConstraint


class Pairs(models.Model):
    number = models.IntegerField(verbose_name="Номер пары", unique=True)
    time_start = models.TimeField(verbose_name="Время начала")
    time_end = models.TimeField(verbose_name="Время окончания")

    def __str__(self):
        return f"{self.number} {self.time_start} - {self.time_end}"

    class Meta():
        verbose_name = "Пару"
        verbose_name_plural = "Пары"


class CodeDirection (models.Model):
    code = models.CharField(max_length=20, verbose_name="Код направления", unique=True)
    name = models.TextField(verbose_name="Наименование направления", unique=True)

    def __str__(self):
        return f"{self.code} {self.name}"

    class Meta():
        verbose_name = "Направление"
        verbose_name_plural = "Направления"


class Speciality (models.Model):
    code = models.ForeignKey(CodeDirection, on_delete=models.CASCADE, verbose_name="Код")
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta():
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"


class Group(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.speciality} {self.name}"

    class Meta():
        verbose_name = "Группу"
        verbose_name_plural = "Группы"


class Building (models.Model):
    name = models.CharField(max_length=30, verbose_name="Название", unique=True)
    address = models.TextField(verbose_name="Адрес", unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta():
        verbose_name = "Корпус"
        verbose_name_plural = "Корпуса"


class Disciplines(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название дисциплины", unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta():
        verbose_name = "Дисциплину"
        verbose_name_plural = "Дисциплины"

class Prepods(models.Model):
    surname = models.CharField(verbose_name="Фамилия", max_length=50, default="")
    name = models.CharField(verbose_name="Имя", max_length=50, null=False, default='')
    patronymic = models.CharField(verbose_name="Отчество", max_length=50, null=True, default="")
    education = models.TextField(verbose_name="Образование", null=True, default="")
    qualification = models.TextField(verbose_name="Данные о повышении квалификации",null=True, default="")
    post = models.TextField(verbose_name="Должность", max_length=300, default="преподаватель")
    disciplines = models.TextField(verbose_name="Преподаваемые дисциплины", default="")
    full_expirience = models.CharField(verbose_name="Общий трудовой стаж", max_length=150, null=True, default="")
    prepod_expirience = models.CharField(verbose_name="Педагогический стаж", max_length=150, null=True, default="")
    sharaga_expirience = models.CharField(verbose_name="Стаж работы в техникуме", max_length=150, null=True, default="")
    contacts = models.TextField(verbose_name="Контакты",null=True, default="")
    degree = models.TextField(verbose_name="Ученая степень/категория", default="нет/нет")

    def __str__(self):
        return f"{self.surname} {self.name[0]}. {self.patronymic[0]}. - {self.disciplines}"

    class Meta():
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class DateTemplates(models.Model):
    name = models.TextField(verbose_name="Название блока")
    date_from = models.DateField(verbose_name="Начало блока")
    date_end = models.DateField(verbose_name="Конец блока")

    def __str__(self):
        return f"{self.id} блок - {self.name}. С {self.date_from} по {self.date_end}"
    class Meta:
        verbose_name = "Блок расписания"
        verbose_name_plural = "Блоки расписания"


class Schedules(models.Model):
    number_pair = models.ForeignKey(Pairs, on_delete=models.CASCADE, verbose_name="Номер пары")
    discipline = models.ForeignKey(Disciplines, on_delete=models.CASCADE, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    prepod = models.ForeignKey(Prepods, on_delete=models.CASCADE, verbose_name="Преподаватель", null=True)
    audience_number = models.CharField(max_length=10, verbose_name="Номер аудитории", null=True, default='')
    date = models.DateField(verbose_name="Дата", null=True, default='')
    block_rasp = models.ForeignKey(DateTemplates, on_delete=models.CASCADE, verbose_name="Блок расписания", null=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name="Корпус", null=True)
    ischange = models.BooleanField(default=False, verbose_name="Замена?")
    iscanceled = models.BooleanField(default=False, verbose_name="Отмена?")
    isdistance = models.BooleanField(default=False, verbose_name="Дистант?")

    def __str__(self):
        return f"{self.date} {self.group} {self.discipline} {self.prepod }"

    class Meta():
        verbose_name = "Строку расписания"
        verbose_name_plural = "Расписание"
        constraints = [
            UniqueConstraint(fields=['date', 'group', 'discipline', 'number_pair', 'prepod', 'ischange'], name='unique_schedul_string')
        ]

class News(models.Model):
    date = models.DateField(verbose_name="Дата новости")
    name = models.CharField(verbose_name="Заголовок", max_length=100, null=False, default='')
    info = models.TextField(verbose_name="Содержимое новости", null=True, default='')
    url = models.URLField(verbose_name="Ссылка на подробную запись", null=True)
    image = models.ImageField(verbose_name="Превью-картинка", null=True, upload_to='server/image')

    def __str__(self):
        return f"{self.date} - {self.name}"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
# -------------------------------- Модели, которые не идут в базу данных

class DaySchedule:
    # инит и переменные внутри были основаны на элементе из миро
    def __init__(self, day, schedules_list):
        self.cur_date = day
        self.lessons = schedules_list

    def __str__(self):
        return  f"{self.cur_date} | {self.lessons}"