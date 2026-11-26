#include <stdio.h>
unsigned long long fact(int n) {
    unsigned long long f = 1;
    for (int i = 1; i <= n; i++) f *= i;
    return f;
}
int main() {
    int n, r; scanf("%d %d", &n, &r);
    unsigned long long nPr = fact(n) / fact(n - r);
    unsigned long long nCr = fact(n) / (fact(r) * fact(n - r));
    printf("nPr = %llu, nCr = %llu\n", nPr, nCr);
    return 0;
}