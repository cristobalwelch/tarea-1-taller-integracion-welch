import requests
import json

# Requests all episode information. Returns # of pages and episode info.
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
        all_episodes_information.append(all_episode_request)

    for page in all_episodes_information:
        for result in page['results']:
            d = dict()
            d['id'], d['name'], d['air_date'], d['episode'] = result['id'], result['name'], result['air_date'], result['episode']
            final_information.append(d)

    return final_information

def all_locations():
    
    current_page = 1
    base_url = 'https://rickandmortyapi.com/api/location?page='
    url = base_url + str(current_page)
    all_locations_information = list()
    final_information = list()

    all_location_request = requests.get(url).json()
    all_locations_information.append(all_location_request)

    while current_page < int(all_location_request['info']['pages']):
        current_page += 1
        url = base_url + str(current_page)
        all_location_request = requests.get(url).json()
        all_locations_information.append(all_location_request)

    for page in all_locations_information:
        for result in page['results']:
            d = dict()
            d['id'], d['name'], d['type'], d['dimension'] = result['id'], result['name'], result['type'], result['dimension']
            d["residents"] = result["residents"]
            final_information.append(d)

    return final_information

def all_characters():
    
    current_page = 1
    base_url = 'https://rickandmortyapi.com/api/character?page='
    url = base_url + str(current_page)
    all_characters_information = list()
    final_information = list()

    all_character_request = requests.get(url).json()
    all_characters_information.append(all_character_request)

    while current_page < int(all_character_request['info']['pages']):
        current_page += 1
        url = base_url + str(current_page)
        all_character_request = requests.get(url).json()
        all_characters_information.append(all_character_request)

    for page in all_characters_information:
        for result in page['results']:
            d = dict()
            d['id'], d['name'], d['status'], d['species'] = result['id'], result['name'], result['status'], result['species']
            d["type"], d["gender"], d["origin"] = result["type"], result["gender"], result["origin"]
            d["location"], d["image"], d["episode"] = result["location"], result["image"], result["episode"]
            final_information.append(d)

    return final_information

def episode_information(id):
    
    base_url = 'https://rickandmortyapi.com/api/episode/'
    url = base_url + str(id)
    final_information = list()
    d = dict()

    episode_request = requests.get(url).json()
    d["id"] = episode_request["id"]
    d["name"], d["air_date"], d["episode"] = episode_request["name"], episode_request["air_date"], episode_request["episode"]
    d["characters"] = list()

    for character in episode_request["characters"]:
        name = character_name(character)
        d["characters"].append(name)
    
    final_information.append(d)
    return final_information

def character_name(url):

    character_request = requests.get(url).json()
    #character_name = character_request["name"]
    character_info = {"id": character_request["id"], "name": character_request["name"], "url": url}
    print(character_info)
    return character_info

def character_information(id):
    
    base_url = 'https://rickandmortyapi.com/api/character/'
    url = base_url + str(id)
    final_information = list()
    d = dict()

    character_request = requests.get(url).json()
    #print(character_request)
    d["name"], d["status"]  =  character_request["name"], character_request["status"]
    d["species"], d["type"] = character_request["species"], character_request["type"]
    d["gender"] = character_request["gender"]
    d["origin"] = character_request["origin"] # Includes Name and URL
    d["location"] = character_request["location"]  # Includes Name and URL
    d["location"]["id"] = character_request["location"]["url"].split('/')[-1]
    d["image"] = character_request["image"] #Image URL
    d["episode"] = list()

    for episode in character_request["episode"]:
        name = episode_name(episode)
        d_temp = {"name": name, "url": episode, "id": episode.split('/')[-1]}
        d["episode"].append(d_temp)
    print(d)
    
    final_information.append(d)
    return final_information

def episode_name(url):

    episode_request = requests.get(url).json()
    episode_name = episode_request["name"]
    #print(episode_name)
    return episode_name

def location_information(id):

    base_url = 'https://rickandmortyapi.com/api/location/'
    url = base_url + str(id)
    final_information = list()
    d = dict()

    location_request = requests.get(url).json()
    #print(location_request)
    d["id"] = location_request["id"]
    d["name"], d["type"], d["dimension"] = location_request["name"], location_request["type"], location_request["dimension"]
    d["residents"] = list()

    # ACA VOY
    for resident in location_request["residents"]:
        name = character_name(resident)
        #d_temp = {"name": name['name'], "url": resident, "id": resident.split('/')[-1]}
        d["residents"].append(name)
    
    final_information.append(d)
    return final_information

def text_search(query):

    query_results = dict()
    episode_results = list()
    location_results = list()
    character_results = list()
    
    all_episode_request = all_episodes()
    all_character_request = all_characters()
    all_location_request = all_locations()

    query = query.lower()

    for episode in all_episode_request:
        if query in episode['name'].lower():
            episode_results.append(episode)
    query_results["episode"] = episode_results
    
    for character in all_character_request:
        if query in character['name'].lower():
            character_results.append(character)
    query_results["character"] = character_results
    
    for location in all_location_request:
        if query in location['name'].lower():
            location_results.append(location)
    query_results["location"] = location_results

    return query_results

