#include <stdio.h>
int main() {
    int type, hours;
    float fee = 0;
    printf("Enter vehicle type (1: Bike, 2: Car, 3: Truck) and hours: ");
    scanf("%d %d", &type, &hours);
    switch(type) {
        case 1: fee = hours * 2.0; break;
        case 2: fee = hours * 5.0; break;
        case 3: fee = hours * 10.0; break;
        default: printf("Invalid vehicle type.\n"); return 0;
    }
    printf("Parking Fee: $%.2f\n", fee);
    return 0;
}