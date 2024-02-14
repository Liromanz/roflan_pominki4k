from ..models import *
from .Parser_schedule import Parser
from datetime import datetime
import requests
from bs4 import BeautifulSoup
class Additions:
    @staticmethod
    def Add_napr():
        napr = {"09.02.01":"Компьютерные системы и комплексы","09.02.06":"Сетевое и системное администрирование", "09.02.07":"Информационные системы и программирование","10.02.05":"Обеспечение информационной безопасности автоматизированных систем","40.02.01":"Право и организация социального обеспечения"}
        for i in list(napr.keys()):
            d = CodeDirection(code=i, name=napr[i])
            try:
                d.save()
            except:
                continue

    # @staticmethod
    # def Add_speciality():


    @staticmethod
    def Add_speciality():
        napr_ids = {}
        for i in CodeDirection.objects.all():
            napr_ids[i.code] = i.id
        for g in ["П", "БД", "ВД", "Т", "ИС", "ИСиП"]:
            d = Speciality(code=napr_ids["09.02.07"], name = g)
            try:
                d.save()
            except:
                continue
        for g in ["CА"]:
            d = Speciality(code=napr_ids["09.02.06"], name = g)
            try:
                d.save()
            except:
                continue
        for g in ["Э"]:
            d = Speciality(code=napr_ids["09.02.01"], name = g)
            try:
                d.save()
            except:
                continue
        for g in ["Ю"]:
            d = Speciality(code=napr_ids["40.02.01"], name = g)
            try:
                d.save()
            except:
                continue
        for g in ["БИ"]:
            d = Speciality(code=napr_ids["10.02.05"], name = g)
            try:
                d.save()
            except:
                continue

    @staticmethod
    def Add_group():
        Parser.Get_groups()
        for group in Parser.Get_groups():
            for i in range(4):
                if group[0:4-i] in [j.name for j in Speciality.objects.all()]:
                    g = Group(speciality_id=int((Speciality.objects.get(name=f"{group[0:4-i]}")).id), name=group)
                    try:
                        g.save()
                    except:
                        break
                    break

    @staticmethod
    def Add_disps():
        for i in Parser.Get_disps()['disps']:
            d = Disciplines(name=i)
            try:
                d.save()
            except:
                continue

    @staticmethod
    def Add_prep():
        link = "https://www.xn--p1ag3a.xn--p1ai/structure/kolledji-i-tehnikum/moskovskiy-priborostroitelnyiy-tehnikum#section-17706"
        respons = requests.get(link).text
        soup = BeautifulSoup(respons, 'lxml')

        menu_prepodov = soup.find('div', id="collapse17706")
        links = menu_prepodov.find_all("a")
        links_obrabot = []
        for i in links:
            if i.get('href')[i.get('href').find('kolledji')::] != 'x':
                links_obrabot.append(i.get('href')[i.get('href').find('kolledji')::])

        for i in range(len(links_obrabot)):
            link = f"https://www.xn--p1ag3a.xn--p1ai/structure/{links_obrabot[i]}"
            respons = requests.get(link).text
            prepod_html = BeautifulSoup(respons, 'lxml')

            FIO = prepod_html.find("h1", class_="inner-title").text.strip()

            prepod_card = prepod_html.find('div', class_="inner-page-content clearfix").text.replace('&nbsp;', '')
            Education = prepod_card[prepod_card.find("Образование:"):prepod_card.find(
                "Данные о повышении квалификации и (или) профессиональной подготовки:")].replace('Образование:', '').strip()
            # print(Education)
            Qualification = prepod_card[prepod_card.find(
                "Данные о повышении квалификации и (или) профессиональной подготовки:"):prepod_card.find(
                "Должность:")].replace('Данные о повышении квалификации и (или) профессиональной подготовки:', '').strip()
            # print(Qualification)
            Post = prepod_card[prepod_card.find("Должность:"):prepod_card.find("Преподаваемые дисциплины:")].replace(
                'Должность:', '').strip()
            # print(Post)
            Disciplines = prepod_card[
                          prepod_card.find("Преподаваемые дисциплины:"):prepod_card.find("Общий трудовой стаж:")].replace(
                'Преподаваемые дисциплины:', '').strip()
            # print(Disciplines)
            Full_expirience = prepod_card[
                              prepod_card.find("Общий трудовой стаж:"):prepod_card.find("Педагогический стаж:")].replace(
                'Общий трудовой стаж:', '').strip()
            # print(Full_expirience)

            Prepod_expirience = prepod_card[prepod_card.find("Педагогический стаж:"):prepod_card.find(
                "Стаж работы в техникуме:")].replace('Педагогический стаж:', '').strip()
            # print(Prepod_expirience)

            Sharaga_expirience = prepod_card[prepod_card.find("Стаж работы в техникуме:"):prepod_card.find(
                "Контактные данные:")].replace('Стаж работы в техникуме:', '').strip()
            # print(Sharaga_expirience)

            Contacts = prepod_card[
                       prepod_card.find("Контактные данные:"):prepod_card.find("Ученая степень/категория")].replace(
                'Контактные данные:', '').strip()
            # print(Contacts)
            Degree = prepod_html.find('div', class_="inner-page-content clearfix").find_all('p')[-1].text.replace(
                'Ученая степень/категория:', '').strip()
            # print(Degree)
            t = Prepods(Name=FIO.split()[1], Surname=FIO.split()[0], Patronymic=FIO.split()[2], Education=Education, Qualification=Qualification, Post=Post, Disciplines=Disciplines, Full_expirience=Full_expirience, Prepod_expirience=Prepod_expirience, Sharaga_expirience=Sharaga_expirience, Contacts=Contacts, Degree=Degree)
            t.save()


    @staticmethod
    def Add_raspisanie():
        data = Parser.Get_disps()
        current_legend = data['legend'] #легенда текущей недели
        groups_schedule = data['pairs'] #словарь группа - дни недели с парами

        t = datetime.today().weekday()

        s = Schedules()



