#include <stdio.h>
int main() {
    int A[2][2] = {{1, 2}, {3, 4}}, B[2][2] = {{5, 6}, {7, 8}}, C[2][2];
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++) C[i][j] = A[i][j] + B[i][j];
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) printf("%d ", C[i][j]);
        printf("\n");
    }
    return 0;
}