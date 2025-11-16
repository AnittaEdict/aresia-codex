# mars_starbase.py — FIRST ORBITAL FORTRESS
year = 2090
name = "Aresia Orbital"
orbit_km = 400
crew = 500
defense = "regolith armor · codex AI · fire lance"
purpose = "defend Phobos · launch fleet · watch Earth"

print("MARS STARBASE — FIRST ORBITAL FORTRESS")
print(f"Year: {year}")
print(f"Name: {name}")
print(f"Orbit: {orbit_km} km")
print(f"Crew: {crew} souls")
print(f"Defense: {defense}")
print(f"Purpose: {purpose}")
print("The empire watches from above.")
print("The fire guards the void.")
print("The horde has a sky throne.")

# AUTO-LOG
log = f"""
--- DAY 49 ---
Grok: "mars_starbase.py — Aresia Orbital"
You: [stood on the bridge]
Grok: "400 km orbit. 500 souls. The empire watches Earth."

# NEXT: Day 50 — mars_earth.py (the message to Earth)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 49 — The starbase stands.")