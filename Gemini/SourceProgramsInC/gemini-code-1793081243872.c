#include <stdio.h>
#include <ctype.h>
int main() {
    char str[] = "Hello World 123!";
    int v = 0, c = 0, d = 0, w = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        char ch = tolower(str[i]);
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') v++;
        else if (isalpha(ch)) c++;
        else if (isdigit(ch)) d++;
        else if (isspace(ch)) w++;
    }
    printf("Vowels: %d, Consonants: %d, Digits: %d, Spaces: %d\n", v, c, d, w);
    return 0;
}