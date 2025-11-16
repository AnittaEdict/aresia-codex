# mars_terraform.py — CO₂ → O₂
mars_atmosphere_co2_percent = 95.3
oxygen_needed_percent = 21.0

co2_to_convert = mars_atmosphere_co2_percent - oxygen_needed_percent
conversion_efficiency = 0.30

o2_producible = co2_to_convert * conversion_efficiency

print("MARS TERRAFORM — BREATHE THE RED")
print(f"Mars CO₂: {mars_atmosphere_co2_percent}%")
print(f"O₂ needed: {oxygen_needed_percent}%")
print(f"→ Convert {co2_to_convert:.1f}% CO₂ → O₂")
print(f"→ With 30% tech: {o2_producible:.1f}% O₂ possible")
print("MOXIE works.")
print("Scale it.")
print("Mars will breathe.")