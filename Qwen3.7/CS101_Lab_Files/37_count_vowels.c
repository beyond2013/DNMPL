#include <stdio.h>
int main() {
    char str[50]; int i=0, count=0;
    printf("Enter string: "); scanf("%s", str);
    while(str[i]) {
        char c = str[i];
        if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||c=='A'||c=='E'||c=='I'||c=='O'||c=='U') count++;
        i++;
    }
    printf("Vowels: %d\n", count);
    return 0;
}
