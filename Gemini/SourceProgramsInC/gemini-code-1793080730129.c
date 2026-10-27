#include <stdio.h>
int main() {
    int n, sum = 0;
    printf("Enter N: "); scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        printf("%d ", i);
        sum += i;
    }
    printf("\nSum: %d\n", sum);
    return 0;
}