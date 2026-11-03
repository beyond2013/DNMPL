#include <iostream>
using namespace std;

int main() {
    double a, b, c;
    cout << "Enter three numbers: ";
    cin >> a >> b >> c;
    if (a >= b && a >= c) cout << "Largest = " << a << '\n';
    else if (b >= a && b >= c) cout << "Largest = " << b << '\n';
    else cout << "Largest = " << c << '\n';
    return 0;
}
