from django.test import TestCase
from .models import Directions, Specialities, Groups, Pair_numbers, Buildings, Disciplines, Disciplines_Specialities_Hours, Employees, Teacher_Disciplines, Pair_statuses, DateTemplates


class DirectionsModelTest(TestCase):
    def setUp(self):
        self.direction = Directions.objects.create(code_name="IT", name="Информационные технологии")

    def test_str(self):
        self.assertEqual(str(self.direction), "IT Информационные технологии - Активно")


class SpecialitiesModelTest(TestCase):
    def setUp(self):
        self.direction = Directions.objects.create(code_name="IT", name="Информационные технологии")
        self.speciality = Specialities.objects.create(short_name="IT-9", full_name="Информационные технологии на базе 9",
                                                      base_on_9=True, description="Описание специальности",
                                                      direction=self.direction)

    def test_str(self):
        self.assertEqual(str(self.speciality), "IT - Информационные технологии на базе 9")


class GroupsModelTest(TestCase):
    def setUp(self):
        self.direction = Directions.objects.create(code_name="IT", name="Информационные технологии")
        self.speciality = Specialities.objects.create(short_name="IT-9", full_name="Информационные технологии на базе 9",
                                                      base_on_9=True, description="Описание специальности",
                                                      direction=self.direction)
        self.group = Groups.objects.create(group_name="IT-101", speciality=self.speciality)

    def test_str(self):
        self.assertEqual(str(self.group), "IT-101 - 2")


class PairNumbersModelTest(TestCase):
    def setUp(self):
        self.pair_number = Pair_numbers.objects.create(time_start="09:00", time_finish="10:30")

    def test_str(self):
        self.assertEqual(str(self.pair_number), "09:00 - 10:30")


class BuildingsModelTest(TestCase):
    def setUp(self):
        self.building = Buildings.objects.create(name="Главное здание", address="Улица Примерная, 1")

    def test_str(self):
        self.assertEqual(str(self.building), "Главное здание")


class DisciplinesModelTest(TestCase):
    def setUp(self):
        self.discipline = Disciplines.objects.create(discipline_name="Математика")

    def test_str(self):
        self.assertEqual(str(self.discipline), "Математика")


class DisciplinesSpecialitiesHoursModelTest(TestCase):
    def setUp(self):
        self.direction = Directions.objects.create(code_name="IT", name="Информационные технологии")
        self.speciality = Specialities.objects.create(short_name="IT-9", full_name="Информационные технологии на базе 9",
                                                      base_on_9=True, description="Описание специальности",
                                                      direction=self.direction)
        self.discipline = Disciplines.objects.create(discipline_name="Математика")
        self.hours = Disciplines_Specialities_Hours.objects.create(speciality=self.speciality,
                                                                    discipline=self.discipline,
                                                                    hours_amount=40)

    def test_str(self):
        self.assertEqual(str(self.hours), "IT-9 - Дисциплина Математика 40")


class EmployeesModelTest(TestCase):
    def setUp(self):
        self.employee = Employees.objects.create(surname="Иванов", name="Иван", patronymic="Иванович")

    def test_str(self):
        self.assertEqual(str(self.employee), "Иванов И. И.")


class TeacherDisciplinesModelTest(TestCase):
    def setUp(self):
        self.direction = Directions.objects.create(code_name="IT", name="Информационные технологии")
        self.speciality = Specialities.objects.create(short_name="IT-9", full_name="Информационные технологии на базе 9",
                                                      base_on_9=True, description="Описание специальности",
                                                      direction=self.direction)
        self.discipline = Disciplines.objects.create(discipline_name="Математика")
        self.employee = Employees.objects.create(surname="Иванов", name="Иван", patronymic="Иванович")
        self.teacher_discipline = Teacher_Disciplines.objects.create(discipline=self.discipline, employee=self.employee)

    def test_str(self):
        self.assertEqual(str(self.teacher_discipline), "Математика - Иванов И. И.")


class PairStatusesModelTest(TestCase):
    def setUp(self):
        self.status = Pair_statuses.objects.create(name="Запланировано")

    def test_str(self):
        self.assertEqual(str(self.status), "Запланировано")


class DateTemplatesModelTest(TestCase):
    def setUp(self):
        self.date_template = DateTemplates.objects.create(name="Семестр 1", date_from="2023-09-01", date_end="2024-01-15")

    def test_str(self):
        self.assertEqual(str(self.date_template), "Семестр 1: с 2023-09-01 по 2024-01-15")