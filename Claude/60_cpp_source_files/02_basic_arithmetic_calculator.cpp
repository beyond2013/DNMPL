#include <iostream>
using namespace std;

int main() {
    double a, b;
    cout << "Enter two numbers: ";
    cin >> a >> b;

    cout << "Sum = " << a + b << '\n';
    cout << "Difference = " << a - b << '\n';
    cout << "Product = " << a * b << '\n';
    if (b != 0)
        cout << "Quotient = " << a / b << '\n';
    else
        cout << "Quotient is undefined because the second number is zero.\n";
    return 0;
}
