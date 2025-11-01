import requests

api_url = "https://icanhazdadjoke.com/"
headers = {"Accept": "application/json"}

print("Willkommen beim Scherzgenerator!")
frage = input("Möchtest du einen Witz hören? (ja/nein) ")

while frage.lower() == "ja":
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        joke = response.json()["joke"]
        print("Witz:", joke)
    else:
        print("Leider konnte kein Witz abgerufen werden.")
    frage = input("Noch einen? (ja/nein) ")

print("Das war's – viel Spaß beim Programmieren!")