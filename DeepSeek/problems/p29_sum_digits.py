"""Problem 29: Sum of digits."""
n = int(input("Number: "))
print(f"Sum of digits = {sum(int(d) for d in str(abs(n)))}")
