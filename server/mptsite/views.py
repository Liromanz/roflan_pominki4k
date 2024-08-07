from django.shortcuts import render
from . import models as m
from datetime import datetime
from .modules.schedule.schedule_generator import ScheduleGenerator as gen
from .modules.Direction_add import Additions
from .modules.excel.excel_schedule import ExcelParser


# Create your views here.

def home_page(request):
    # Additions.Add_zamena()
    # Additions.Add_napr()
    # Additions.Add_speciality()
    # Additions.Add_group()
    # Additions.Add_pairs_numbers()
    # Additions.Add_building()
    # Additions.Add_disps()
    # Additions.Add_prep()
    # Additions.Add_schedule()

    # добавляет группы дисциплины из файла, обьединяет дисциплину с преподом, и делает расписание
    # ExcelParser.import_schedule()
    return render(request, 'mptsite/index.html')


def prepods(request):
    prepodi = m.Teacher.objects.all()
    return render(request, 'mptsite/Prepodi.html', context={'prepodi': prepodi})


def maintest(request):
    return render(request, 'mptsite/topBanner.html')


def prepods(request):
    prepodi = m.Teacher.objects.all()
    return render(request, 'mptsite/Prepodi.html', context={'prepodi': prepodi})

def newFile(request):
    return render(request, 'mptsite/newfile.html')

def newrasp(request):
    group = m.Group.objects.get(name='П50-8-22')

    st = datetime(2024, 3, 4)
    end = datetime(2024, 3, 18)

    day_rasp = gen.generate_by_two_dates(group, st, end)
    #day_rasp = [i for i in day_rasp if len(i.lessons) > 0]
    #print(day_rasp[1].lessons[0].building)
    slovar = {"rasp": day_rasp}
    return render(request, 'mptsite/raspisanie.html', context=slovar)