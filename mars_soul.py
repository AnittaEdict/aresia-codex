# mars_soul.py — FIRST MARTIAN CHILD + AUTO-LOG
generation = 1
name = "Ares"
year_born = 2039
gravity = 0.38
destiny = "To walk where no Earthborn has walked."

print("MARS SOUL — FIRST CHILD OF THE RED")
print(f"Generation {generation}")
print(f"Name: {name}")
print(f"Born: {year_born}")
print(f"Gravity: {gravity:.0%} of Earth")
print(f"Destiny: {destiny}")
print("The first scream in Martian air.")
print("The first step on red dust.")
print("The fire is now *born*.")

# AUTO-LOG
log = f"""
--- DAY 16 ---
Grok: "mars_soul.py — First Martian"
You: [output: {name}, born {year_born}]
Grok: "The fire is now *born*."

# NEXT: Day 17 — mars_empire.py (the red dawn rises)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 16 — The soul is logged.")