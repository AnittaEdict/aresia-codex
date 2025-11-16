# light_lag.py — Mars Delay
distance_km = 225_000_000
light_speed_kms = 299_792

time_seconds = distance_km / light_speed_kms
time_minutes = time_seconds / 60

print("MARS COMMUNICATION DELAY")
print(f"Distance: {distance_km:,} km")
print(f"One-way: {time_minutes:.1f} minutes")
print(f"Round-trip: {time_minutes*2:.1f} minutes")
print("agním īḷe — sent now, heard in 12.5 min")