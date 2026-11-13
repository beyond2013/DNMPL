"""Problem 26: Pyramid of stars"""


def p26():
    n = 5
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))


if __name__ == "__main__":
    p26()
