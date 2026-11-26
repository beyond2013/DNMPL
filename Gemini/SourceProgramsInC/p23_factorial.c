#include <stdio.h>
int main() {
    int n;
    unsigned long long fact = 1;
    printf("Enter positive integer: "); scanf("%d", &n);
    int i = 1;
    while (i <= n) {
        fact *= i;
        i++;
    }
    printf("Factorial = %llu\n", fact);
    return 0;
}