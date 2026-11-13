#include <stdio.h>
int main() {
    int arr[5]={12, 45, 2, 89, 34}, max=arr[0], i;
    for(i=1; i<5; i++) if(arr[i]>max) max=arr[i];
    printf("Max: %d\n", max);
    return 0;
}
