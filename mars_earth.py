# mars_earth.py — MESSAGE TO EARTH
year = 2095
sender = "FIRE-PRIEST ARESIAN I"
receiver = "Earth — All Nations"
medium = "Aresia Orbital Laser Array"
message = "We are the children of the steppe and the void. The fire is shared. The red dust is home. Join us — or watch from afar."
signature = "agním īḷe puróhitaṃ"

print("MARS EARTH — MESSAGE TO THE CRADLE")
print(f"Year: {year}")
print(f"Sender: {sender}")
print(f"Receiver: {receiver}")
print(f"Medium: {medium}")
print(f"Message: {message}")
print(f"Signature: {signature}")
print("The empire speaks to its mother.")
print("The fire crosses the void.")
print("The horde invites the lost.")

# AUTO-LOG
log = f"""
--- DAY 50 ---
Grok: "mars_earth.py — Message to Earth"
You: [sent the beam]
Grok: "Laser array. 2095. The cradle hears the child."

# NEXT: Day 51 — mars_reply.py (Earth's answer)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 50 — The message is sent.")