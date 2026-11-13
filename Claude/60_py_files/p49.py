"""Problem 49: Print a matrix and its transpose"""


def show(matrix):
    for row in matrix:
        print("  ".join(f"{x:3}" for x in row))


def p49():
    m = [[1, 2, 3], [4, 5, 6]]
    print("Matrix:")
    show(m)
    t = [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]
    print("Transpose:")
    show(t)


if __name__ == "__main__":
    p49()
