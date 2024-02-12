import requests
from bs4 import BeautifulSoup

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

    def class_to_dict(obj):
        return obj.__dict__

class JSONDataAdapter:
    @staticmethod
    def to_json(o):
        if isinstance(o, Day):
            return ({
                "name": o.name,
                "platform": o.platform,
                "classes": o.classes,
            })
        if isinstance(o, MPT_class):
            return ({
                "number": o.number,
                "legend": o.legend,
                "name_ch": o.name_ch,
                "name_zn": o.name_zn,
                "prepod_ch": o.prepod_ch,
                "prepod_zn": o.prepod_zn,
            })

    def getter(self):
        if self.legend == False:
            print(f"{self.number} {self.name_ch} {self.prepod_ch}")
        else:
            print(f"{self.number} {self.name_ch} {self.prepod_ch} / {self.name_zn} {self.prepod_zn}")



link = "https://mpt.ru/studentu/raspisanie-zanyatiy/"

respons = requests.get(link).text
# respons = open(r"C:\Users\serge\OneDrive\Рабочий стол\site.txt", 'r')
soup = BeautifulSoup(respons, 'lxml')

faculty = soup.find_all('div', role = "tabpanel")
groups = dict()

for i in faculty:
    # получение имен всех групп и их id расписания на сайте
    if (i.find('h2') == None):
        groups[(i.find('h3').text).replace('Группа ', '')] = i.get('id')


