#include <iostream>
using namespace std;

bool isPrime(int n) {
    if (n < 2) return false;
    for (int d = 2; d <= n / d; ++d)
        if (n % d == 0) return false;
    return true;
}

int main() {
    int start, end;
    cout << "Enter start and end of range: ";
    cin >> start >> end;
    if (start > end) {
        cout << "Start must not exceed end.\n";
        return 0;
    }
    for (int n = start; n <= end; ++n)
        if (isPrime(n)) cout << n << ' ';
    cout << '\n';
    return 0;
}
