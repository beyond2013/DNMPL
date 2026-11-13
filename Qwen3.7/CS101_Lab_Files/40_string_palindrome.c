#include <stdio.h>
#include <string.h>
int main() {
    char str[50]; int i=0, j, isPal=1;
    printf("Enter string: "); scanf("%s", str);
    j = strlen(str) - 1;
    while(i<j) { if(str[i]!=str[j]) { isPal=0; break; } i++; j--; }
    printf(isPal ? "Palindrome\n" : "Not Palindrome\n");
    return 0;
}
