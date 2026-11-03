#include <iostream>
using namespace std;

double largestOfThree(double a, double b, double c) {
    double largest = a;
    if (b > largest) largest = b;
    if (c > largest) largest = c;
    return largest;
}

int main() {
    double a, b, c;
    cout << "Enter three numbers: ";
    cin >> a >> b >> c;
    cout << "Largest = " << largestOfThree(a, b, c) << '\n';
    return 0;
}
