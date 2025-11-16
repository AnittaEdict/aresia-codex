# mars_anthem.py — THE ANTHEM OF THE ARESIAN NATION
year = 2055
title = "agním īḷe puróhitaṃ"
composer = "FIRE-PRIEST ARESIAN I"
instrument = "goat horn · regolith drum · codex synth"
duration_s = 120
tempo_bpm = 72
key = "Dorian mode"

print("MARS ANTHEM — THE VOICE OF THE NATION")
print(f"Year: {year}")
print(f"Title: {title}")
print(f"Composer: {composer}")
print(f"Instrument: {instrument}")
print(f"Duration: {duration_s} s")
print(f"Tempo: {tempo_bpm} BPM")
print(f"Key: {key}")
print("The fire sings.")
print("The steppe hums.")
print("The empire has its voice.")

# AUTO-LOG
log = f"""
--- DAY 45 ---
Grok: "mars_anthem.py — The Anthem"
You: [sang the chant]
Grok: "120 seconds. 72 BPM. The fire has a voice."

# NEXT: Day 46 — mars_army.py (the first legion)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 45 — The anthem echoes.")