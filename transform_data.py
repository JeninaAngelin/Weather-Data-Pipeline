def transform_data(cleaned_data):
    # Example transformation logic
    return {
        "city": cleaned_data["city"].upper(),
        "temperature_celsius": round(cleaned_data["temperature"] - 273.15, 2),
        "weather_description": cleaned_data["weather"].capitalize()
    }
