from django.shortcuts import render
from . import models as m

# Create your views here.


def home_page(request):
    return render(request, 'index.html')


def rasp_page(request):
    slovar = {"bbb": "расписание еще не выложили, но будет жопа", "groups": ["п50-8-22", "п50-7-22", "п50-6-22"]}
    return render(request, 'rasp.html', context=slovar)


def prepods(request):
    prepodi = m.Teacher.objects.all()
    return render(request, 'Prepodi.html', context={'prepodi': prepodi})

def newFile(request):
    return render(request, 'newfile.html')