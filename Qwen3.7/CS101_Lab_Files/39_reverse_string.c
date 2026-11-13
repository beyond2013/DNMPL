#include <stdio.h>
#include <string.h>
int main() {
    char str[50], temp; int i=0, j;
    printf("Enter string: "); scanf("%s", str);
    j = strlen(str) - 1;
    while(i<j) { temp=str[i]; str[i]=str[j]; str[j]=temp; i++; j--; }
    printf("Reversed: %s\n", str);
    return 0;
}
