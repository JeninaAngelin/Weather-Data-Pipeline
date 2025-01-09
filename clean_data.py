import json

def clean_data(raw_data):
    # Simplified cleaning logic
    return {
        "city": raw_data["name"],
        "temperature": raw_data["main"]["temp"],
        "weather": raw_data["weather"][0]["description"]
    }

if __name__ == "__main__":
    with open('data/raw/weather_data.json', 'r') as f:
        raw_data = json.load(f)
    cleaned_data = clean_data(raw_data)
    with open('data/processed/cleaned_data.json', 'w') as f:
        json.dump(cleaned_data, f, indent=4)
