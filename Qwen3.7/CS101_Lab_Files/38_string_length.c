#include <stdio.h>
int main() {
    char str[50]; int len=0;
    printf("Enter string: "); scanf("%s", str);
    while(str[len]) len++;
    printf("Length: %d\n", len);
    return 0;
}
