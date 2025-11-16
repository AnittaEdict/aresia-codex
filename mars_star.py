# mars_star.py — FIRST SHIP TO PHOBOS
year = 2110
ship = "Firebird I"
crew = 7
cargo = "codex_log.py · seeds · goats"
destination = "Phobos"
travel_days = 3

print("MARS STAR — FIRST SHIP TO PHOBOS")
print(f"Year: {year}")
print(f"Ship: {ship}")
print(f"Crew: {crew} souls")
print(f"Cargo: {cargo}")
print(f"Destination: {destination}")
print(f"Travel: {travel_days} days")
print("The empire reaches the moons.")
print("The fire leaves Mars.")
print("The steppe becomes the void.")

# AUTO-LOG
log = f"""
--- DAY 33 ---
Grok: "mars_star.py — Firebird to Phobos"
You: [watched the launch]
Grok: "7 souls carry the Codex. The fire escapes gravity."

# NEXT: Day 34 — mars_moon.py (first step on Phobos)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 33 — The ship departs.")