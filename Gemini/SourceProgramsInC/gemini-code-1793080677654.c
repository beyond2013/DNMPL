#include <stdio.h>
int main() {
    float basic, hra, da, gross;
    printf("Enter basic salary: ");
    scanf("%f", &basic);
    hra = 0.40 * basic;
    da = 0.20 * basic;
    gross = basic + hra + da;
    printf("Gross Salary: %.2f\n", gross);
    return 0;
}