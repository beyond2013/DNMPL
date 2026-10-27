#include <stdio.h>
int main() {
    int arr[] = {12, 45, 2, 67, 34};
    int n = 5, min = arr[0], max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] < min) min = arr[i];
        if (arr[i] > max) max = arr[i];
    }
    printf("Min: %d, Max: %d\n", min, max);
    return 0;
}