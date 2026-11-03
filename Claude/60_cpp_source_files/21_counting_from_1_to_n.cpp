#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter a positive integer N: ";
    cin >> n;
    if (n < 1) {
        cout << "N must be positive.\n";
        return 0;
    }
    for (int i = 1; i <= n; ++i) cout << i << ' ';
    cout << '\n';
    return 0;
}
