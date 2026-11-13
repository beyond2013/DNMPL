#include <stdio.h>
int main() {
    char op; int a, b;
    printf("Enter operator (+,-,*,/): "); scanf(" %c", &op);
    printf("Enter two numbers: "); scanf("%d %d", &a, &b);
    switch(op) {
        case '+': printf("%d\n", a+b); break;
        case '-': printf("%d\n", a-b); break;
        case '*': printf("%d\n", a*b); break;
        case '/': printf("%d\n", a/b); break;
        default: printf("Invalid\n");
    }
    return 0;
}
