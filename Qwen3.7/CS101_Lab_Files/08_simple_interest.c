#include <stdio.h>
int main() {
    float p, r, t, si;
    printf("Enter P, R, T: "); scanf("%f %f %f", &p, &r, &t);
    si = (p * r * t) / 100;
    printf("SI: %.2f\n", si);
    return 0;
}
