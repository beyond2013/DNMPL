#include <stdio.h>
#include <ctype.h>
int main() {
    char ch;
    printf("Enter a character: ");
    scanf(" %c", &ch);
    ch = tolower(ch);
    switch (ch) {
        case 'a': case 'e': case 'i': case 'o': case 'u':
            printf("Vowel\n"); break;
        default:
            if (isalpha(ch)) printf("Consonant\n");
            else printf("Not an alphabet character.\n");
    }
    return 0;
}