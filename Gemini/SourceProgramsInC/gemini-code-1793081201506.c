#include <stdio.h>
void decToBin(int n) {
    int bin[32], i = 0;
    if (n == 0) { printf("0\n"); return; }
    while (n > 0) { bin[i++] = n % 2; n /= 2; }
    for (int j = i - 1; j >= 0; j--) printf("%d", bin[j]);
    printf("\n");
}
int main() {
    decToBin(10);
    return 0;
}