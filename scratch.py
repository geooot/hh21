import requests
import pandas

res = requests.get("https://pokeapi.co/api/v2/pokemon?limit=20=offset=0")
print(res)