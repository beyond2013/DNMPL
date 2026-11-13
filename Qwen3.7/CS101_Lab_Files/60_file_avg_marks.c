#include <stdio.h>
#include <stdlib.h>
int main() {
    FILE *f = fopen("marks.txt", "w");
    fprintf(f, "85\n90\n75\n"); fclose(f); // Create dummy data
    
    f = fopen("marks.txt", "r");
    int mark, sum=0, count=0;
    while(fscanf(f, "%d", &mark) != EOF) { sum+=mark; count++; }
    fclose(f);
    printf("Average: %.2f\n", (float)sum/count);
    return 0;
}
