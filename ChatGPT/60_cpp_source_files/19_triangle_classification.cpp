#include <iostream>
using namespace std;

int main() {
    double a, b, c;
    cout << "Enter three side lengths: ";
    cin >> a >> b >> c;
    if (a <= 0 || b <= 0 || c <= 0 ||
        a + b <= c || a + c <= b || b + c <= a) {
        cout << "These sides do not form a triangle.\n";
    } else if (a == b && b == c) {
        cout << "Equilateral triangle\n";
    } else if (a == b || a == c || b == c) {
        cout << "Isosceles triangle\n";
    } else {
        cout << "Scalene triangle\n";
    }
    return 0;
}
