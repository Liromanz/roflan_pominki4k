from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home_page),
    path('prepodi/', v.prepods),
    path('newfile/', v.newFile),
    path('rsp/', v.newrasp, name='rasp'),
    path('not_auth_student/', v.not_auth_student),
    # path('lupapupa/<int:num>/', v.prepods)
]
