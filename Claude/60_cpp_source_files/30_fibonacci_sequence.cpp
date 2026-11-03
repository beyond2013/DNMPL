#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "How many Fibonacci terms? ";
    cin >> n;
    if (n < 1 || n > 90) {
        cout << "Enter a number from 1 to 90.\n";
        return 0;
    }
    unsigned long long a = 0, b = 1;
    for (int i = 0; i < n; ++i) {
        cout << a << ' ';
        unsigned long long next = a + b;
        a = b;
        b = next;
    }
    cout << '\n';
    return 0;
}
