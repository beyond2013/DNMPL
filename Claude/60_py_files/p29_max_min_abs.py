"""Problem 29: max, min, abs functions"""


def p29():
    def my_max(a, b):
        return a if a >= b else b

    def my_min(a, b):
        return a if a <= b else b

    def my_abs(x):
        return -x if x < 0 else x

    print("max(7, 12) =", my_max(7, 12))
    print("min(7, 12) =", my_min(7, 12))
    print("abs(-9.5)  =", my_abs(-9.5))


if __name__ == "__main__":
    p29()
