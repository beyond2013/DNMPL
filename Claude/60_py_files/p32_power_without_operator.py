"""Problem 32: power(base, exp) without ** operator"""


def p32():
    def power(base, exp):
        result = 1
        for _ in range(abs(exp)):
            result *= base
        return result if exp >= 0 else 1 / result

    print("2^10 =", power(2, 10))
    print("5^0  =", power(5, 0))
    print("2^-3 =", power(2, -3))


if __name__ == "__main__":
    p32()
