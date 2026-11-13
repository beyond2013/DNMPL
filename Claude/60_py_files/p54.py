"""Problem 54: Sum of digits (recursive)"""


def p54():
    def digit_sum(n):
        return n if n < 10 else n % 10 + digit_sum(n // 10)

    print("Digit sum of 4829 =", digit_sum(4829))


if __name__ == "__main__":
    p54()
