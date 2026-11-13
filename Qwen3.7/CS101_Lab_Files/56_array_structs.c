#include <stdio.h>
struct Student { char name[20]; int marks; };
int main() {
    struct Student cls[2] = {{"Ali", 80}, {"Sara", 90}};
    for(int i=0; i<2; i++) printf("%s: %d\n", cls[i].name, cls[i].marks);
    return 0;
}
