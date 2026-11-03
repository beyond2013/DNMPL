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
    int count = 0;
    do {
        ++count;
        n /= 10;
    } while (n > 0);
    cout << "Number of digits = " << count << '\n';
    return 0;
}
