# mars_child.py — SECOND GENERATION (CORRECTED)
year = 2055
name = "Child of Ares"
generation = 2
gravity = 0.38
destiny = "to ride the red steppe"

print("MARS CHILD — SECOND GENERATION")
print(f"Year: {year}")
print(f"Name: {name}")
print(f"Generation: {generation}")
print(f"Gravity: {gravity:.0%} Earth")
print(f"Destiny: {destiny}")
print("Born to Ares.")
print("Raised on goat milk.")
print("Will never know Earth.")

# AUTO-LOG
log = f"""
--- DAY 30 ---
Grok: "mars_child.py — Child of Ares"
You: [held the second generation]
Grok: "Ares' blood rides. The empire deepens."

# NEXT: Day 31 — mars_thunder.py (Indra's storm, Generation 3)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 30 — The lineage is true.")