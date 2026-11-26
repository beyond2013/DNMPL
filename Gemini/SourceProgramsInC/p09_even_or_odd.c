#include <stdio.h>
int main() {
    int n;
    printf("Enter an integer: ");
    scanf("%d", &n);
    if (n % 2 == 0) printf("%d is Even.\n", n);
    else printf("%d is Odd.\n", n);
    return 0;
}