#include <iostream>
using namespace std;

double power(double voltage, double current) { return voltage * current; }
double resistance(double voltage, double current) { return voltage / current; }
double energyKWh(double powerWatts, double hours) { return powerWatts * hours / 1000.0; }

int main() {
    double voltage, current, hours;
    cout << "Enter voltage (V), current (A), and operating hours: ";
    cin >> voltage >> current >> hours;
    if (current == 0 || hours < 0) {
        cout << "Current must be nonzero and hours must be nonnegative.\n";
        return 0;
    }
    double p = power(voltage, current);
    cout << "Power = " << p << " W\n";
    cout << "Resistance = " << resistance(voltage, current) << " ohms\n";
    cout << "Energy = " << energyKWh(p, hours) << " kWh\n";
    return 0;
}
