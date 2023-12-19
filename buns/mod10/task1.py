import requests
import json

url = 'https://swapi.dev/api/starships/10'
response = requests.get(url)

if response.status_code == 200:
    starship_data = response.json()
else:
    raise Exception(f"Не удалось получить данные с {url}. Код состояния: {response.status_code}")


def fetch_pilot_info(pilot_url):
    pilot_response = requests.get(pilot_url)
    if pilot_response.status_code == 200:
        pilot_data = pilot_response.json()
        homeworld_response = requests.get(pilot_data['homeworld'])
        if homeworld_response.status_code == 200:
            homeworld_data = homeworld_response.json()
            return {
                'name': pilot_data['name'],
                'height': pilot_data['height'],
                'mass': pilot_data['mass'],
                'homeworld': homeworld_data['name'],
                'homeworld_url': pilot_data['homeworld']
            }
        else:
            raise Exception(f"Не удалось получить данные о родной планете пилота {pilot_data['name']}. Код состояния: {homeworld_response.status_code}")
    else:
        raise Exception(f"Не удалось получить данные о пилоте. Код состояния: {pilot_response.status_code}")


pilots = [fetch_pilot_info(pilot) for pilot in starship_data['pilots']]


ship_info = {
    'ship_name': starship_data['name'],
    'starship_class': starship_data['starship_class'],
    'max_atmosphering_speed': starship_data['max_atmosphering_speed'],
    'pilots': pilots,
}

print(json.dumps(ship_info, indent=4))

with open('ship.json', 'w') as f:
    json.dump(ship_info, f, indent=4)
