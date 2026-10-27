#include <stdio.h>
float add(float a, float b) { return a + b; }
float sub(float a, float b) { return a - b; }
int main() {
    float a = 10, b = 5;
    printf("Sum: %.2f, Diff: %.2f\n", add(a, b), sub(a, b));
    return 0;
}