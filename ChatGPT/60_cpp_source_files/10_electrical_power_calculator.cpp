#include <iostream>
using namespace std;

int main() {
    double voltage, current;
    cout << "Enter voltage (V) and current (A): ";
    cin >> voltage >> current;
    cout << "Power = " << voltage * current << " watts\n";
    if (current != 0)
        cout << "Resistance = " << voltage / current << " ohms\n";
    else
        cout << "Resistance V/I is undefined when current is zero.\n";
    return 0;
}
