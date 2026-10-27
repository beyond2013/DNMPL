#include <stdio.h>
int main() {
    int arr[] = {10, 23, 45, 70}, target = 45, idx = -1;
    for (int i = 0; i < 4; i++) {
        if (arr[i] == target) { idx = i; break; }
    }
    printf("Found at index: %d\n", idx);
    return 0;
}