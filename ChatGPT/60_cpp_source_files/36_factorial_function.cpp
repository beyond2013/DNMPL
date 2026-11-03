#include <iostream>
using namespace std;

unsigned long long factorial(int n) {
    unsigned long long result = 1;
    for (int i = 2; i <= n; ++i) result *= i;
    return result;
}

int main() {
    int n;
    cout << "Enter an integer from 0 to 20: ";
    cin >> n;
    if (n < 0 || n > 20) cout << "Invalid input.\n";
    else cout << n << "! = " << factorial(n) << '\n';
    return 0;
}
