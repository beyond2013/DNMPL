#include <stdio.h>
int main() {
    int arr[] = {1, 2, 2, 3, 1, 4, 2}, n = 7, visited[7] = {0};
    for (int i = 0; i < n; i++) {
        if (visited[i]) continue;
        int count = 1;
        for (int j = i + 1; j < n; j++) {
            if (arr[i] == arr[j]) { visited[j] = 1; count++; }
        }
        printf("%d occurs %d times\n", arr[i], count);
    }
    return 0;
}