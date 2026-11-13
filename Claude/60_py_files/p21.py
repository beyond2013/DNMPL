"""Problem 21: Sum of digits"""


def p21():
    n = 4829
    total, temp = 0, n
    while temp > 0:
        total += temp % 10
        temp //= 10
    print(f"Sum of digits of {n} = {total}")


if __name__ == "__main__":
    p21()
