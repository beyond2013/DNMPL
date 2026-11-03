#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    const int DAYS = 30;
    vector<double> units(DAYS);
    double total = 0, highest = -1;
    int highestDay = 0;

    cout << "Enter electricity consumption for 30 days (kWh):\n";
    for (int i = 0; i < DAYS; ++i) {
        cout << "Day " << i + 1 << ": ";
        cin >> units[i];
        if (units[i] < 0) {
            cout << "Consumption cannot be negative.\n";
            return 0;
        }
        total += units[i];
        if (units[i] > highest) {
            highest = units[i];
            highestDay = i + 1;
        }
    }

    // Illustrative flat tariff; change to match the required tariff.
    const double RATE = 20.0;
    cout << fixed << setprecision(2);
    cout << "Total consumption = " << total << " kWh\n";
    cout << "Daily average = " << total / DAYS << " kWh\n";
    cout << "Highest consumption = " << highest << " kWh on day " << highestDay << '\n';
    cout << "Estimated bill at Rs. " << RATE << " per kWh = Rs. " << total * RATE << '\n';
    return 0;
}
