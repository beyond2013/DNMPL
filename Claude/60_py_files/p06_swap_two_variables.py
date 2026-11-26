"""Problem 6: Swap two variables (with and without a temporary)"""


def p06():
    a, b = 10, 20
    print("Before:", a, b)
    temp = a            # method 1: temporary variable
    a = b
    b = temp
    print("With temp:", a, b)

    a, b = 10, 20       # reset to the original values
    a = a + b           # method 2: arithmetic, no temporary
    b = a - b
    a = a - b
    print("Without temp:", a, b)

    a, b = 10, 20
    a, b = b, a         # method 3: Python's tuple swap
    print("Pythonic:", a, b)


if __name__ == "__main__":
    p06()
