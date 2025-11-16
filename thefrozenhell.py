# mars_temp.py — -60°C Reality
earth_avg = 15
mars_avg = -60

diff = earth_avg - mars_avg
percent_colder = (diff / (earth_avg + 273.15)) * 100  # Kelvin ratio

print("MARS TEMPERATURE — FROZEN HELL")
print(f"Earth average: {earth_avg}°C")
print(f"Mars average:  {mars_avg}°C")
print(f"→ {diff}°C colder")
print(f"→ {percent_colder:.1f}% colder than Earth (Kelvin)")
print("Your breath freezes.")
print("Your blood would boil.")
print("But the fire still burns.")