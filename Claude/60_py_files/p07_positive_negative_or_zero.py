"""Problem 7: Positive, negative, or zero"""


def p07():
    for n in (5, -3, 0):
        if n > 0:
            print(n, "is positive")
        elif n < 0:
            print(n, "is negative")
        else:
            print(n, "is zero")


if __name__ == "__main__":
    p07()
