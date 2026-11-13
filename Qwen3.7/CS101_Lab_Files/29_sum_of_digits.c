#include <stdio.h>
int main() {
    int n, sum=0, rem;
    printf("Enter N: "); scanf("%d", &n);
    while(n!=0) { sum+=n%10; n/=10; }
    printf("Sum: %d\n", sum);
    return 0;
}
