# mars_pressure.py — Ghost Atmosphere
earth_pressure = 1013  # hPa
mars_pressure = 6.1    # hPa

percent_of = (mars_pressure / earth_pressure) * 100
percent_less = ((earth_pressure - mars_pressure) / earth_pressure) * 100

print("MARS ATMOSPHERE — GHOST")
print(f"Earth: {earth_pressure} hPa")
print(f"Mars:  {mars_pressure} hPa")
print(f"→ {percent_of:.1f}% of Earth")
print(f"→ {percent_less:.1f}% LESS than Earth")
print("A whisper. But not silence.")