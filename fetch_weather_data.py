import requests
import json
from src.api.api_config import API_URL, API_KEY

def fetch_weather_data(city):
    response = requests.get(f"{API_URL}?q={city}&appid={API_KEY}")
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

if __name__ == "__main__":
    city = "London"
    data = fetch_weather_data(city)
    with open('data/raw/weather_data.json', 'w') as f:
        json.dump(data, f, indent=4)
