from django.shortcuts import render
from . import models as m
from datetime import datetime

from .models import Specialities, Directions, News
from .modules.questions.question_helper import QuestionHelper
from .modules.schedule.schedule_generator import ScheduleGenerator as gen
from .modules.Direction_add import Additions
from .modules.excel.excel_schedule import ExcelParser


# Create your views here.

def home_page(request):
    if request.method == "POST":
        pass
    else:
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

        specialities = Specialities.objects.filter(is_active=True)
        news = News.objects.all()
        try:
            main_news = News.objects.get(is_on_main_page=True)
        except m.News.DoesNotExist:
            main_news = None

        try:
            block_abit = m.Category_of_questions.objects.get(category_name="Абитуриенту")
        except m.Category_of_questions.DoesNotExist:
            block_abit = None
        questions = QuestionHelper.get_questions_with_subcategories(block_abit)

        try:
            block_faq = m.Category_of_questions.objects.get(category_name="Вопрос-ответ")
        except m.Category_of_questions.DoesNotExist:
            block_faq = None
        faq = QuestionHelper.get_questions(block_faq)

        context = {'specialities': specialities, 'news': news, 'main_news': main_news, "questions": questions,
                   "faq": faq}
        return render(request, 'mptsite/index.html', context=context)


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
    # day_rasp = [i for i in day_rasp if len(i.lessons) > 0]
    # print(day_rasp[1].lessons[0].building)
    slovar = {"rasp": day_rasp}
    return render(request, 'mptsite/raspisanie.html', context=slovar)
