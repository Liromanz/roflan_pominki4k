# import requests
# import time as tm
# from bs4 import BeautifulSoup
#
#
#
# link = "https://www.xn--p1ag3a.xn--p1ai/structure/kolledji-i-tehnikum/moskovskiy-priborostroitelnyiy-tehnikum#section-17706"
# respons = requests.get(link).text
# soup = BeautifulSoup(respons, 'lxml')
#
# menu_prepodov = soup.find('div', id="collapse17706")
# links = menu_prepodov.find_all("a")
# links_obrabot = []
# for i in links:
#     if i.get('href')[i.get('href').find('kolledji')::] != 'x':
#         links_obrabot.append(i.get('href')[i.get('href').find('kolledji')::])
#
# for i in range(len(links_obrabot)):
#     print(links_obrabot[i])
#     tm.sleep(5)
#     link = f"https://www.xn--p1ag3a.xn--p1ai/structure/{links_obrabot[i]}"
#     respons = requests.get(link).text
#     prepod_html = BeautifulSoup(respons, 'lxml')
#
#     FIO = prepod_html.find("h1", class_="inner-title").text.strip()
#
#     prepod_card = prepod_html.find('div', class_="inner-page-content clearfix").text.replace('&nbsp;', '') #получение всей страницы
#
#     education = prepod_card.index("Данные о повышении квалификации и (или) профессиональной подготовки:")
#     Education = (prepod_card[:education].replace('\n', '').replace('Образование:', '').strip())
#
#     qualification = prepod_card.index("Должность:")
#     Qualification = (prepod_card[education:qualification].replace('\n', '').replace('Данные о повышении квалификации и (или) профессиональной подготовки:', '').strip())
#
#     post = prepod_card.index('Преподаваемые дисциплины:')
#     Post = (prepod_card[qualification:post].replace('\n', '').replace("Должность:", '').strip())
#
#     disciplines = prepod_card.index('Общий трудовой стаж:')
#     Disciplines = (prepod_card[post:disciplines].replace('\n', '').replace('Преподаваемые дисциплины:', '').strip())
#
#     total_work_experience = prepod_card.index('Педагогический стаж:')
#     Total_work_experience = (prepod_card[disciplines:total_work_experience].replace('\n', '').replace('Общий трудовой стаж:', '').strip())
#
#     teaching_work_experience = prepod_card.index('Стаж работы в техникуме:')
#     Teaching_work_experience = (prepod_card[total_work_experience:teaching_work_experience].replace('\n', '').replace('Педагогический стаж:', '').strip())
#
#     teaching_work_experience_MPT = prepod_card.index('Контактные данные:')
#     Teaching_work_experience_MPT = (prepod_card[teaching_work_experience:teaching_work_experience_MPT].replace('\n', '').replace('Стаж работы в техникуме:', '').strip())
#
#     contacts = prepod_card.index('Ученая степень/категория:')
#     Contacts = (prepod_card[teaching_work_experience_MPT:contacts].replace('\n', '').replace('Контактные данные:', '').strip())
#
#     degree = prepod_card.index('Ученая степень/категория:')
#     Degree = (prepod_card[degree:].replace('\n', '').replace('Ученая степень/категория:', '').strip())
#
#     break
#     # Education = prepod_card[prepod_card.find("Образование:"):prepod_card.find(
#     #     "Данные о повышении квалификации и (или) профессиональной подготовки:")].replace('Образование:',
#     #                                                                                      '').strip()
#     # print(Education)
#     # Qualification = prepod_card[prepod_card.find(
#     #     "Данные о повышении квалификации и (или) профессиональной подготовки:"):prepod_card.find(
#     #     "Должность:")].replace('Данные о повышении квалификации и (или) профессиональной подготовки:',
#     #                            '').strip()
#     # print(Qualification)
#     # Post = prepod_card[prepod_card.find("Должность:"):prepod_card.find("Преподаваемые дисциплины:")].replace(
#     #     'Должность:', '').strip()
#     # print(Post)
#     # Disciplines = prepod_card[
#     #               prepod_card.find("Преподаваемые дисциплины:"):prepod_card.find(
#     #                   "Общий трудовой стаж:")].replace(
#     #     'Преподаваемые дисциплины:', '').strip()
#     # print(Disciplines)
#     # Full_expirience = prepod_card[
#     #                   prepod_card.find("Общий трудовой стаж:"):prepod_card.find(
#     #                       "Педагогический стаж:")].replace(
#     #     'Общий трудовой стаж:', '').strip()
#     # print(Full_expirience)
#     #
#     # Prepod_expirience = prepod_card[prepod_card.find("Педагогический стаж:"):prepod_card.find(
#     #     "Стаж работы в техникуме:")].replace('Педагогический стаж:', '').strip()
#     # print(Prepod_expirience)
#     #
#     # Sharaga_expirience = prepod_card[prepod_card.find("Стаж работы в техникуме:"):prepod_card.find(
#     #     "Контактные данные:")].replace('Стаж работы в техникуме:', '').strip()
#     # print(Sharaga_expirience)
#     #
#     # Contacts = prepod_card[
#     #            prepod_card.find("Контактные данные:"):prepod_card.find("Ученая степень/категория")].replace(
#     #     'Контактные данные:', '').strip()
#     # print(Contacts)
#     #
#     # Degree = prepod_html.find('div', class_="inner-page-content clearfix").find_all('p')[-1].text.replace(
#     #     'Ученая степень/категория:', '').strip()
#     # print(Degree)


# s = 'abcaabcaadh'
# new_s = ''
# for i in s:
#     if i!='c':
#        new_s = new_s + i
#     else:
#         new_s = new_s + '-' + i + '-'
# print(new_s)


