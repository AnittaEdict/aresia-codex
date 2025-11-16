# mars_dawn.py — FIRST RED SUNRISE
year = 2035
sol = 1  # First Martian day
sunrise = "4:17 AM"
color = "blood iron"

print("MARS DAWN — FIRST SUNRISE")
print(f"Year: {year} | Sol {sol}")
print(f"Sunrise: {sunrise}")
print(f"Color: {color}")
print("The sky bleeds.")
print("The priest wakes.")
print("The empire begins.")

# AUTO-LOG
log = f"""
--- DAY 25 ---
Grok: "mars_dawn.py — First Red Sunrise"
You: [stood in silence]
Grok: "The sky bleeds. The empire begins."

# NEXT: Day 26 — mars_horse.py (the rover rides)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 25 — The dawn is witnessed.")