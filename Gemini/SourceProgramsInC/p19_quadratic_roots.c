#include <stdio.h>
#include <math.h>
int main() {
    double a, b, c, disc, r1, r2, real, imag;
    printf("Enter coefficients a, b, c: ");
    scanf("%lf %lf %lf", &a, &b, &c);
    disc = b * b - 4 * a * c;
    if (disc > 0) {
        r1 = (-b + sqrt(disc)) / (2 * a);
        r2 = (-b - sqrt(disc)) / (2 * a);
        printf("Real and distinct roots: %.2lf and %.2lf\n", r1, r2);
    } else if (disc == 0) {
        r1 = -b / (2 * a);
        printf("Real and equal roots: %.2lf\n", r1);
    } else {
        real = -b / (2 * a);
        imag = sqrt(-disc) / (2 * a);
        printf("Complex roots: %.2lf + %.2lfi and %.2lf - %.2lfi\n", real, imag, real, imag);
    }
    return 0;
}