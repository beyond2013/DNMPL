"""Problem 11: Percentage to grade"""


def p11():
    def grade(p):
        if p < 0 or p > 100:
            return "Invalid"
        if p >= 80:
            return "A"
        if p >= 70:
            return "B"
        if p >= 60:
            return "C"
        if p >= 50:
            return "D"
        return "F"

    for p in (92, 74.5, 61, 50, 35, 120):
        print(f"{p}% -> {grade(p)}")


if __name__ == "__main__":
    p11()
