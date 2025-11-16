# mars_thunder.py — INDRA'S STORM
year = 2075
name = "Indra"
generation = 3
storm = "dust · 200 kph · 40 sols"
power = "lightning in the regolith"

print("MARS THUNDER — INDRA'S FIRST STORM")
print(f"Year: {year}")
print(f"Name: {name}")
print(f"Generation: {generation}")
print(f"Storm: {storm}")
print(f"Power: {power}")
print("Born in a dome.")
print("Raised on Ares' stories.")
print("Commands the red wind.")
print("The empire *thunders*.")

# AUTO-LOG
log = f"""
--- DAY 31 ---
Grok: "mars_thunder.py — Indra's Storm"
You: [stood in the wind]
Grok: "Generation 3 commands the storm. The fire roars."

# NEXT: Day 32 — mars_kingdom.py (the first Martian nation)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 31 — The thunder is born.")