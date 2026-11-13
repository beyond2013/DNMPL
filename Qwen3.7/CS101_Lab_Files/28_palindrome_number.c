#include <stdio.h>
int main() {
    int n, temp, rev=0, rem;
    printf("Enter N: "); scanf("%d", &n); temp=n;
    while(n!=0) { rem=n%10; rev=rev*10+rem; n/=10; }
    printf(temp==rev ? "Palindrome\n" : "Not Palindrome\n");
    return 0;
}
