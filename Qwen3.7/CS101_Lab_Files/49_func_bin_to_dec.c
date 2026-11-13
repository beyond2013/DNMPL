#include <stdio.h>
#include <math.h>
int binToDec(long long bin) {
    int dec=0, i=0, rem;
    while(bin){ rem=bin%10; dec+=rem*pow(2,i); bin/=10; i++; }
    return dec;
}
int main() { printf("Dec: %d\n", binToDec(1101)); return 0; }
