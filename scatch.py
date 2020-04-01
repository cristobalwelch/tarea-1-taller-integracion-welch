import requests
import json

def all_episodes():

    current_page = 1
    base_url = 'https://rickandmortyapi.com/api/episode?page='
    url = base_url + str(current_page)
    all_episodes_information = list()
    final_information = list()

    all_episode_request = requests.get(url).json()
    all_episodes_information.append(all_episode_request)

    while current_page < int(all_episode_request['info']['pages']):
        current_page += 1
        url = base_url + str(current_page)
        all_episode_request = requests.get(url).json()
        print(all_episode_request)
        all_episodes_information.append(all_episode_request)

    for page in all_episodes_information:
        for result in page['results']:
            d = dict()
            d['name'], d['air_date'], d['episode'] = result['name'], result['air_date'], result['episode']
            final_information.append(d)

    return final_information

x = all_episodes()
print(x)