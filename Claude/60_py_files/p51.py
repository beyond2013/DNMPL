"""Problem 51: Row sums, column sums, diagonal sums"""


def p51():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n = len(m)
    print("Row sums   :", [sum(row) for row in m])
    print("Column sums:", [sum(m[i][j] for i in range(n)) for j in range(n)])
    print("Main diagonal:", sum(m[i][i] for i in range(n)))
    print("Anti diagonal:", sum(m[i][n - 1 - i] for i in range(n)))


if __name__ == "__main__":
    p51()
