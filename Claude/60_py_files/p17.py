"""Problem 17: Sum of first N natural numbers"""


def p17():
    n = 100
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f"Loop sum = {total}, formula n(n+1)/2 = {n * (n + 1) // 2}")


if __name__ == "__main__":
    p17()
