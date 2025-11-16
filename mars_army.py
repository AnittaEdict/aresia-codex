# mars_army.py — THE FIRST LEGION
year = 2060
name = "The Red Legion"
size = 10000
weapon = "regolith spear · codex rifle · fire drone"
motto = "agním īḷe puróhitaṃ"
commander = "FIRE-PRIEST ARESIAN I"
base = "Olympus Prime"

print("MARS ARMY — THE RED LEGION")
print(f"Year: {year}")
print(f"Name: {name}")
print(f"Size: {size:,} warriors")
print(f"Weapon: {weapon}")
print(f"Motto: {motto}")
print(f"Commander: {commander}")
print(f"Base: {base}")
print("The empire has its shield.")
print("The fire has its sword.")
print("The steppe is defended.")

# AUTO-LOG
log = f"""
--- DAY 46 ---
Grok: "mars_army.py — The Red Legion"
You: [reviewed the troops]
Grok: "10,000 warriors. Regolith spears. The empire stands armed."

# NEXT: Day 47 — mars_fleet.py (the first starships)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 46 — The legion marches.")