import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
import json

class Pair:
    def __init__(self, date, platform, group, number, name, prepod):
        self.date = date
        self.platform = platform
        self.group = group
        self.number = number

        self.name = name
        self.prepod = prepod

    def __str__(self):
        return f"{self.date}|{self.platform}|{self.number}|{self.name} - {self.prepod}"

def format_datetime(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y:%m:%d %H:%M:%S")
    if isinstance(obj, date):
        return obj.strftime("%Y-%m-%d")

def serealiser(pair: Pair):
    return {"date": format_datetime(pair.date), "platform": pair.platform, "group":pair.group, "number":pair.number, "name":pair.name, "prepod":pair.prepod}

class Parser:
    @staticmethod
    def Get_groups(inside=False):
        link = "https://mpt.ru/studentu/raspisanie-zanyatiy/"
        respons = requests.get(link).text
        soup = BeautifulSoup(respons, 'lxml')
        faculty = soup.find_all('div', role="tabpanel")
        groups = dict()  # словарь групп и id в html

        for i in faculty:
            # получение имен всех групп и их id расписания на сайте
            if (i.find('h2') == None):
                groups[(i.find('h3').text).replace('Группа ', '')] = i.get('id')
        if inside:
            return groups
        else:
            return list(groups.keys())
    @staticmethod
    def Get_disps():
        link = "https://mpt.ru/studentu/raspisanie-zanyatiy/"
        respons = requests.get(link).text
        soup = BeautifulSoup(respons, 'lxml')
        groups = Parser.Get_groups(inside=True)

        legendendary = soup.find('span', class_='label').text  # Получение легенды

        disps = []
        pairs_group = dict()
        for g in list(groups.keys()):
            week_schedul = soup.find('div', id=f'{groups[g]}')  # необработанное расписание на неделю
            day_schedul = week_schedul.find_all('table')  # необработанные расписания на 1 день

            for zaniatie in day_schedul:
                raspisanie = zaniatie.find_all('tbody')[-1].find_all('tr')  # расписание на 1 день
                for stroka_raspis in raspisanie:
                    if stroka_raspis.find('th') == None:  # отсеиваются заголовки
                        stlb_rasps = stroka_raspis.find_all('td')  # столбцы  расписания
                        if len(stlb_rasps) == 3:
                            if stlb_rasps[2] == '' or stlb_rasps[2] == None:
                                disps.append(stlb_rasps[1].text)
                            elif stlb_rasps[1].find('div') == None:
                                disps.append(stlb_rasps[1].text)
                            else:
                                ch = 'label label-danger'
                                zn = 'label label-info'

                                cch = str(stlb_rasps[1].find('div', class_=ch).text).replace("\n", '').strip()
                                czn = str(stlb_rasps[1].find('div', class_=zn).text).replace("\n", '').strip()

                                disps.append(cch)
                                disps.append(czn)
        return {'disps': list(set(disps)), 'groups': list(groups.keys()), 'legend':legendendary}

    @staticmethod
    def Get_pairs(json_form=False):
        pairs = []
        # groups = {'П50-8-22': '2084fc05f67bc0c1e78dc7c87b5d1dc2'}
        # groups = {'П50-9-21': '3dfcedbcbe61b166aeefe70959f2bc18'}
        groups = {}
        link = "https://mpt.ru/studentu/raspisanie-zanyatiy/"
        respons = requests.get(link).text
        site_body = BeautifulSoup(respons, "lxml")

        week_days_list = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота"]

        for i in site_body.find_all('div', role = "tabpanel"):
            if (i.find('h2') == None):
                groups[(i.find('h3').text).replace('Группа ', '')] = i.get('id')

        for group in list(groups.keys()):
            week = site_body.find('div', id=f'{groups[group]}')
            days = week.find_all('table')

            start_date = date.fromisoformat("2024-02-05")

            legend = False
            second = False
            while not legend:
                for day in days:
                    day_name = day.find('h4')
                    platform = str(day_name.find('span').text)  # платформа
                    day_id = week_days_list.index(
                        str(day_name.text).replace(day_name.find('span').text, '').replace("\n",
                                                                                           '').lower()) if not second else week_days_list.index(
                        str(day_name.text).replace(day_name.find('span').text, '').replace("\n", '').lower()) + 7
                    actual_date = start_date + timedelta(days=day_id)  # актуальная дата для дня недели

                    raspisanie = day.find_all('tbody')[-1].find_all('tr')[0:-1]
                    legend = False
                    cch, czn, pch, pzn = '', '', '', ''
                    for stroka_raspis in raspisanie:
                        legend = False
                        if stroka_raspis.find('th') == None:  # отсеиваются заголовки
                            stlb_rasps = stroka_raspis.find_all('td')  # столбцы  расписания
                            if len(stlb_rasps) == 3:
                                num = int(stlb_rasps[0].text)
                                if stlb_rasps[2] == '' or stlb_rasps[2] == None:
                                    cch = stlb_rasps[1].text
                                    czn = stlb_rasps[1].text
                                    pch, pzn = ''
                                elif stlb_rasps[1].find('div') == None:
                                    cch = stlb_rasps[1].text
                                    czn = stlb_rasps[1].text
                                    if stlb_rasps[2].find('div') == None:
                                        pch = stlb_rasps[2].text
                                        pzn = stlb_rasps[2].text
                                else:
                                    legend = True
                                    ch = 'label label-danger'
                                    zn = 'label label-info'

                                    cch = str(stlb_rasps[1].find('div', class_=ch).text).replace("\n", '').strip()
                                    czn = str(stlb_rasps[1].find('div', class_=zn).text).replace("\n", '').strip()

                                    pch = str(stlb_rasps[2].find('div', class_=ch).text).replace("\n", '').strip()
                                    pzn = str(stlb_rasps[2].find('div', class_=zn).text).replace("\n", '').strip()
                            if not json_form:
                                if not second:
                                    pairs.append(Pair(actual_date, platform, group, num, cch, pch))
                                else:
                                    pairs.append(Pair(actual_date, platform, group, num, czn, pzn))
                            else:
                                if not second:
                                    pairs.append(serealiser(Pair(actual_date, platform, group, num, cch, pch)))
                                else:
                                    pairs.append(serealiser(Pair(actual_date, platform, group, num, czn, pzn)))
                    if days.index(day) == len(days) - 1 and second == False:
                        second = True
                    elif days.index(day) == len(days) - 1 and second == True:
                        legend = True
        return pairs

