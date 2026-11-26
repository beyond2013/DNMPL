#include <stdio.h>
#include <string.h>
int main() {
    char str[] = "madam";
    int l = 0, r = strlen(str) - 1, is_pal = 1;
    while (l < r) {
        if (str[l++] != str[r--]) { is_pal = 0; break; }
    }
    printf(is_pal ? "Palindrome\n" : "Not Palindrome\n");
    return 0;
}