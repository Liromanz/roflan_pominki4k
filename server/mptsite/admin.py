from django.contrib import admin
from . import models as m

# Register your models here.

admin.site.register(m.Pairs)
admin.site.register(m.CodeDirection)
admin.site.register(m.Group)
admin.site.register(m.Prepods)
admin.site.register(m.Building)
admin.site.register(m.Disciplines)
admin.site.register(m.Schedules)
admin.site.register(m.Speciality)