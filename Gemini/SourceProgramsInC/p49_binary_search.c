#include <stdio.h>
int main() {
    int arr[] = {2, 5, 8, 12, 16, 23, 38}, target = 16;
    int l = 0, r = 6, mid, found = -1;
    while (l <= r) {
        mid = l + (r - l) / 2;
        if (arr[mid] == target) { found = mid; break; }
        if (arr[mid] < target) l = mid + 1;
        else r = mid - 1;
    }
    printf("Index: %d\n", found);
    return 0;
}