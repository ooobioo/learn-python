# MetaWeather API Example
import requests

url = "https://www.metaweather.com/api/"
headers = {
    "Content-Type": "application/json"
}

response = requests.get(url)
data = response.json()
print(data)