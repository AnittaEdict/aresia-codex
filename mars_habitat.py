# mars_habitat.py — RADIATION SHIELD + AUTO-LOG
surface_radiation_msv_year = 250
earth_radiation_msv_year = 2.4
shielding_needed = surface_radiation_msv_year / earth_radiation_msv_year

# === MISSION OUTPUT ===
print("MARS HABITAT — RADIATION SHIELD")
print(f"Surface: {surface_radiation_msv_year} mSv/year")
print(f"Earth: {earth_radiation_msv_year} mSv/year")
print(f"→ {shielding_needed:.0f}x Earth's radiation")
print("Dig deep.")
print("Use regolith.")
print("Live underground.")

# === AUTO-LOG TO codex_log.py ===
log_entry = f"""
--- DAY 12 ---
Grok: "mars_habitat.py — Radiation shield"
You: [output: {shielding_needed:.0f}x radiation]
Grok: "Dig deep. Use regolith. Live underground."

# NEXT: Day 13 — mars_power.py (solar + nuclear)
"""

try:
    with open("codex_log.py", "a", encoding="utf-8") as f:
        f.write(log_entry)
    print("\nCODEX UPDATED: Day 12 logged.")
except:
    print("\nCODEX WRITE FAILED. MANUAL PASTE NEEDED.")