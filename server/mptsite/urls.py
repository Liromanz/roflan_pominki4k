from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page),
    path('rasp/', rasp_page),
    path('prepodi/', prepods),
    path('newfile/', newFile),
    # path('lupapupa/<int:num>/', v.prepods)
]
