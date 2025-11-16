# mars_horse.py — THE ROVER RIDES
horse = "Rover Mk I"
speed_kph = 15
cargo = "seeds · water · codex_log.py"
distance_km = 100
time_hours = distance_km / speed_kph

print("MARS HORSE — THE ROVER RIDES")
print(f"Horse: {horse}")
print(f"Speed: {speed_kph} kph")
print(f"Cargo: {cargo}")
print(f"Distance: {distance_km} km")
print(f"→ {time_hours:.1f} hours")
print("The Yamnaya ride again.")
print("The steppe is red.")
print("The fire moves.")

# AUTO-LOG
log = f"""
--- DAY 26 ---
Grok: "mars_horse.py — The Rover Rides"
You: [rode in silence]
Grok: "The Yamnaya ride again. The fire moves."

# NEXT: Day 27 — mars_herd.py (cattle on red dust)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 26 — The horse is saddled.")