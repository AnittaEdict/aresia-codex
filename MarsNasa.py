# live_mars.py — Real Mars Pressure (NASA)
import requests

url = "https://mars.nasa.gov/rss/api/?feed=weather&category=mars2020&feedtype=json"

try:
    data = requests.get(url).json()
    latest = data['soles'][0]  # Most recent sol
    pressure = latest['pressure']
    earth_date = latest['terrestrial_date']

    print("LIVE FROM MARS — PERSEVERANCE ROVER")
    print(f"Earth date: {earth_date}")
    print(f"Mars pressure: {pressure} Pa")
    print(f"→ {(pressure/100):.1f} hPa")
    print("The ghost speaks — in real time.")

except:
    print("NASA link down. Using last known:")
    print("Mars: 6.1 hPa")