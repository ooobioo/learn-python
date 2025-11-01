import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_data(name):
    """Fetch data for a specific Pokémon by name."""
    url = f"{BASE_URL}{name.lower()}"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"].capitalize(),
            "id": data["id"],
            "height": data["height"],
            "weight": data["weight"],
            "types": [t["type"]["name"] for t in data["types"]],
        }
    else:
        print(f"Error: Pokémon '{name}' not found. (HTTP {response.status_code})")
        return None

if __name__ == "__main__":
    pokemon_name = input("Enter Pokémon name: ").strip()
    pokemon = get_pokemon_data(pokemon_name)

    if pokemon:
        print("\nPokémon Data:")
        print(f"Name: {pokemon['name']}")
        print(f"ID: {pokemon['id']}")
        print(f"Height: {pokemon['height']}")
        print(f"Weight: {pokemon['weight']}")
        print(f"Types: {', '.join(pokemon['types'])}")
