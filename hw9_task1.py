import requests
from pprint import pprint

BASE_URL = "https://superheroapi.com/api/2619421814940190/"


def search_power_get(search_name, search_power='intelligence'):
    list_power = list()
    for i in search_name:
        url = BASE_URL + "search/" + i
        response_character = requests.get(url, timeout=5).json()["results"][0]
        list_power.append({'id': response_character["id"],
                           'name': response_character["name"],
                           'intelligence': int(response_character["powerstats"][search_power])})
    return list_power


if __name__ == '__main__':
    search_hero = ['Hulk', 'Captain America', 'Thanos']
    power = 'intelligence'
    results = search_power_get(search_hero, power)
    pprint(results)
    max_power = {'id': 0, 'name': 'none', power: 0}
    for hero in results:
        if max_power[power] < hero[power]:
            max_power = hero
    print(f'\nГерой {max_power["name"]} с максимальным уровнем {power} = {max_power[power]}.')
