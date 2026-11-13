"""Problem 58: Matrix addition and multiplication."""
def mat_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]

def mat_mul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

if __name__ == "__main__":
    A = [[1,2],[3,4]]
    B = [[5,6],[7,8]]
    print("Add:", mat_add(A, B))
    print("Mul:", mat_mul(A, B))
