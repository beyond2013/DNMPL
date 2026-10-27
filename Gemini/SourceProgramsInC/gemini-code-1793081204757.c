#include <stdio.h>
#define PI 3.14159
float areaCircle(float r) { return PI * r * r; }
float areaRect(float l, float w) { return l * w; }
int main() {
    printf("Circle: %.2f, Rect: %.2f\n", areaCircle(3), areaRect(4, 5));
    return 0;
}