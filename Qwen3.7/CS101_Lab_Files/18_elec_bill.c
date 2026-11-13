#include <stdio.h>
int main() {
    int u; float bill;
    printf("Enter units: "); scanf("%d", &u);
    if(u<=100) bill=u*10;
    else if(u<=200) bill=1000+(u-100)*15;
    else bill=2500+(u-200)*20;
    printf("Bill: %.2f\n", bill);
    return 0;
}
