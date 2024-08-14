from django.contrib import admin
from . import models as m

# Register your models here.

admin.site.register(m.Directions)
admin.site.register(m.Specialities)
admin.site.register(m.Groups)
admin.site.register(m.Buildings)
admin.site.register(m.Disciplines)
admin.site.register(m.Disciplines_Specialities_Hours)
admin.site.register(m.Employees)
admin.site.register(m.Teacher_Disciplines)
admin.site.register(m.Pair_numbers)
admin.site.register(m.Pair_statuses)


class SchedulesAdmin(admin.ModelAdmin):
    list_display = ('pair_number', 'date', 'teacher', 'group', 'is_change')
    list_filter = ('group',)
    search_fields = ('teacher', 'group')
    ordering = ('date', 'pair_number')
    list_editable = ('is_change',)


admin.site.register(m.Schedules, SchedulesAdmin)


class DateTemplatesAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_from', 'date_end')


admin.site.register(m.DateTemplates, DateTemplatesAdmin)


admin.site.register(m.News)
admin.site.register(m.Category_of_questions)
admin.site.register(m.Questions)
