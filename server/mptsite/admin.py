from django.contrib import admin
from . import models as m

# Register your models here.

admin.site.register(m.Pairs)
admin.site.register(m.CodeDirection)
admin.site.register(m.Group)
admin.site.register(m.Prepods)
admin.site.register(m.Building)
admin.site.register(m.Disciplines)


class SchedulesAdmin(admin.ModelAdmin):
    list_display = ('number_pair', 'block_rasp', 'date', 'discipline', 'group')
    list_filter = ('group', )
    search_fields = ('discipline', 'prepod')
    ordering = ('date', 'number_pair')


admin.site.register(m.Schedules, SchedulesAdmin)
admin.site.register(m.Speciality)


class DateTemplatesAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_from', 'date_end')


admin.site.register(m.DateTemplates, DateTemplatesAdmin)
