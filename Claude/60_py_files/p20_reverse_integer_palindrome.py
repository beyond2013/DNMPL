"""Problem 20: Reverse an integer and test palindrome"""


def p20():
    for n in (12321, 12345):
        reversed_n, temp = 0, n
        while temp > 0:
            reversed_n = reversed_n * 10 + temp % 10
            temp //= 10
        verdict = "is" if reversed_n == n else "is not"
        print(f"{n} reversed = {reversed_n}; {verdict} a palindrome")


if __name__ == "__main__":
    p20()
