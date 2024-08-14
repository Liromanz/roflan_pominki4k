from django.contrib import admin
from .models import (
    Directions,
    Specialities,
    Groups,
    Pair_numbers,
    Buildings,
    Disciplines,
    Disciplines_Specialities_Hours,
    Employees,
    Teacher_Disciplines,
    Pair_statuses,
    DateTemplates,
    Schedules,
    Users,
    News,
    Category_of_questions,
    Subcategory_of_questions,
    Questions
)

@admin.register(Directions)
class DirectionsAdmin(admin.ModelAdmin):
    list_display = ('code_name', 'name', 'is_active')
    search_fields = ('code_name', 'name')

@admin.register(Specialities)
class SpecialitiesAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'full_name', 'is_active', 'direction')
    search_fields = ('short_name', 'full_name')
    list_filter = ('direction',)

@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'speciality', 'course')
    search_fields = ('group_name',)
    list_filter = ('speciality',)

@admin.register(Pair_numbers)
class PairNumbersAdmin(admin.ModelAdmin):
    list_display = ('time_start', 'time_finish')

@admin.register(Buildings)
class BuildingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

@admin.register(Disciplines)
class DisciplinesAdmin(admin.ModelAdmin):
    list_display = ('discipline_name',)

@admin.register(Disciplines_Specialities_Hours)
class DisciplinesSpecialitiesHoursAdmin(admin.ModelAdmin):
    list_display = ('speciality', 'discipline', 'hours_amount')
    search_fields = ('speciality__full_name', 'discipline__discipline_name')

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'post')
    search_fields = ('surname', 'name', 'patronymic')

@admin.register(Teacher_Disciplines)
class TeacherDisciplinesAdmin(admin.ModelAdmin):
    list_display = ('discipline', 'employee')
    search_fields = ('discipline__discipline_name', 'employee__surname')

@admin.register(Pair_statuses)
class PairStatusesAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(DateTemplates)
class DateTemplatesAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_from', 'date_end')

@admin.register(Schedules)
class SchedulesAdmin(admin.ModelAdmin):
    list_display = ('pair_number', 'group', 'building', 'date', 'teacher', 'is_change', 'is_cancel')
    search_fields = ('group__group_name',)

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('token', 'secret_user', 'sex', 'birth_date', 'group')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'short_description', 'date_to')
    search_fields = ('name', 'short_description')

@admin.register(Subcategory_of_questions)
class SubcategoryOfQuestionsAdmin(admin.ModelAdmin):
    list_display = ('subcategory_name',) 
   
@admin.register(Category_of_questions)
class CategoryOfQuestionsAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('question', 'category_id')
    search_fields = ('question',)