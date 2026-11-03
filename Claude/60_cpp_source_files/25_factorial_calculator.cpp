#include <iostream>
using namespace std;

int main() {
    int n;
    unsigned long long factorial = 1;
    cout << "Enter a nonnegative integer (up to 20): ";
    cin >> n;
    if (n < 0 || n > 20) {
        cout << "Please enter a value from 0 to 20.\n";
        return 0;
    }
    for (int i = 2; i <= n; ++i) factorial *= i;
    cout << n << "! = " << factorial << '\n';
    return 0;
}
