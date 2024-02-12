import requests
from bs4 import BeautifulSoup
class Parser:
    @staticmethod
    def Get_disps():
        link = "https://mpt.ru/studentu/raspisanie-zanyatiy/"

        respons = requests.get(link).text
        soup = BeautifulSoup(respons, 'lxml')

        faculty = soup.find_all('div', role = "tabpanel")
        groups = dict()

        for i in faculty:
            # получение имен всех групп и их id расписания на сайте
            if (i.find('h2') == None):
                groups[(i.find('h3').text).replace('Группа ', '')] = i.get('id')


        disps = []
        for g in list(groups.keys()):
            raspis_soup = soup.find('div', id=f'{groups[g]}')
            day_rasp = raspis_soup.find_all('table') # необработанное расписнаие на 1 день
            for zaniatie in day_rasp:
                raspisanie = zaniatie.find_all('tbody')[-1].find_all('tr') # расписание на 1 день
                for stroka_raspis in raspisanie:
                    if stroka_raspis.find('th') == None: # отсеиваются заголовки
                        stlb_rasps = stroka_raspis.find_all('td') # столбцы  расписания
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
        return list(set(disps))


    @staticmethod
    def Get_schedule():
        pass

