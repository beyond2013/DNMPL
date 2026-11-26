#include <stdio.h>
int main() {
    int arr[] = {1, 1, 2, 3, 3, 4}, n = 6, j = 0;
    if (n > 0) {
        for (int i = 0; i < n - 1; i++) {
            if (arr[i] != arr[i + 1]) arr[j++] = arr[i];
        }
        arr[j++] = arr[n - 1];
    }
    for (int i = 0; i < j; i++) printf("%d ", arr[i]);
    return 0;
}