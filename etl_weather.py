import requests
import pandas as pd
import sqlite3
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Please set OPENWEATHERMAP_API_KEY in your .env file.")

CITIES = ["Frankfurt", "Berlin", "Munich", "Hamburg"]

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

# === Extract ===
weather_data = []
for city in CITIES:
    data = fetch_weather(city)
    weather_data.append({
        "city": city,
        "temp": data['main']['temp'],
        "feels_like": data['main']['feels_like'],
        "weather": data['weather'][0]['description'],
        "timestamp": datetime.fromtimestamp(data['dt'])
    })

# === Transform ===
df = pd.DataFrame(weather_data)
df['temp'] = df['temp'].round(1)
df['feels_like'] = df['feels_like'].round(1)

# === Load ===
conn = sqlite3.connect("weather.db")
df.to_sql("weather_data", conn, if_exists="replace", index=False)
conn.commit()

# Verify
print(pd.read_sql("SELECT * FROM weather_data", conn))
conn.close()
