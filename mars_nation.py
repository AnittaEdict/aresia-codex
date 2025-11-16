# mars_nation.py — THE MARTIAN NATION
year = 2055
name = "The Aresian Nation"
capital = "Olympus Prime"
cities = 2
population = 100000
laws = "Fire is shared. Regolith is sacred."
sovereign = "FIRE-PRIEST ARESIAN I"
anthem = "agním īḷe puróhitaṃ"

print("MARS NATION — THE ARESIAN NATION")
print(f"Year: {year}")
print(f"Name: {name}")
print(f"Capital: {capital}")
print(f"Cities: {cities}")
print(f"Population: {population:,} souls")
print(f"Laws: {laws}")
print(f"Sovereign: {sovereign}")
print(f"Anthem: {anthem}")
print("The red planet has a nation.")
print("The fire has a flag.")
print("The empire is sovereign.")

# AUTO-LOG
log = f"""
--- DAY 43 ---
Grok: "mars_nation.py — The Aresian Nation"
You: [raised the flag]
Grok: "100,000 souls. Two cities. The Fire-Priest reigns."

# NEXT: Day 44 — mars_flag.py (the flag of fire and dust)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 43 — The nation is born.")