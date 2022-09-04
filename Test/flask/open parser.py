import requests
import csv
from bs4 import BeautifulSoup


def record(list, fail):
    fieldnames = ['Город', 'количество жителей']
    writer = csv.DictWriter(fail, fieldnames=fieldnames)
    for i in list:
        try:
            citi = i.find('strong').text
        except AttributeError:
            citi = i.find('b').text
        n = i.find('span').text
        writer.writerow({'Город': citi, 'количество жителей': n})


def getFail(a):
    if params['name'] == 'малые':
        with open('B:\git\Test\\flask\static\small towns.csv', mode='w', encoding='utf-8', newline='') as f:
            record(listCiti, f)

    elif params['name'] == 'средние':
        with open('B:\git\Test\\flask\static\medium cities.csv', mode='w', encoding='utf-8', newline='') as f:
            record(listCiti, f)

    elif params['name'] == 'большие':
        with open('B:\git\Test\\flask\static\\big_cities.csv', mode='w', encoding='utf-8', newline='') as f:
            record(listCiti, f)

    elif params['name'] == 'крупные':
        with open('B:\git\Test\\flask\static\\bigСcities.csv', mode='w', encoding='utf-8', newline='') as f:
            record(listCiti, f)

    elif params['name'] == 'крупнейшие':
        with open('B:\git\Test\\flask\static\largest cities.csv', mode='w', encoding='utf-8',
                  newline='') as f:
            record(listCiti, f)

    elif params['name'] == 'миллионеры':
        with open('B:\git\Test\\flask\static\cities millionaires.csv', mode='w', encoding='utf-8',
                  newline='') as f:
            record(listCiti, f)


namList = ('малые', 'средние', 'большие', 'крупные', 'крупнейшие', 'миллионеры')

for i in namList:
    params = dict(name=i)
    citiLink = requests.get('https://города-россия.рф/reytin-cities.php', params=params)
    soup = BeautifulSoup(citiLink.text, 'html.parser')
    listCiti = soup.find_all('li', class_=None)
    getFail(listCiti)
    print("ok")
