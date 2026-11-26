"""Problem 8: Even or odd"""


def p08():
    for n in (10, 7):
        print(n, "is", "even" if n % 2 == 0 else "odd")


if __name__ == "__main__":
    p08()
