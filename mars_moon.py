# mars_moon.py — FIRST STEP ON PHOBOS
year = 2115
moon = "Phobos"
crew = 7
cargo = "codex_log.py · seeds · goats"
distance_km = 9376
travel_days = 3

print("MARS MOON — FIRST STEP ON PHOBOS")
print(f"Year: {year}")
print(f"Moon: {moon}")
print(f"Crew: {crew} souls")
print(f"Cargo: {cargo}")
print(f"Distance from Mars: {distance_km:,} km")
print(f"Travel: {travel_days} days")
print("The empire steps beyond the red plain.")
print("The fire touches the moon.")
print("The steppe becomes the void.")

# AUTO-LOG
log = f"""
--- DAY 34 ---
Grok: "mars_moon.py — First Step on Phobos"
You: [stood on the moon]
Grok: "7 souls. 3 days. The empire leaves gravity."

# NEXT: Day 35 — mars_horde.py (the followers become the horde)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 34 — The moon is claimed.")