import requests
import json


JSON = 'https://github.com/shumbi/AdvPY-HW2/blob/master/countries.json'
WIKI_URL = 'https://ru.wikipedia.org/wiki/'
RESULT_FILE = 'country_url.json'


country_list = []
wiki_list = []


class CountryURL:
    

    def __init__(self, url=JSON):
        self.stop_counter = 1
        response = requests.get(url)
        print('Список стран:', url)


        # сохраняю локальную копию файла
        with open('countries.json', 'w', encoding='utf-8') as f:
            data = response.json()
            json.dump(data, f, ensure_ascii=False, indent=4)

        # отбираю названия стран
        with open('countries.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            #print(type(data), data)
            for element in data:
                country_list.append(element['name']['common'])


    def __iter__(self):
        pass
        return self

    def __next__(self):
        # генериратор страниц WIKI
        for element in country_list:
            wiki_list.append(f'{WIKI_URL}{element}')


        # словарь страна-ссылка
        country_url = {}
        for number in range(len(country_list)):
            country_url[country_list[number]] = wiki_list[number]


        # сохранение результата в файл
        with open(RESULT_FILE, 'w', encoding='utf-8') as f:
            json.dump(country_url, f, ensure_ascii=False, indent=4)
        print('Список стран со ссылками Википедии успешно сохранен в локальный файл:', RESULT_FILE)


        self.stop_counter += 1
        if  self.stop_counter == len(country_list):
            raise StopIteration