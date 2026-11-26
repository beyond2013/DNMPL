#include <stdio.h>
int main() {
    int units;
    float bill = 0;
    printf("Enter units consumed: ");
    scanf("%d", &units);
    if (units <= 100) bill = units * 1.0;
    else if (units <= 300) bill = 100 * 1.0 + (units - 100) * 1.5;
    else bill = 100 * 1.0 + 200 * 1.5 + (units - 300) * 2.0;
    printf("Total Bill: $%.2f\n", bill);
    return 0;
}