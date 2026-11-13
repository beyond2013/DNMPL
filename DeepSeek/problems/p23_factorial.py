"""Problem 23: Factorial of N."""
n = int(input("N: "))
f = 1
for i in range(2, n+1): f *= i
print(f"{n}! = {f}")
