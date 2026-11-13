"""Problem 30: GCD and LCM using Euclidean algorithm."""
a, b = map(int, input("Two numbers: ").split())
x, y = a, b
while y: x, y = y, x % y
print(f"GCD = {x}, LCM = {a*b//x}")
