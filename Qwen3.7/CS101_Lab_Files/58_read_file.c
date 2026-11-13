#include <stdio.h>
#include <stdlib.h>
int main() {
    FILE *f = fopen("test.txt", "r");
    char ch;
    if(!f) { printf("Error\n"); exit(1); }
    while((ch = fgetc(f)) != EOF) printf("%c", ch);
    fclose(f); return 0;
}
