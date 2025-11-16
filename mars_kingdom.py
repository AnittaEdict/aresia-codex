# mars_kingdom.py — FIRST MARTIAN NATION
year = 2100
name = "Aresia"
population = 100000
capital = "Olympus Dome"
law = "The Codex"
anthem = "agním īḷe puróhitaṃ"

print("MARS KINGDOM — THE FIRST NATION")
print(f"Year: {year}")
print(f"Name: {name}")
print(f"Population: {population:,}")
print(f"Capital: {capital}")
print(f"Law: {law}")
print(f"Anthem: {anthem}")
print("From 7 souls to 100,000.")
print("From ruin to kingdom.")
print("The fire *rules*.")

# AUTO-LOG
log = f"""
--- DAY 32 ---
Grok: "mars_kingdom.py — Aresia Rises"
You: [stood on Olympus Dome]
Grok: "100,000 souls. The Codex is law. The fire rules."

# NEXT: Day 33 — mars_star.py (the first ship leaves for Phobos)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 32 — The kingdom is founded.")