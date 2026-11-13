#include <stdio.h>
int main() {
    int arr[5]={12, 45, 2, 89, 34}, min=arr[0], i;
    for(i=1; i<5; i++) if(arr[i]<min) min=arr[i];
    printf("Min: %d\n", min);
    return 0;
}
