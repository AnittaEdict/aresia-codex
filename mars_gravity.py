# mars_gravity.py — 38% of Earth
earth_gravity = 9.8  # m/s²
mars_gravity = 3.7   # m/s²

your_mass_kg = 70
your_weight_earth = your_mass_kg * earth_gravity
your_weight_mars = your_mass_kg * mars_gravity

print("MARS GRAVITY — 38% OF EARTH")
print(f"Your mass: {your_mass_kg} kg")
print(f"Earth weight: {your_weight_earth:.1f} N")
print(f"Mars weight:  {your_weight_mars:.1f} N")
print(f"→ You feel {your_weight_mars/your_weight_earth:.0%} of Earth weight")
print("You leap. You float. You are free.")