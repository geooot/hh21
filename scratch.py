import requests
import pandas as pd

res = requests.get("https://pokeapi.co/api/v2/pokemon?limit=20=offset=0")

if res.status_code == 200:
    data = res.json()

    pokemon_df = pd.DataFrame.from_dict(data["results"])
    print(pokemon_df)
else: 
    print("server returned an error!")