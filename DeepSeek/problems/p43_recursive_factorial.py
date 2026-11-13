"""Problem 43: Recursive factorial."""
def fact(n):
    return 1 if n <= 1 else n * fact(n-1)

if __name__ == "__main__":
    print(fact(6))
