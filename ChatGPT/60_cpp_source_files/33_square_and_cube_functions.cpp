#include <iostream>
using namespace std;

double square(double n) { return n * n; }
double cube(double n) { return n * n * n; }

int main() {
    double number;
    cout << "Enter a number: ";
    cin >> number;
    cout << "Square = " << square(number) << '\n';
    cout << "Cube = " << cube(number) << '\n';
    return 0;
}
