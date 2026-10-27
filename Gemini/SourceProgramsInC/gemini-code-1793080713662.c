#include <stdio.h>
int main() {
    float a, b, c;
    printf("Enter three side lengths: ");
    scanf("%f %f %f", &a, &b, &c);
    if (a + b > c && a + c > b && b + c > a) {
        if (a == b && b == c) printf("Equilateral\n");
        else if (a == b || b == c || a == c) printf("Isosceles\n");
        else printf("Scalene\n");
    } else {
        printf("Not a valid triangle.\n");
    }
    return 0;
}