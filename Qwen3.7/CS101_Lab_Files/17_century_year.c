#include <stdio.h>
int main() {
    int y;
    printf("Enter year: "); scanf("%d", &y);
    if(y % 100 == 0) printf("Century Year\n");
    else printf("Not a Century Year\n");
    return 0;
}
