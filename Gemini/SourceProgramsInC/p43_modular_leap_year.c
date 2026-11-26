#include <stdio.h>
int isLeap(int y) {
    return (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0);
}
int main() {
    printf(isLeap(2024) ? "Leap\n" : "Not Leap\n");
    return 0;
}