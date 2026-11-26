#include <stdio.h>
#include <string.h>
int main() {
    char str[] = "programming";
    int freq[26] = {0};
    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] >= 'a' && str[i] <= 'z') freq[str[i] - 'a']++;
    }
    for (int i = 0; i < 26; i++) {
        if (freq[i] > 0) printf("%c: %d\n", i + 'a', freq[i]);
    }
    return 0;
}