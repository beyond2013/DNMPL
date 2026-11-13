#include <stdio.h>
int main() {
    int arr[3]={10, 20, 30}, *p=arr;
    for(int i=0; i<3; i++) { printf("%d ", *p); p++; }
    printf("\n"); return 0;
}
