from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home_page, name='main_page'),
    path('prepodi/', v.prepods),
    path('newfile/', v.newFile),
    path('not_auth_student/', v.not_auth_student, name='not_auth_stud'),
    path('schedule/', v.schedule, name='schedule')
    # path('lupapupa/<int:num>/', v.prepods)
]
