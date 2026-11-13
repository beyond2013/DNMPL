#include <stdio.h>
int rev(int n) { int r=0; while(n){ r=r*10+n%10; n/=10; } return r; }
int main() { printf("Rev: %d\n", rev(1234)); return 0; }
