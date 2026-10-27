#include <stdio.h>
int main() {
    int n, orig, rev = 0;
    printf("Enter integer: "); scanf("%d", &n);
    orig = n;
    while (n > 0) {
        rev = rev * 10 + n % 10;
        n /= 10;
    }
    if (orig == rev) printf("Palindrome\n"); else printf("Not Palindrome\n");
    return 0;
}