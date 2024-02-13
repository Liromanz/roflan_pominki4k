import requests
from bs4 import BeautifulSoup
from datetime import datetime


class Day:
    def __init__(self, name, platform, classes):
        self.name = name
        self.platform = platform
        self.classes = classes


class MPT_class:
    def __init__(self, number, legend, name_ch, name_zn, prepod_ch, prepod_zn):
        self.number = number
        self.legend = legend

        self.name_ch = name_ch
        self.name_zn = name_zn
        self.prepod_ch = prepod_ch
        self.prepod_zn = prepod_zn

    def getter(self):
        if self.legend == False:
            print(f"{self.number} {self.name_ch} {self.prepod_ch}")
        else:
            print(f"{self.number} {self.name_ch} {self.prepod_ch} / {self.name_zn} {self.prepod_zn}")

    def __eq__(self, other):
        return self.number == other.number

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
            week_schedul = soup.find('div', id=f'{groups[g]}')  # необработанное расписание на неделю #TODO Заглушка
            day_schedul = week_schedul.find_all('table')  # необработанные расписания на 1 день

            list_days = []
            l_mpt_cls_days = []


            for zaniatie in day_schedul:
                day_name = zaniatie.find('h4')  # имя дня и площадка
                raspisanie = zaniatie.find_all('tbody')[-1].find_all('tr')  # расписание на 1 день
                day_cls = []  # Список занятий на день
                num = 0
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
                                disps.append(stlb_rasps[1].text)
                            elif stlb_rasps[1].find('div') == None:
                                disps.append(stlb_rasps[1].text)
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

                                disps.append(cch)
                                disps.append(czn)

                        if len(day_cls) > 0:
                            if day_cls[-1] != MPT_class(num, legend, cch, czn, pch, pzn):
                                day_cls.append(MPT_class(num, legend, cch, czn, pch, pzn))
                        else:
                            day_cls.append(MPT_class(num, legend, cch, czn, pch, pzn))
                l_mpt_cls_days.append(day_cls)
                list_days.append(Day(str(day_name.text).replace(day_name.find('span').text, '').replace("\n", ''),
                                     str(day_name.find('span').text), day_cls))
                pairs_group[g] = list_days
                day_cls = []
        return {'disps': list(set(disps)), 'groups': list(groups.keys()), 'pairs': pairs_group, 'legend':legendendary}
    @staticmethod
    def Get_schedule():
        pass

