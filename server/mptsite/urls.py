from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home_page),
    path('rasp/', v.rasp_page, name='rasp'),
    path('prepodi/', v.prepods),
    path('newfile/', v.newFile),
]
