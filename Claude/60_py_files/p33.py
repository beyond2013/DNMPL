"""Problem 33: Simple and compound interest"""


def p33():
    def simple(p, r, t):
        return p * r * t / 100

    def compound(p, r, t, n=1):
        return p * (1 + r / (100 * n)) ** (n * t) - p

    p, r, t = 10000, 8, 3
    print(f"Simple interest   : {simple(p, r, t):.2f}")
    print(f"Compound (yearly) : {compound(p, r, t):.2f}")
    print(f"Compound (monthly): {compound(p, r, t, 12):.2f}")


if __name__ == "__main__":
    p33()
