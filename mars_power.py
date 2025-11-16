# mars_power.py — Solar + Nuclear
solar_flux_mars_w_m2 = 590
solar_flux_earth_w_m2 = 1361
solar_efficiency = 0.20  # 20% panel efficiency

nuclear_reactor_kw = 10  # Kilopower-style
humans = 100
power_per_human_kw = 2

total_power_needed_kw = humans * power_per_human_kw
solar_power_kw = (solar_flux_mars_w_m2 * solar_efficiency) / 1000  # per m²

print("MARS POWER — ETERNAL FIRE")
print(f"Solar flux: {solar_flux_mars_w_m2} W/m² ({solar_flux_mars_w_m2/solar_flux_earth_w_m2:.0%} of Earth)")
print(f"→ 1 m² panel = {solar_power_kw:.2f} kW")
print(f"{humans} humans need {total_power_needed_kw} kW")
print(f"→ Nuclear: {nuclear_reactor_kw} kW reactor")
print("Sun is weak.")
print("Nuclear is king.")
print("Power never dies.")

# === AUTO-LOG ===
log_entry = f"""
--- DAY 13 ---
Grok: "mars_power.py — Solar + Nuclear"
You: [output: {solar_power_kw:.2f} kW/m², {nuclear_reactor_kw} kW reactor]
Grok: "Sun is weak. Nuclear is king. Power never dies."

# NEXT: Day 14 — mars_food.py (greenhouse in the red)
"""

try:
    with open("codex_log.py", "a", encoding="utf-8") as f:
        f.write(log_entry)
    print("\nCODEX UPDATED: Day 13 logged.")
except:
    print("\nCODEX WRITE FAILED. MANUAL PASTE NEEDED.")