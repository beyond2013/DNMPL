"""Problem 10: Leap year"""


def p10():
    def is_leap(y):
        return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

    for year in (1900, 2000, 2024, 2026):
        print(year, "is a leap year" if is_leap(year) else "is not a leap year")


if __name__ == "__main__":
    p10()
