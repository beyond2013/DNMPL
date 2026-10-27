#include <stdio.h>
int main() {
    int mat[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, d_sum = 0;
    for (int i = 0; i < 3; i++) d_sum += mat[i][i];
    printf("Diagonal Sum: %d\n", d_sum);
    return 0;
}