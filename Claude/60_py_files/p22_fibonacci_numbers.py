"""Problem 22: First N Fibonacci numbers"""


def p22():
    n = 12
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


if __name__ == "__main__":
    p22()
