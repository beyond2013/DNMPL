"""Problem 16: Multiplication table"""


def p16():
    n = 7
    for i in range(1, 11):
        print(f"{n} x {i:2} = {n * i}")


if __name__ == "__main__":
    p16()
