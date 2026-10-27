#include <stdio.h>
#include <ctype.h>
int main() {
    char str[] = "hello world from c";
    int capitalize = 1;
    for (int i = 0; str[i] != '\0'; i++) {
        if (isspace(str[i])) capitalize = 1;
        else if (capitalize) { str[i] = toupper(str[i]); capitalize = 0; }
    }
    printf("%s\n", str);
    return 0;
}