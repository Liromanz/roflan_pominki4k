from ..models import *
from .Parser_schedule import Parser
from datetime import datetime, date
import requests
import time as tm
import datetime as dt
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

    @staticmethod
    def Add_speciality():
        napr_ids = {}
        for i in CodeDirection.objects.all():
            napr_ids[i.code] = i
        for g in ["П", "БД", "ВД", "Т", "ИС", "ИСиП"]:
            d = Speciality(code=napr_ids["09.02.07"], name=g)
            try:
                d.save()
            except:
                continue
        for g in ["СА"]:
            d = Speciality(code=napr_ids["09.02.06"], name=g)
            try:
                d.save()
            except:
                continue
        for g in ["Э"]:
            d = Speciality(code=napr_ids["09.02.01"], name=g)
            try:
                d.save()
            except:
                continue
        for g in ["Ю"]:
            d = Speciality(code=napr_ids["40.02.01"], name=g)
            try:
                d.save()
            except:
                continue
        for g in ["БИ"]:
            d = Speciality(code=napr_ids["10.02.05"], name=g)
            try:
                d.save()
            except:
                continue

    @staticmethod
    def Add_group():
        for group in Parser.Get_groups():
            print(group)
            for i in range(4):
                if group[0:4-i] in [j.name for j in Speciality.objects.all()]:
                    g = Group(speciality_id=int((Speciality.objects.get(name=f"{group[0:4-i]}")).id), name=group)
                    print(g)
                    try:
                        g.save()
                    except:
                        print('Ошибка')
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
    def Add_building():
        cl = 0
        buildings = {"Нахимовский": "Нахимовский проспект, 21", "Нежинская": "Нежинская, 7"}
        for i in list(buildings.keys()):
            d = Building(id=cl, name=i, address=buildings[i])
            d.save()
            cl += 1

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
        print(*links_obrabot, sep='\n')
        for i in range(len(links_obrabot)):
            tm.sleep(5)
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
    def Add_pairs_numbers():
        cl = 0
        for i in [((8, 30, 0), (10, 0, 0)),((10, 10, 0), (11, 40, 0)),((12, 0, 0), (13, 30, 0)), ((13, 50, 0), (15, 20, 0)), ((15, 30, 0), (17, 0, 0)), ((17, 10, 0), (18, 40, 0))]:
            p = Pairs(id=cl, number=cl+1, time_start=dt.time(*i[0]) , time_end=dt.time(*i[1]))
            p.save()
            cl += 1


    @staticmethod
    def Add_schedule():
        data = Parser.Get_pairs(json_form=True)
        for i in data:
            print(i)
            date_schedul = date.fromisoformat(i['date'])
            number_id = Pairs.objects.get(id=i['number'] - 1)
            group = Group.objects.get(name=f"{i['group']}")
            disp = Disciplines.objects.get(name=f"{i['name']}")
            if i['name'] == 'ПРАКТИКА':
                s = Schedules(number_pair=number_id, discipline=disp, group=group, date=date_schedul)
                s.save()
                continue
            if i['name'] == '':
                continue

            prepod_fio = i['prepod']
            biulding = Building.objects.get(name=f"{i['platform']}") if i['platform'] != '' else None
            cl = 0
            for i in range(len(prepod_fio.split(','))):
                fio = prepod_fio.split(',')[i].split('.')
                prepods_variant = Prepods.objects.filter(surname=fio[2].strip())
                if len(prepods_variant) == 0:
                    p = Prepods(surname=fio[2].strip(), name=fio[0].strip(), patronymic=fio[1].strip())
                    p.save()
                    prepods_variant = Prepods.objects.filter(surname=fio[2].strip())
                for prepod in prepods_variant:
                    if prepod.name.startswith(fio[0].strip()) and prepod.patronymic.startswith(fio[1].strip()):
                        prepod_id = prepod
                        s = Schedules(number_pair=number_id, discipline=disp, group=group, prepod=prepod_id,
                                        date=date_schedul, building=biulding)
                        s.save()

