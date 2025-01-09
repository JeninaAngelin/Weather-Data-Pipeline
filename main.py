from src.api.fetch_weather_data import fetch_weather_data
from src.processing.clean_data import clean_data
from src.processing.transform_data import transform_data
from src.storage.save_to_db import save_to_db

def main(city):
    raw_data = fetch_weather_data(city)
    cleaned_data = clean_data(raw_data)
    transformed_data = transform_data(cleaned_data)
    save_to_db(transformed_data)

if __name__ == "__main__":
    city = "London"
    main(city)
