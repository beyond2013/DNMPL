"""Problem 30: isPrime and twin primes"""


def is_prime(n):
    """Shared helper: trial division up to sqrt(n)."""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def p30():
    twins = [(p, p + 2) for p in range(2, 100) if is_prime(p) and is_prime(p + 2)]
    print("Twin primes below 100:", twins)


if __name__ == "__main__":
    p30()
