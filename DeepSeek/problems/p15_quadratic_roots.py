"""Problem 15: Roots of a quadratic equation."""
import math
a, b, c = map(float, input("a b c: ").split())
d = b*b - 4*a*c
if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Two real roots: {r1:.2f}, {r2:.2f}")
elif d == 0:
    print(f"One root: {-b/(2*a):.2f}")
else:
    print("Complex roots")
