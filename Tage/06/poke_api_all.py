import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon"

def get_all_pokemon(limit=10000):
    """Fetch a complete list of all Pokémon names."""
    response = requests.get(f"{BASE_URL}?limit={limit}")
    
    if response.status_code == 200:
        data = response.json()
        names = [pokemon["name"] for pokemon in data["results"]]
        return names
    else:
        print(f"Error fetching Pokémon list (HTTP {response.status_code})")
        return []

if __name__ == "__main__":
    all_pokemon = get_all_pokemon()

    print(f"Total Pokémon found: {len(all_pokemon)}\n")
    print("Sample Pokémon list:")
    print(", ".join(all_pokemon[:300]))  # print only first 30 names
