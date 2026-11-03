#include <iostream>
using namespace std;

int main() {
    int n;
    long long sum = 0;
    cout << "Enter a positive integer N: ";
    cin >> n;
    if (n < 1) {
        cout << "N must be positive.\n";
        return 0;
    }
    for (int i = 1; i <= n; ++i) sum += i;
    cout << "Sum using loop = " << sum << '\n';
    cout << "Sum using formula = " << 1LL * n * (n + 1) / 2 << '\n';
    return 0;
}
