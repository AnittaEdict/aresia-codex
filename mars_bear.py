# mars_bear.py — THE UNSPOKEN
name_forbidden = "Radiation"
name_spoken = "The Red One"
power = "250 mSv/year"
taboo = "name it and it comes"

print("MARS BEAR — THE RED ONE WALKS")
print(f"We do not say: '{name_forbidden}'")
print(f"We say: '{name_spoken}'")
print(f"It walks at {power}")
print(f"Rule: {taboo}")
print("We offer the first dome.")
print("We keep silence.")
print("We survive.")

# AUTO-LOG
log = f"""
--- DAY 22 ---
Grok: "mars_bear.py — The Red One"
You: [silence before the bear]
Grok: "Name it not. Offer first. Survive."

# NEXT: Day 23 — mars_wagon.py (the steppe moves again)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 22 — The bear is honored.")