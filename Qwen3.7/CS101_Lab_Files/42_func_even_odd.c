#include <stdio.h>
void check(int n) { printf(n%2==0 ? "Even\n" : "Odd\n"); }
int main() { check(10); check(7); return 0; }
