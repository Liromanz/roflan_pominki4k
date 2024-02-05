from django.shortcuts import render
from . import models as m
from .modules.raspgenerator import RaspGenerator

# Create your views here.


def home_page(request):
    return render(request, 'index.html')


def rasp_page(request):
    rasps = RaspGenerator()
    day_rasp = rasps.GenerateCurrentDay(m.Group.objects.filter(name='П50-8-22')[0])

    slovar = {"rasp": day_rasp}
    return render(request, 'rasp.html', context=slovar)


def prepods(request):
    prepodi = m.Teacher.objects.all()
    return render(request, 'Prepodi.html', context={'prepodi': prepodi})

def newFile(request):
    return render(request, 'newfile.html')