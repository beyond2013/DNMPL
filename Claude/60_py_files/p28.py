"""Problem 28: Armstrong numbers between 1 and 1000"""


def p28():
    result = []
    for n in range(1, 1001):
        digits = len(str(n))
        total, temp = 0, n
        while temp > 0:
            total += (temp % 10) ** digits
            temp //= 10
        if total == n:
            result.append(n)
    print(result)


if __name__ == "__main__":
    p28()
