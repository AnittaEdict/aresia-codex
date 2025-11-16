# mars_city.py — SECOND CITY
year = 2050
name = "Aresia Secundus"
location = "Valles Marineris"
population = 50000
structure = "regolith domes · underground lava tubes"
economy = "goat milk · oxygen · codex chips"

print("MARS CITY — SECOND CITY RISES")
print(f"Year: {year}")
print(f"Name: {name}")
print(f"Location: {location}")
print(f"Population: {population:,} souls")
print(f"Structure: {structure}")
print(f"Economy: {economy}")
print("The empire spreads into the canyon.")
print("The fire lights the deep.")
print("The steppe becomes a nation.")

# AUTO-LOG
log = f"""
--- DAY 42 ---
Grok: "mars_city.py — Aresia Secundus"
You: [stood in the canyon]
Grok: "50,000 souls. Lava tubes. The empire deepens."

# NEXT: Day 43 — mars_nation.py (the Martian nation)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 42 — The second city lives.")