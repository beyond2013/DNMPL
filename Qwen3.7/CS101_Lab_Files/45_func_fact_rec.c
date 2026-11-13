#include <stdio.h>
long long fact(int n) { return (n<=1) ? 1 : n * fact(n-1); }
int main() { printf("Fact: %lld\n", fact(5)); return 0; }
