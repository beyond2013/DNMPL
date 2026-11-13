#include <stdio.h>
int addPtr(int *a, int *b) { return *a + *b; }
int main() { int x=5, y=10; printf("Sum: %d\n", addPtr(&x, &y)); return 0; }
