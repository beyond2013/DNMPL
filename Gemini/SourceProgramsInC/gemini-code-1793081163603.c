#include <stdio.h>
double power(double base, int exp) {
    double res = 1;
    int abs_exp = exp < 0 ? -exp : exp;
    for (int i = 0; i < abs_exp; i++) res *= base;
    return exp < 0 ? 1.0 / res : res;
}
int main() {
    printf("%.2lf\n", power(2.0, -3));
    return 0;
}