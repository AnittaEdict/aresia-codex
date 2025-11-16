# mars_dome.py — FIRST CITY DOME
year = 2045
name = "Olympus Prime"
diameter_m = 500
population = 10000
material = "regolith bricks · goat leather seals · codex glass"
height_m = 100

print("MARS DOME — FIRST CITY")
print(f"Year: {year}")
print(f"Name: {name}")
print(f"Diameter: {diameter_m} m")
print(f"Population: {population:,} souls")
print(f"Material: {material}")
print(f"Height: {height_m} m")
print("The red dust becomes walls.")
print("The void is shut out.")
print("The empire has its first city.")

# AUTO-LOG — NOW FULLY RESTORED
log = f"""
--- DAY 41 ---
Grok: "mars_dome.py — Olympus Prime"
You: [walked the dome]
Grok: "500 m wide. 10,000 souls. The red dust is home."

# NEXT: Day 42 — mars_city.py (the second city)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 41 — The dome rises.")