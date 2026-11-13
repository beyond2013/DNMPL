#include <stdio.h>
#include <stdlib.h>
int main() {
    FILE *f = fopen("test.txt", "a");
    if(!f) { printf("Error\n"); exit(1); }
    fprintf(f, "Appended line.\n");
    fclose(f); printf("Appended.\n"); return 0;
}
