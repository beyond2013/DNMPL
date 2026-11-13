"""Problem 24: GCD and LCM (Euclid)"""


def p24():
    a, b = 48, 18
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    gcd = x
    lcm = a * b // gcd
    print(f"GCD({a}, {b}) = {gcd}, LCM({a}, {b}) = {lcm}")


if __name__ == "__main__":
    p24()
