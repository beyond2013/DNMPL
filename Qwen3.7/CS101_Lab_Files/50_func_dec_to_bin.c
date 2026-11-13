#include <stdio.h>
void decToBin(int n) {
    if(n>1) decToBin(n/2);
    printf("%d", n%2);
}
int main() { printf("Bin: "); decToBin(13); printf("\n"); return 0; }
