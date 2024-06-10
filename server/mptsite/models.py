from django.db import models
from django.db.models import UniqueConstraint


class Directions(models.Model):
    code_name = models.CharField(max_length=50, verbose_name="Код направления", unique=True, null=False)
    name = models.TextField(verbose_name="Название направления", unique=True, null=False)
    is_active = models.BooleanField(null=False, default=True)

    def __str__(self):
        return f"{self.code_name} {self.name} - {'Активно' if self.is_active else 'Не активно'}"

    class Meta():
        verbose_name = "Направление"
        verbose_name_plural = "Направления"


class Specialities(models.Model):
    short_name = models.CharField(verbose_name="Краткое название", max_length=10, null=False, unique=True)
    full_name = models.CharField(verbose_name="Полное название", max_length=150, null=False)
    base_on_9 = models.BooleanField(verbose_name="На базе 9-го", null=False, default=False)
    base_on_11 = models.BooleanField(verbose_name="На базе 11-го", null=False, default=False)
    description = models.TextField(verbose_name="Описание", null=False, default="")
    direction = models.ForeignKey(Directions, on_delete=models.CASCADE, null=True, verbose_name="Направление")

    def __str__(self):
        return f"{self.short_name} - {self.direction}"

    class Meta():
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"


class Groups(models.Model):
    group_name = models.CharField(max_length=50, verbose_name="Название группы", unique=True, null=False)
    speciality = models.ForeignKey(Specialities, on_delete=models.CASCADE, null=False, verbose_name="Специальность")
    course = models.IntegerField(verbose_name="Курс", default=2)

    def __str__(self):
        return f"{self.group_name} - {self.course}"

    class Meta():
        verbose_name = "Группу"
        verbose_name_plural = "Группы"


class Pair_numbers(models.Model):
    time_start = models.CharField(max_length=20, verbose_name="Начало пары", null=False)
    time_finish = models.CharField(max_length=20, verbose_name="Конец пары")

    def __str__(self):
        return f"{self.time_start} - {self.time_finish}"

    class Meta():
        verbose_name = "Время пары"
        verbose_name_plural = "Время пары"


