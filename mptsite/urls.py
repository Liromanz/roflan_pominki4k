from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home_page),
    path('prepodi/', v.prepods),
    path('newfile/', v.newFile),
    # path('rsp/', v.newrasp, name='rasp')
    path('schedule/', v.schedule)
    # path('lupapupa/<int:num>/', v.prepods)
]
