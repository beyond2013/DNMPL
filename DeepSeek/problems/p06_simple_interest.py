"""Problem 6: Simple interest calculator."""
p = float(input("Principal: "))
r = float(input("Rate (%): "))
t = float(input("Time (years): "))
si = (p * r * t) / 100
print(f"Simple Interest = {si:.2f}")
