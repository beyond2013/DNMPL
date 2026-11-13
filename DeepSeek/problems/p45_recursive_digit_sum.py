"""Problem 45: Recursive sum of digits."""
def digit_sum(n):
    return 0 if n == 0 else n % 10 + digit_sum(n // 10)

if __name__ == "__main__":
    print(digit_sum(1234))
