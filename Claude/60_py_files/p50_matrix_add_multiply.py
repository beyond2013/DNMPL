"""Problem 50: Matrix addition and multiplication"""


def show(matrix):
    for row in matrix:
        print("  ".join(f"{x:3}" for x in row))


def p50():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    n = len(a)
    add = [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]
    mul = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mul[i][j] += a[i][k] * b[k][j]
    print("A + B:")
    show(add)
    print("A x B:")
    show(mul)


if __name__ == "__main__":
    p50()
