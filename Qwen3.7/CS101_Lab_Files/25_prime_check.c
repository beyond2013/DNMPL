#include <stdio.h>
int main() {
    int n, i, isPrime=1;
    printf("Enter N: "); scanf("%d", &n);
    if(n<=1) isPrime=0;
    for(i=2; i*i<=n; i++) { if(n%i==0) { isPrime=0; break; } }
    printf(isPrime ? "Prime\n" : "Not Prime\n");
    return 0;
}
