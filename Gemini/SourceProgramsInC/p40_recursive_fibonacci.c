#include <stdio.h>
int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
int main() {
    printf("Fib(6) = %d\n", fib(6));
    return 0;
}