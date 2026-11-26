#include <stdio.h>
int main() {
    int a, b;
    printf("Enter range A and B: "); scanf("%d %d", &a, &b);
    for (int i = a; i <= b; i++) {
        if (i <= 1) continue;
        int prime = 1;
        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) { prime = 0; break; }
        }
        if (prime) printf("%d ", i);
    }
    printf("\n");
    return 0;
}