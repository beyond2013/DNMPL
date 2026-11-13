#include <stdio.h>
long long fact(int n) { long long f=1; for(int i=1;i<=n;i++) f*=i; return f; }
int main() { printf("Fact: %lld\n", fact(5)); return 0; }
