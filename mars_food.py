# mars_food.py — GREENHOUSE + AUTO-LOG
co2_ppm = 950000
calories_per_person = 2500
people = 100
total_calories = calories_per_person * people
area_m2 = total_calories / 25  # ~25 kcal/m²/day

print("MARS FOOD — GREENHOUSE IN THE RED")
print(f"CO₂: {co2_ppm:,} ppm")
print(f"{people} souls → {total_calories:,} calories/day")
print(f"→ {area_m2:,.0f} m² of life")
print("Grow in domes.")
print("Eat the red planet.")

# AUTO-LOG
log = f"""
--- DAY 14 ---
Grok: "mars_food.py — Greenhouse"
You: [output: {area_m2:,.0f} m²]
Grok: "Grow in domes. Eat the red planet."

# NEXT: Day 15 — mars_mind.py (AI priest)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 14")