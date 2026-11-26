"""Problem 38: Count even and odd elements"""


def p38():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even = sum(1 for x in data if x % 2 == 0)
    print(f"Even = {even}, Odd = {len(data) - even}")


if __name__ == "__main__":
    p38()
