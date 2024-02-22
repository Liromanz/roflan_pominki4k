from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('start/', getting_started_page, name='start'),
]
