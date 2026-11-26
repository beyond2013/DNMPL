"""Problem 14: Slab-based electricity bill"""


def p14():
    def bill(units):
        # first 100 units @10, next 100 @15, next 100 @20, rest @25
        slabs = [(100, 10), (100, 15), (100, 20)]
        total, remaining = 0, units
        for size, rate in slabs:
            used = min(remaining, size)
            total += used * rate
            remaining -= used
        total += remaining * 25
        return total

    for units in (80, 150, 250, 400):
        print(f"{units} units -> Rs {bill(units)}")


if __name__ == "__main__":
    p14()
