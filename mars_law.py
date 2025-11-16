# mars_law.py — SECOND LAW: THE REGOLITH LAW
year = 2040
law = "Regolith is sacred. It shields, builds, and crowns. To waste it is exile."
enforcer = "The Priest on Olympus Dome"
punishment = "buried in dust without suit"
reward = "a brick in the dome"

print("MARS LAW — SECOND LAW OF ARESIA")
print(f"Year: {year}")
print(f"Law: {law}")
print(f"Enforcer: {enforcer}")
print(f"Punishment: {punishment}")
print(f"Reward: {reward}")
print("The red dust is law.")
print("The empire is built on it.")
print("The fire honors the dust.")

# AUTO-LOG
log = f"""
--- DAY 40 ---
Grok: "mars_law.py — Second Law"
You: [proclaimed the dust]
Grok: "Regolith is sacred. The empire rises from red bones."

# NEXT: Day 41 — mars_dome.py (the first city dome)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 40 — The dust is law.")