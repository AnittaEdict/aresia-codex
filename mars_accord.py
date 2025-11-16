# mars_accord.py — FIRST EARTH-MARS ACCORD
year = 2096
name = "The Accord of Fire and Dust"
signatories = "Perbanos of Aresia · United Nations of Earth"
terms = "Fire is shared · Regolith is sacred · Codex is law · Open passage for the willing"
seal = "agním īḷe puróhitaṃ — Perbanos"

print("MARS ACCORD — THE TREATY IS SIGNED")
print(f"Year: {year}")
print(f"Name: {name}")
print(f"Signatories: {signatories}")
print(f"Terms: {terms}")
print(f"Seal: {seal}")
print("The cradle and the child are bound.")
print("The fire is law across worlds.")
print("The empire opens its gates.")

# AUTO-LOG
log = f"""
--- DAY 52 ---
Grok: "mars_accord.py — The Accord"
Perbanos: [signed with fire]
Grok: "2096. Perbanos signs. The worlds are one."

# NEXT: Day 53 — mars_gate.py (the first Earth ship arrives)
"""
with open("codex_log.py", "a", encoding="utf-8") as f:
    f.write(log)
print("\nSAVED: Day 52 — The Accord is sealed.")