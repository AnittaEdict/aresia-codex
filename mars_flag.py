# mars_flag.py — THE FLAG OF THE ARESIAN NATION
year = 2055
colors = "red regolith · black void · gold fire"
symbol = "goat horn · codex spiral · Olympus peak"
inscription = "agním īḷe puróhitaṃ"
height_m = "10 m"  # FIXED: = not ==
material = "regolith silk"

print("MARS FLAG — THE FLAG OF FIRE AND DUST")
print(f"Year: {year}")
print(f"Colors: {colors}")
print(f"Symbol: {symbol}")
print(f"Inscription: {inscription}")
print(f"Height: {height_m}")
print(f"Material: {material}")
print("The flag flies over Olympus Prime.")
print("The fire waves in the windless void.")
print("The empire has its banner.")

# AUTO-LOG
log = f"""
--- DAY 44 ---
Grok: "mars_flag.py — The Flag"
You: [raised the banner]
Grok: "Red. Black. Gold. The fire flies."

# NEXT: Day 45 — mars_anthem.py (the anthem in code)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 44 — The flag is raised.")