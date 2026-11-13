"""Problem 18: Factorial"""


def p18():
    n = 6
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    print(f"{n}! = {fact}")


if __name__ == "__main__":
    p18()
