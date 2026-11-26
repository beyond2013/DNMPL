"""Problem 52: Symmetric matrix check"""


def p52():
    def is_symmetric(m):
        n = len(m)
        return all(m[i][j] == m[j][i] for i in range(n) for j in range(n))

    print(is_symmetric([[1, 2, 3], [2, 4, 5], [3, 5, 6]]))   # True
    print(is_symmetric([[1, 2], [3, 4]]))                    # False


if __name__ == "__main__":
    p52()
