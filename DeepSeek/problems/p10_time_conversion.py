"""Problem 10: Convert total seconds to hours, minutes, seconds."""
total = int(input("Total seconds: "))
h, rem = divmod(total, 3600)
m, s = divmod(rem, 60)
print(f"{h}h {m}m {s}s")
