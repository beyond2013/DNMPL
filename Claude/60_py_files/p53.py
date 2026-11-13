"""Problem 53: Factorial and Fibonacci: recursive vs iterative"""


def fact_rec(n):
    return 1 if n <= 1 else n * fact_rec(n - 1)


def fib_rec(n):
    return n if n < 2 else fib_rec(n - 1) + fib_rec(n - 2)


def p53():
    def fact_iter(n):
        r = 1
        for i in range(2, n + 1):
            r *= i
        return r

    def fib_iter(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    print("6!   recursive:", fact_rec(6), "| iterative:", fact_iter(6))
    print("fib(10) recursive:", fib_rec(10), "| iterative:", fib_iter(10))
    print("Note: recursive Fibonacci repeats work and is exponentially slow.")


if __name__ == "__main__":
    p53()
