#include <stdio.h>
int main() {
    int n;
    printf("Enter number of terms: "); scanf("%d", &n);
    long long t1 = 0, t2 = 1, next;
    for (int i = 1; i <= n; i++) {
        printf("%lld ", t1);
        next = t1 + t2;
        t1 = t2;
        t2 = next;
    }
    printf("\n");
    return 0;
}