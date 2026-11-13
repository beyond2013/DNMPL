#include <stdio.h>
struct Student { char name[20]; int roll; float marks; };
int main() {
    struct Student s1 = {"Ali", 101, 85.5};
    printf("Name: %s, Roll: %d, Marks: %.2f\n", s1.name, s1.roll, s1.marks);
    return 0;
}
