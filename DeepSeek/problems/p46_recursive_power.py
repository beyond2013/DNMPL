"""Problem 46: Recursive power x^n."""
def power(x, n):
    return 1 if n == 0 else x * power(x, n-1)

if __name__ == "__main__":
    print(power(2, 10))
