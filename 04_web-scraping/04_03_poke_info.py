# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5

BASE_URL = "https://pokeapi.co/api/v2/"

import requests

favorite_pokemon = ["pikachu", "bulbasaur", "mudkip", "ditto", "diglett", "geodude"]

pokemon_info = []
for pokemon in favorite_pokemon:
  response = requests.get(f"{BASE_URL}pokemon/{pokemon}")
  data = response.json()

  pokemon_info.append({
    "name": data["name"],
    "id": data["id"],
    "types": [type["type"]["name"] for type in data["types"]]

  })

print(pokemon_info)
