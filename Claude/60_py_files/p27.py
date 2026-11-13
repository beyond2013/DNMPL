"""Problem 27: Pascal's triangle"""


def p27():
    rows = 6
    for i in range(rows):
        value = 1
        line = []
        for j in range(i + 1):
            line.append(str(value))
            value = value * (i - j) // (j + 1)   # C(i, j+1) from C(i, j)
        print(" ".join(line).center(rows * 4))


if __name__ == "__main__":
    p27()
