from django.shortcuts import render
from . import models as m
from .modules.Direction_add import Additions
from .modules.Parser_schedule import Parser

# Create your views here.


def home_page(request):
    # Additions.Add_napr()
    # Additions.Add_group()
    # Additions.Add_prep()
    # Additions.Add_disps()
    return render(request, 'index.html')


def rasp_page(request):
    slovar = {"bbb": "расписание еще не выложили, но будет жопа", "groups": ["п50-8-22", "п50-7-22", "п50-6-22"]}
    return render(request, 'rasp.html', context=slovar)


def prepods(request):
    prepodi = m.Teacher.objects.all()
    return render(request, 'Prepodi.html', context={'prepodi': prepodi})

def newFile(request):
    return render(request, 'newfile.html')