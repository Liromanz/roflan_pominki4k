from django.db import models

# Create your models here.


class Teacher(models.Model):
    First_name = models.CharField(verbose_name="Фамилия", max_length=30)
    Name = models.CharField(verbose_name="Имя",max_length=20)
    Patronymic = models.CharField(verbose_name="Отчество",max_length=30, null=True, default="")
    Education = models.TextField(verbose_name="Образование",)
    Qualification = models.TextField(verbose_name="Данные о повышении квалификации",null=True, default="")
    Post = models.CharField(verbose_name="Должность",max_length=100)
    Disciplines = models.CharField(verbose_name="Преподаваемые дисциплины",max_length=100)
    Full_expirience = models.IntegerField(verbose_name="Общий трудовой стаж",)
    Prepod_expirience = models.IntegerField(verbose_name="Педагогический стаж",)
    Sharaga_expirience = models.IntegerField(verbose_name="Стаж работы в техникуме",)
    Contacts = models.EmailField(verbose_name="Контакты",null=True, default="")
    Degree = models.TextField(verbose_name="Ученая степень\категория",max_length=50, default="нет")

    def __str__(self):
        return f"{self.First_name} {self.Name[0]}. {self.Patronymic[0]}. - {self.Disciplines}"

    class Meta():
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
