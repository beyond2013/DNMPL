"""Problem 23: Prime check and primes up to N"""


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


def p23():
    print("97 prime?", is_prime(97), "| 91 prime?", is_prime(91))
    n = 50
    print(f"Primes up to {n}:", [x for x in range(2, n + 1) if is_prime(x)])


if __name__ == "__main__":
    p23()
