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
    long long reversed = 0;
    do {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    } while (n > 0);
    cout << "Reversed number = " << reversed << '\n';
    return 0;
}
