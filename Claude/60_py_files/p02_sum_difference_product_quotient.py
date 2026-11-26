"""Problem 2: Sum, difference, product, quotient, remainder"""


def p02():
    a, b = 17, 5
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    if b != 0:
        print(f"{a} / {b} = {a / b:.2f}  (integer quotient {a // b})")
        print(f"{a} % {b} = {a % b}")
    else:
        print("Cannot divide by zero")


if __name__ == "__main__":
    p02()
