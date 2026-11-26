#include <stdio.h>
int main() {
    int n, orig, rem, sum = 0;
    printf("Enter 3-digit integer: "); scanf("%d", &n);
    orig = n;
    while (n != 0) {
        rem = n % 10;
        sum += rem * rem * rem;
        n /= 10;
    }
    if (sum == orig) printf("Armstrong Number\n"); else printf("Not Armstrong\n");
    return 0;
}