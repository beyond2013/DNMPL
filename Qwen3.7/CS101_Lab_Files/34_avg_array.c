#include <stdio.h>
int main() {
    int arr[5]={10, 20, 30, 40, 50}, sum=0, i;
    for(i=0; i<5; i++) sum+=arr[i];
    printf("Avg: %.2f\n", (float)sum/5);
    return 0;
}
