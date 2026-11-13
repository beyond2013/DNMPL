#include <stdio.h>
int max3(int a, int b, int c) {
    if(a>=b && a>=c) return a;
    if(b>=c) return b;
    return c;
}
int main() { printf("Max: %d\n", max3(10, 25, 15)); return 0; }
