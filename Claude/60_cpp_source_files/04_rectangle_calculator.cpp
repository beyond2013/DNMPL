#include <iostream>
using namespace std;

int main() {
    double length, width;
    cout << "Enter length and width: ";
    cin >> length >> width;
    cout << "Area = " << length * width << '\n';
    cout << "Perimeter = " << 2 * (length + width) << '\n';
    return 0;
}
