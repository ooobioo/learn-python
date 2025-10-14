import requests

# URL für den Pegel Nürnberg, aktueller Wasserstand (letzter Messwert)
url = "https://pegelonline.wsv.de/webservices/rest-api/v2/stations/10600000/measurements.json?includeCurrentMeasurement=true"

response = requests.get(url)
data = response.json()

print(data)

# Ausgabe des aktuellen Messwerts
if "currentMeasurement" in data:
    wasserstand = data["currentMeasurement"]["value"]
    zeitpunkt = data["currentMeasurement"]["timestamp"]
    print(f"Aktueller Wasserstand am Pegel Nürnberg: {wasserstand} m (gemessen am {zeitpunkt})")
else:
    print("Keine aktuellen Messwerte gefunden.")