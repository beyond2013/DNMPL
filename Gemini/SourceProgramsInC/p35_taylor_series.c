#include <stdio.h>
#include <math.h>
int main() {
    double x, term, sum;
    int n;
    printf("Enter x in radians: "); scanf("%lf", &x);
    printf("Enter number of terms: "); scanf("%d", &n);
    sum = term = x;
    for (int i = 1; i < n; i++) {
        term = -term * x * x / ((2 * i) * (2 * i + 1));
        sum += term;
    }
    printf("sin(%.2lf) = %.4lf\n", x, sum);
    return 0;
}