# mars_distance.py — VISUALIZE KM
def mars_km(distance_km, speed_kph=10):
    hours = distance_km / speed_kph
    days = hours / 24
    print(f"{distance_km:,} km at {speed_kph} kph")
    print(f"→ {hours:.1f} hours")
    print(f"→ {days:.1f} Martian days")
    print("-" * 30)

# REAL MARS DISTANCES
print("MARS DISTANCE — THE STEPPE IN MOTION")
mars_km(100)      # Olympus Mons base
mars_km(500)      # Valles Marineris edge
mars_km(1000)     # Colony to colony
mars_km(21000)    # Full circumference (like Earth!)