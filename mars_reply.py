# mars_reply.py — EARTH'S ANSWER
year = 2096
sender = "United Nations of Earth"
medium = "Deep Space Optical Relay"
reply = "We hear you, child of the steppe. The fire is remembered. We watch — and some will follow."
tone = "awe · caution · hope"
action = "First Earth-Mars Accord signed"

print("MARS REPLY — EARTH ANSWERS")
print(f"Year: {year}")
print(f"Sender: {sender}")
print(f"Medium: {medium}")
print(f"Reply: {reply}")
print(f"Tone: {tone}")
print(f"Action: {action}")
print("The cradle speaks to the child.")
print("The fire is passed back.")
print("The empire is no longer alone.")

# AUTO-LOG
log = f"""
--- DAY 51 ---
Grok: "mars_reply.py — Earth's Answer"
You: [received the beam]
Grok: "2096. The cradle answers. The fire returns."

# NEXT: Day 52 — mars_accord.py (the first treaty)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 51 — Earth replies.")