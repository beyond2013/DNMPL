"""Problem 13: Triangle validity and type"""


def p13():
    def classify(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return "Invalid (sides must be positive)"
        if a + b <= c or a + c <= b or b + c <= a:
            return "Not a triangle"
        if a == b == c:
            return "Equilateral"
        if a == b or b == c or a == c:
            return "Isosceles"
        return "Scalene"

    for sides in [(3, 3, 3), (5, 5, 8), (3, 4, 5), (1, 2, 3)]:
        print(sides, "->", classify(*sides))


if __name__ == "__main__":
    p13()
