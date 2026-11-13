#include <stdio.h>
int main() {
    int arr[5]={10, 20, 30, 40, 50}, key=30, i, found=0;
    for(i=0; i<5; i++) { if(arr[i]==key) { found=1; break; } }
    printf(found ? "Found at %d\n" : "Not Found\n", i);
    return 0;
}
