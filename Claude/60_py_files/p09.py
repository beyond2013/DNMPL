"""Problem 9: Largest of three numbers"""


def p09():
    a, b, c = 14, 42, 27
    if a >= b and a >= c:
        largest = a
    elif b >= c:
        largest = b
    else:
        largest = c
    print(f"Largest of {a}, {b}, {c} is {largest}")


if __name__ == "__main__":
    p09()
