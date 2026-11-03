#include <iostream>
using namespace std;

int main() {
    long long n;
    cout << "Enter a nonnegative integer: ";
    cin >> n;
    if (n < 0) {
        cout << "Please enter a nonnegative integer.\n";
        return 0;
    }
    int sum = 0;
    do {
        sum += static_cast<int>(n % 10);
        n /= 10;
    } while (n > 0);
    cout << "Sum of digits = " << sum << '\n';
    return 0;
}
