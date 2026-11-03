#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double km;
    cout << "Enter distance in kilometres: ";
    cin >> km;
    cout << fixed << setprecision(3);
    cout << "Metres = " << km * 1000 << '\n';
    cout << "Centimetres = " << km * 100000 << '\n';
    cout << "Miles = " << km * 0.621371 << '\n';
    return 0;
}
