#include <stdio.h>
struct Student { char name[20]; int roll; };
void printStudent(struct Student s) { printf("Roll: %d, Name: %s\n", s.roll, s.name); }
int main() { struct Student s1 = {"Sara", 102}; printStudent(s1); return 0; }