# groups = {'Э-1-20': 'c9b8fc80cb5cb97cb5d053754f366f80', 'Э-1-21, Э-11/1-22': 'd510b3c7198aef53c1deef68d0df4915', 'Э-1-22, Э-11/1-23': 'f45ba40bbd5cd619d6af4c4c4c0d6a53', 'Э-2-20, Э-11-21': '6cd2a1f6b9bd94fb664f40b9a6d5d533', 'Э-2-21, Э-11/2-22': 'ee931d754e68bcd82d27db2fa71f1db7', 'Э-2-22, Э-11/2-23': '012ce303b4bcba51f7710d0a668e1281', 'СА50-1-20': '42c56c74dfe954481279bb9ca281181a', 'СА50-1-21': 'ab7318d0dd24601782beb820d32f29ec', 'СА50-1-22': '0d8f931a2d0492196ccbaa1f44f1bfcc', 'СА50-2-20': '89c33b6dbacd0a81aca9efd6bbd79224', 'СА50-2-21': '80e87f6d98a73b3fb9f10c59586d7d30', 'СА50-2-22': 'b0a2d49c52fc2bb719dc4301d496fec7', 'СА50-3-20': '29178907cf306cf25bdc50e54e5e1085', 'СА50-3-22': 'def2b2669f02b9211e97044fcd5d70ae', 'СА50-4-22': '174acdaadc8655e2af30c824c66bef80', 'БД50-1-20': '1bef25a0f9383494916ad9cd272a8449', 'БД50-1-21, БД50-11-22': 'f2825c1784109c84cd6994c929029a1e', 'БД50-1-22, БД50-11-23': '6099f972988df0aa54de97e777c1f922', 'ВД50-1-20, ВД50-11/1-21': 'c3373e875e5c0add80303fbb9a47ef2f', 'ВД50-1-21': 'ad1f7e3f21668a4636e82b27e6d072c1', 'ВД50-1-22': 'c9fa3fd9c62f5ec5b03e443b13c53961', 'ВД50-2-20, ВД50-11/2-21': 'c9fac56b75d5aceb40135797d627f267', 'ВД50-2-21': '62b622b043c1ef5fcf6ae11b647f3b17', 'ВД50-2-22': 'ed4c06aef5e313300ce768a887d63161', 'ВД50-3-20, ВД50-11/3-21': 'b24723d1f5375935f649826f7db8e91f', 'ВД50-3-21': '73994db9d549ff8ade14c234e4a5d1af', 'ВД50-3-22': 'a954a2c55059e1a0fdb8f944a4ad2f95', 'ВД50-4-20, ВД50-11/4-21': 'b807e244770a32947346dc3d19f44975', 'ВД50-4-21': 'b3668d2bb3d9e58d1ddfd63def396d94', 'ВД50-4-22': '176643b92cf44a5d2289a58450f53a7e', 'ВД50-5-22': 'c4fc247bef51a2be9e06f7223db7499a', 'ИС50-1-20': '41969f423ef6ac6226676e1a70f7b354', 'ИС50-1-21, ИС50-11/1-22': 'd7c1b2a940d78e478f46649a69d5ed26', 'ИС50-1-22, ИС50-11/1-23': 'c57ac702afda85e535f350ffd2681bd1', 'ИС50-11-22': 'da91920488311dff7153ba8c2c960086', 'ИС50-11-23': '3683a58ea0d8f1d0f608af10026b3dba', 'ИС50-2-20': 'dd731162a29e5b4d7afc0b6ad24502f6', 'ИС50-2-21, ИС50-11/2-22': '12579b0c2525209cfeb9e7d02992e9db', 'ИС50-2-22, ИС50-11/2-23': 'c528bf5bd0d66718c21a8d2080c5c64a', 'ИС50-3-20, ИС50-11-21': '152f521df877c79e24cbb79a7068bd2d', 'ИС50-3-22, ИС50-11/3-23': '518536b9647630be7bba2b6c67aeb80b', 'П50-1-20': '400591ce031159c882eaeac3b922ebb9', 'П50-1-21': 'b6900d310f951feac4d68463ad97b84e', 'П50-1-22': '547d6879a78127f998297406f017cece', 'П50-2-20': '88fd6ce682c9414485b86527be5b43e1', 'П50-2-21': 'e137bc0e5c25290e7451809fd2c96880', 'П50-2-22': '33da51a5ed9013fab3a76ca0748c69ac', 'П50-3-20': '9618c8e6a0fc06623acf30e191026ec8', 'П50-3-21': 'b886101a7b4a9fb0535a5e89559d1068', 'П50-3-22': '6f7d733351a1236c5525de60207f98e0', 'П50-4-20': 'e26b91992a6a75a1ee7a24ff17306ca7', 'П50-4-21': 'f5e3bc922e59880aa95466eb58e1cdd0', 'П50-4-22': 'ed9535653ee8d9d90a32e07431830bd9', 'П50-5-20': '731a5b47ed6405e173bfe11f45fe91ca', 'П50-5-21': 'c6d425c1da82a022ae1673b94eca6c2e', 'П50-5-22': '0d58fa5065760beec044e076c41be265', 'П50-6-20, П50-11-21': '8393aed93f11caef18cfae0f7e21f53c', 'П50-6-21': '6d61e835e2fda4115c88b82b56ab768b', 'П50-6-22': 'b975cfe8145d3dbd461e8634767e9642', 'П50-7-20': 'e30f0f9b55eb39fb9a016b482908fe04', 'П50-7-21': '865361ab66bc6c1d98a01644e82c4e88', 'П50-7-22': 'd42ac47c8d287459fe7273d6c465e53f', 'П50-8-21': '68dc3ce2de0de1450d7d28113654945e', 'П50-8-22': '2084fc05f67bc0c1e78dc7c87b5d1dc2', 'П50-9-21': '3dfcedbcbe61b166aeefe70959f2bc18', 'Т50-1-20': '1f2afaaf4f6e9fa555a5aa4037621195', 'Т50-1-21': '8283abf1536af48ec954c94aa0170660', 'Т50-1-22, Т50-11/1-23': 'a8f2a926ed9320ac5e0b41069c8bcff0', 'Т50-11/1-22': '782d5a9da97fa60e1d831eb96ba7e757', 'Т50-11-22': '20fb86ce835d5ad716bb6b68040ce546', 'Т50-11-23': '4bc572b93f0a0f286136b9011f38926c', 'БИ50-1-20': 'b4454d5e8f1a6c5113ec1d5e4eb870d9', 'БИ50-1-21, БИ50-11/1-22': 'c967f44ce4b23d8d6f1bc2c7d074bc53', 'БИ50-1-22, БИ50-11/1-23': 'b1946bfcf06fc91e80eeae4d5e0fa6bc', 'БИ50-11-21': 'cb61321801c81af462ff7ec8cc3ba780', 'БИ50-11-22': '0357c09e7c1136325357df8c5859ddbe', 'БИ50-2-20': 'e3d1a995cd9f0b73d6566a299b030477', 'БИ50-2-21, БИ50-11/2-22': '2f3a6ff029ec9d07d40000f2d8c4c995', 'БИ50-2-22': '61562ba3de2c477fb1c57c291ba5c7dd', 'БИ50-3-20': '9e42d7b6e95d35b64cadce8b496cfd4f', 'БИ50-3-21, БИ50-11/3-22': 'bd7bee2b0d4f24f2846483e98ebc2ddd', 'БИ50-3-22': 'b09b4206cfe475159e7a1a5bae9feb52', 'Ю-1-21': 'be7f5e9a39fb8a166f25d7983aae5153', 'Ю-1-22, Ю-11/1-23': 'f22ed68dea9693dff988eed55f971ecd', 'Ю-1-23': '6be1a0e5c7248f6a5a3201f62fecb6f9', 'Ю-2-21, Ю-11/2-22': '63a5cdf8db4cd50325113c7f990df825', 'Ю-2-22, Ю-11/2-23': 'f17f474156e945076249e375ba2d60d6', 'Ю-2-23': 'a8e778b7593dff0a5e6a10f6372d0785', 'БИ50-1-23': 'abfe475394ecbde27242c5dcb49675de', 'БИ50-2-23': '623aafe3844f48a7931f968bf971868c', 'БИ50-3-23': '005eb981a9fcee68f7fc3aa33e3ad457', 'БИ50-4-23': 'f021ef6b54d3c67c90e2dced6d490cfd', 'БИ50-5-23': '86a83f7c0685f466ed271652c6e39f3b', 'ИСиП-1-23': '843b85ebf083d4ec5b25b148fb616fe0', 'ИСиП-10-23': '748d760518aaf16083442237f978b1ba', 'ИСиП-11-23': 'ea7923ea74a9a9682aed359171dcbac1', 'ИСиП-12-23': 'ff92fa1c406ba49fef4efcc2155eb102', 'ИСиП-13-23': '61b9ec7ddd81e595b90f4a03a2276def', 'ИСиП-14-23': '515b60a03ad25d2834c49a8107a98143', 'ИСиП-15-23': 'ca4e4f38106d9bd9071b5b9e3cf23056', 'ИСиП-2-23': '9f9f6975c0a1a5dcf31458d456c96a41', 'ИСиП-3-23': '1fe395588fcf1dc105dc2e3f55075b20', 'ИСиП-4-23': 'b0b386904f61277d575d3070df5ebb56', 'ИСиП-5-23': '837b455e5f25a199421693974e3c7678', 'ИСиП-6-23': 'e3c00a45b82249f2b661b46978927215', 'ИСиП-7-23': 'f67b62d91bdfe26d79db3b6ff1c6aa3b', 'ИСиП-8-23': '195d74b3ba4bd612434817fa7e7f8f86', 'ИСиП-9-23': 'd39c38c8a16de53b83c8894705abf096', 'СА50-1-23': 'edc15db0c670a60dd3c7ce49cf8691fe', 'СА50-2-23': '9fae7ca66424819cf81294ddce7e3a66', 'СА50-3-23': 'cc57b2a77cddefdbcccf82478b7352a4', 'Э-1-23': 'c9d31b8f79c957f08cb17a1163619c6f', 'Э-2-23': '149505fc0169d45f88a1ff3cfe41633e'}
disps = []
for g in list(groups.keys()):

    raspis_soup = soup.find('div', id=f'{groups[g]}')

    day_rasp = raspis_soup.find_all('table') # необработанное расписнаие на 1 день
    list_days = []
    l_mpt_cls_days = []
    for zaniatie in day_rasp:
        day_name = zaniatie.find('h4') # имя дня и площадка
        # print(str(day_name.text).replace(day_name.find('span').text, ''), str(day_name.find('span').text))
        raspisanie = zaniatie.find_all('tbody')[-1].find_all('tr') # расписание на 1 день
        day_cls = []
        num = 0
        legend = False
        cch, czn, pch, pzn = '', '', '', ''
        for stroka_raspis in raspisanie:
            legend = False
            if stroka_raspis.find('th') == None: # отсеиваются заголовки
                stlb_rasps = stroka_raspis.find_all('td') # столбцы  расписания
                if len(stlb_rasps) == 3:
                    num = int(stlb_rasps[0].text)
                    if stlb_rasps[2] == '' or stlb_rasps[2] == None:
                        disps.append(stlb_rasps[1].text)
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

                        disps.append(cch)
                        disps.append(czn)


                        pch = str(stlb_rasps[2].find('div', class_=ch).text).replace("\n", '').strip()
                        pzn = str(stlb_rasps[2].find('div', class_=zn).text).replace("\n", '').strip()

                if len(day_cls) > 0:
                    if day_cls[-1] != MPT_class(num, legend, cch, czn, pch, pzn):
                        day_cls.append(MPT_class(num, legend, cch, czn, pch, pzn))
                else:
                    day_cls.append(MPT_class(num, legend, cch, czn, pch, pzn))
        l_mpt_cls_days.append(day_cls)
        list_days.append(Day(str(day_name.text).replace(day_name.find('span').text, '').replace("\n", ''), str(day_name.find('span').text), day_cls))
        # for i in day_cls:
        #     i.getter()
        day_cls = []

    # о бля, то бля, сериализация
    jtwo = []
    for i in list_days:
        l = []
        for j in i.classes:
            l.append(JSONDataAdapter.to_json(j))
        i.classes = l
        jone = JSONDataAdapter.to_json(i)
        jtwo.append(jone)
print()
    # print(jtwo)
     #кодировка
    # with open(fr'C:\Users\serge\OneDrive\Рабочий стол\Расписания\{g.replace("/", "$")}.json', 'w') as file:
    #     string_json = json.dumps(jtwo)
    #
    #     file.write(string_json)

# for i in l_mpt_cls_days:
#     for j in i:
#         print(j.getter())




