"""Problem 32: Armstrong number (3-digit)."""
n = int(input("3-digit number: "))
s = sum(int(d)**3 for d in str(n))
print("Armstrong" if s == n else "Not Armstrong")
