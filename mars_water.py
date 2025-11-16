# mars_water.py — Ice oceans beneath
earth_oceans_km3 = 1.332e9
mars_ice_estimate_km3 = 5e6  # Polar caps + subsurface

percent_of_earth = (mars_ice_estimate_km3 / earth_oceans_km3) * 100

print("MARS WATER — FROZEN OCEANS")
print(f"Earth oceans: {earth_oceans_km3:,.0f} km³")
print(f"Mars ice: ~{mars_ice_estimate_km3:,.0f} km³")
print(f"→ {percent_of_earth:.2f}% of Earth's water — locked in ice")
print("Drill deep.")
print("Melt the poles.")
print("Life may sleep below.")