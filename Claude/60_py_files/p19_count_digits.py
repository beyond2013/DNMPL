"""Problem 19: Count digits"""


def p19():
    n = 987654
    count, temp = 0, abs(n)
    if temp == 0:
        count = 1
    while temp > 0:
        temp //= 10
        count += 1
    print(f"{n} has {count} digits")


if __name__ == "__main__":
    p19()