class Buildings(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название", null=False, unique=True)
    address = models.TextField(verbose_name="Адрес", null=False, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta():
        verbose_name = "Здание"
        verbose_name_plural = "Здания"


class Disciplines(models.Model):
    discipline_name = models.CharField(max_length=200, verbose_name="Название дисциплины", unique=True, null=False)

    def __str__(self):
        return f"{self.discipline_name}"

    class Meta():
        verbose_name = "Дисциплину"
        verbose_name_plural = "Направления"


class Disciplines_Specialities_Hours(models.Model):
    speciality = models.ForeignKey(Specialities, on_delete=models.CASCADE, verbose_name="Специальность")
    discipline = models.ForeignKey(Disciplines, on_delete=models.CASCADE, verbose_name="Дисциплина")
    hours_amount = models.PositiveIntegerField(verbose_name="Время по рабочему плану", default=0, null=True)

    def __str__(self):
        return f"{self.speciality.name} - Дисциплина {self.discipline.name} {self.hours_amount} "

    class Meta():
        verbose_name = "Количество часов"
        verbose_name_plural = "Количества часов"


class Employees(models.Model):
    surname = models.CharField(verbose_name="Фамилия", max_length=50, default="")
    name = models.CharField(verbose_name="Имя", max_length=50, null=False, default='')
    patronymic = models.CharField(verbose_name="Отчество", max_length=50, null=True, default="")
    education = models.TextField(verbose_name="Образование", null=True, default="")
    qualification = models.TextField(verbose_name="Квалификация", null=True, default="")
    post = models.CharField(verbose_name="Должность", max_length=300, null=True, default="")
    total_work_experience = models.TextField(verbose_name="Общий стаж работы", null=True, default="")
    teaching_work_experience = models.TextField(verbose_name="Педагогический стаж", null=True, default="")
    teaching_work_experience_MPT = models.TextField(verbose_name="Стаж рабооты в техникуме", null=True, default="")
    phone = models.CharField(max_length=20, verbose_name="Телефон", null=True, default="")
    email = models.EmailField(max_length=300, verbose_name="Почта", null=True, default="")
    degree = models.TextField(verbose_name="Ученая степень")

    def __str__(self):
        return f"{self.surname} {self.name[0]}. {self.patronymic[0]}. "

    class Meta():
        verbose_name = "Работника"
        verbose_name_plural = "Работники"


class Teacher_Disciplines(models.Model):
    discipline = models.ForeignKey(Disciplines, on_delete=models.CASCADE, verbose_name="Дисциплина")
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, verbose_name="Сотрудник")

    def __str__(self):
        return f"{self.discipline.name} - {self.employee.surname} {self.employee.name[0]}. {self.employee.patronymic[0]}."

    class Meta():
        verbose_name = "Преподаваемую дисциплину"
        verbose_name_plural = "Преподаваемые дисциплины"
        unique_together = ('discipline', 'employee',)


class Pair_statuses(models.Model):
    name = models.CharField(verbose_name="Название статуса", max_length=50, null=False, default='')

    def __str__(self):
        return f"{self.name}"

    class Meta():
        verbose_name = "Статус пары"
        verbose_name_plural = "Статусы пар"


class DateTemplates(models.Model):
    name = models.CharField(verbose_name="Название статуса", max_length=50, null=False, default='')
    date_from = models.DateField(verbose_name='Блок с')
    date_end = models.DateField(verbose_name='Блок по')

    def __str__(self):
        return f"{self.name}: с {self.date_from} по {self.date_end}"

    class Meta():
        verbose_name = "Блок расписания"
        verbose_name_plural = "Блоки генерации расписания"


class Schedules(models.Model):
    pair_number = models.ForeignKey(Pair_numbers, on_delete=models.CASCADE, null=False, verbose_name="Номер пары")
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, null=False, verbose_name="Группа")
    audience = models.CharField(max_length=10, verbose_name="Аудитория", null=True, default="")
    building = models.ForeignKey(Buildings, on_delete=models.CASCADE, null=False, verbose_name="Корпус")
    date = models.DateField(verbose_name="Дата проведения", null=True)
    teacher = models.ForeignKey(Teacher_Disciplines, on_delete=models.CASCADE, verbose_name="Преподаватель")
    is_change = models.BooleanField(verbose_name="Является заменой?", null=False, default=False)
    is_cancel = models.ForeignKey(Pair_statuses, on_delete=models.CASCADE, verbose_name="Отмена?", null=True, default=None)
    is_remote = models.BooleanField(verbose_name='Дистанционно?', null=False, default=False)

    def __str__(self):
        return f"{self.pair_number.pk} {self.group.group_name} {self.audience} {self.building} {self.date}"


class Users(models.Model):
    token = models.CharField(verbose_name='Токен доступа', max_length=256, null=False, blank=False, unique=True)
    secret_user = models.CharField(verbose_name='Секрет пользователя', max_length=256, null=False, blank=False,
                                   unique=True)
    sex = models.BooleanField(verbose_name='Мужчина?', null=False, default=False)
    birth_date = models.DateField(verbose_name='Дата рождения', null=False)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, null=True, verbose_name="Группа")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class News(models.Model):
    date = models.DateField(verbose_name="Дата новости")
    name = models.CharField(verbose_name="Заголовок", max_length=100, null=False, default='')
    description = models.TextField(verbose_name="Содержимое новости", null=True, default='')
    link = models.URLField(verbose_name="Ссылка на подробную запись", null=True)
    picture = models.ImageField(verbose_name="Превью-картинка", null=True, upload_to='server/static/mptsite/img/news')
    short_description = models.CharField(verbose_name="Краткое описание", max_length=100, null=False, default='')
    date_to = models.DateField(verbose_name="Актуально до", null=False)

    def __str__(self):
        return f"{self.date} - {self.name}"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Category_of_questions(models.Model):
    category_name = models.CharField(verbose_name="Наименование категории", max_length=100, null=False)

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        verbose_name = "Категория вопроса"
        verbose_name_plural = "Категории вопросов"


class Questions(models.Model):
    question = models.CharField(verbose_name="Вопрос", max_length=300, null=False)
    answer = models.TextField(verbose_name="Ответ", null=False)
    category_id = models.ForeignKey(Category_of_questions, on_delete=models.CASCADE, verbose_name="Категория",
                                    null=False)

    def __str__(self):
        return f"Вопрос: {self.question}"

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


# -------------------------------- Модели, которые не идут в базу данных

class DaySchedule:
    # инит и переменные внутри были основаны на элементе из миро
    def __init__(self, day, schedules_list):
        self.cur_date = day
        self.lessons = schedules_list

    def __str__(self):
        return f"{self.cur_date} | {self.lessons}"
