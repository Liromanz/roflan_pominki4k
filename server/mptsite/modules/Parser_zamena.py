import requests
from bs4 import BeautifulSoup
from datetime import datetime, date

class Pair:
    def __init__(self, date_zam, group, number, name, prepod, iscanceled, idistance):
        self.date_zam = date_zam
        self.group = group
        self.number = number

        self.name = name
        self.prepod = prepod

        self.iscanceled = iscanceled
        self.idistance = idistance

    def __str__(self):
        # return f"{self.date}|{self.number}|{self.name} - {self.prepod}"
        return f"{self.date_zam}|{self.group}|{self.number}|{self.name}|{self.prepod}|{'Отменено' if self.iscanceled else 'Замена'}|{'Дистант' if self.idistance else ''}"

def format_datetime(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y:%m:%d %H:%M:%S")
    if isinstance(obj, date):
        return obj.strftime("%Y-%m-%d")

def serealiser(pair: Pair):
    return {"date": format_datetime(pair.date_zam), "group":pair.group, "number":pair.number, "name":pair.name, "prepod":pair.prepod, 'iscanceled': pair.iscanceled, 'idistance': pair.idistance}


class Parser_zamena():

    @staticmethod
    def Get_zamens():
        list_zamen = []
        date1 = ''
        link = "https://mpt.ru/studentu/izmeneniya-v-raspisanii/"
        respons = requests.get(link).text
        soup = BeautifulSoup(respons, 'lxml')

        main = soup.find('main')
        main_main = main.find('div', class_="container")
        for i in main_main.find_all(['h4', 'table']):
            # print(i)
            # print("###########")
            if i.name == 'h4':
                date1 = i.find('b').text
                date1 = datetime.strptime(date1, '%d.%m.%Y').date()
                # if __name__ == '__main__':
                #     date1 = i.find('b').text
                #     date1 = datetime.strptime(date1, '%d.%m.%Y').date()
            if i.name == 'table':
                group = i.find('caption').find('b').text.strip()
                # print(group)
                for str_zameni in i.find_all('tr'):
                    if len(str_zameni.find_all('td')) > 0:

                        name_zam_prepod = str_zameni.find_all('td')[2].text.replace('. ', '.')

                        number = str_zameni.find_all('td')[0].text
                        name = ''
                        distant = False


                        prepod = ''
                        if name_zam_prepod == 'Занятие отменено с последующей отработкой' or 'Занятие перенесено' in name_zam_prepod:
                            name = "ОТМЕНА"
                            list_zamen.append(serealiser(Pair(iscanceled=True, idistance=False, group=group, date_zam=date1, prepod=None, name=None, number=number)))
                            print(Pair(iscanceled=True, idistance=False, group=group, date_zam=date1, prepod=None, name=None, number=number))
                            # print(group, number, "ОТМЕНА")
                            continue

                        if "(ДИСТАН" in name_zam_prepod:
                            distant = True

                        name = name_zam_prepod.split('.')[0][:-2].strip().replace("  ", " ")
                        if ',' in name_zam_prepod:
                            for j in name_zam_prepod.split(','):
                                for k in j.split():
                                    if '.' in k:
                                        prepod = k.strip()
                                if 'отменено' in j:
                                    list_zamen.append(serealiser(Pair(iscanceled=True, idistance=distant, group=group,
                                                                      date_zam=date1, prepod=prepod, name=name, number=number)))
                                    print(Pair(iscanceled=True, idistance=distant, group=group,
                                               date_zam=date1, prepod=prepod, name=name, number=number))
                                    # print(group, number, "ОТМЕНА")
                                    continue
                                else:
                                    list_zamen.append(serealiser(Pair(iscanceled=False, idistance=distant, group=group,
                                                                      date_zam=date1, prepod=prepod, name=name, number=number)))
                                    print(Pair(iscanceled=False, idistance=distant, group=group,
                                               date_zam=date1, prepod=prepod, name=name, number=number))
                                    # print(group, number, name, prepod, distant)
                        else:
                            for k in name_zam_prepod.split():
                                if '.' in k:
                                    prepod = k.strip()
                            list_zamen.append(serealiser(Pair(iscanceled=False, idistance=distant, group=group,
                                                              date_zam=date1, prepod=prepod, name=name, number=number)))
                            print(Pair(iscanceled=False, idistance=distant, group=group,
                                       date_zam=date1, prepod=prepod, name=name, number=number))
                            # print(group, number, name, prepod, distant)

                        # zameni.append(Pair(key, platform=0, group=group, number=num, name=name_zam))
        return list_zamen

