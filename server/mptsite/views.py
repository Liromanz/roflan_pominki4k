from django.shortcuts import render
from . import models as m
import datetime
from .modules.schedule_generator import ScheduleGenerator as gen
from .modules.Direction_add import Additions
from .modules.schedule_generator import ScheduleGenerator


# Create your views here.


def home_page(request):
    return render(request, 'index.html')
    # Additions.Add_napr()
    # Additions.Add_speciality()
    # Additions.Add_group()
    # Additions.Add_pairs_numbers()
    # Additions.Add_building()
    # Additions.Add_disps()
    # Additions.Add_prep()
    # Additions.Add_schedule()

def rasp_page(request):

    ### Вариация расписания на сегодняшний день. Передаем только группу
    #day_rasp = ScheduleGenerator.generate_by_day(m.Group.objects.filter(name='П50-8-22')[0])

    ### Вариация расписания на выбранный день. Передаем группу и дату
    #day_rasp = ScheduleGenerator.generate_by_day(m.Group.objects.filter(name='П50-8-22')[0], date(2024, 2, 6))

    ### Вариация расписания на текущую неделю. Передаем только группу
    #day_rasp = ScheduleGenerator.generate_current_week(m.Group.objects.filter(name='П50-8-22')[0])

    ### Вариация расписания на следующую неделю. Передаем только группу
    #day_rasp = ScheduleGenerator.generate_next_week(m.Group.objects.filter(name='П50-8-22')[0])

    ### Вариация расписания на промежуток дней. Передаем группу, стартовую дату и дату окончания
    #day_rasp = ScheduleGenerator.generate_by_two_dates(m.Group.objects.filter(name='П50-8-22')[0],
    #                                                   date(2024, 2, 6), date(2024, 2, 14))

    group = m.Group.objects.get(name='П50-8-22')

    st = datetime.date.fromisoformat('2024-02-05')
    end = datetime.date.fromisoformat('2024-02-18')

    day_rasp = gen.generate_by_two_dates(group, st, end)
    # day_rasp = [i for i in day_rasp if len(i.lessons) > 0]
    # print(day_rasp[1].lessons[0].building)
    slovar = {"rasp": day_rasp}
    return render(request, 'mptsite/rasp.html', context=slovar)


def prepods(request):
    prepodi = m.Teacher.objects.all()
    return render(request, 'mptsite/Prepodi.html', context={'prepodi': prepodi})

def newFile(request):
    return render(request, 'mptsite/newfile.html')

def newrasp(request):
    group = m.Group.objects.get(name='П50-8-22')

    st = datetime.date.fromisoformat('2024-02-05')
    end = datetime.date.fromisoformat('2024-02-18')

    day_rasp = gen.generate_by_two_dates(group, st, end)
    #day_rasp = [i for i in day_rasp if len(i.lessons) > 0]
    #print(day_rasp[1].lessons[0].building)
    slovar = {"rasp": day_rasp}
    return render(request, 'mptsite/raspisanie.html', context=slovar)