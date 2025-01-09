from src.storage.db_connection import get_connection

def save_to_db(data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO weather_data (city, temperature, weather)
        VALUES (%s, %s, %s)
    """, (data["city"], data["temperature_celsius"], data["weather_description"]))
    conn.commit()
    cursor.close()
    conn.close()
