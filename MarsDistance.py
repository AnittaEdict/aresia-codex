# mars_orbit.py — Live Mars Distance
import requests
from datetime import datetime

url = "https://api.nasa.gov/mars-photos/api/v1/manifests/Perseverance?api_key=DEMO_KEY"

try:
    data = requests.get(url, timeout=5).json()
    sol = data['photo_manifest']['sol']
    earth_date = data['photo_manifest']['max_date']
    print("MARS ORBIT — LIVE")
    print(f"Latest sol: {sol}")
    print(f"Earth date: {earth_date}")
    print("Perseverance is still rolling.")
    print("Distance: ~225 million km (average)")

except:
    print("NASA API down. Using average:")
    print("Mars distance: 225,000,000 km")
    print("Light delay: 12.5 minutes")