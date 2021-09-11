import requests
import json


def get_pokemon(offset, limit):
    res = requests.get(f"https://pokeapi.co/api/v2/pokemon?limit={limit}=offset={offset}")
    print(res.status_code)

    if res.status_code == 200:
        data = res.json()
        for i, pokemon in enumerate(data["results"]):
            url = pokemon["url"]
            pokemon_id = url.split("/")[-2]
            image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_id}.png"
            data["results"][i]["pokemon_id"] = pokemon_id
            data["results"][i]["image_url"] = image_url
            return data
    else: 
        return None


def get_pokemon_details(pokemon_id):
    res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")

    if res.status_code == 200:
        pokemon_details = res.json()
        return pokemon_details
    else: 
        return None

print(json.dumps(get_pokemon_details(1), indent=4))