#include <stdio.h>
int main() {
    int target = 42, guess;
    do {
        printf("Guess the number: "); scanf("%d", &guess);
        if (guess > target) printf("Too high!\n");
        else if (guess < target) printf("Too low!\n");
        else printf("Correct!\n");
    } while (guess != target);
    return 0;
}