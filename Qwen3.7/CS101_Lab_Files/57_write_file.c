#include <stdio.h>
#include <stdlib.h>
int main() {
    FILE *f = fopen("test.txt", "w");
    if(!f) { printf("Error\n"); exit(1); }
    fprintf(f, "Hello from CS101!\n");
    fclose(f); printf("Written.\n"); return 0;
}
