#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double units;
    const double FIXED_CHARGE = 150.0;
    cout << "Enter units consumed: ";
    cin >> units;
    if (units < 0) {
        cout << "Units cannot be negative.\n";
        return 0;
    }

    // Illustrative progressive slabs: first 100 at Rs. 10,
    // next 100 at Rs. 15, remaining units at Rs. 20.
    double bill = FIXED_CHARGE;
    if (units <= 100) bill += units * 10;
    else if (units <= 200) bill += 100 * 10 + (units - 100) * 15;
    else bill += 100 * 10 + 100 * 15 + (units - 200) * 20;

    cout << fixed << setprecision(2);
    cout << "Estimated bill = Rs. " << bill << '\n';
    return 0;
}
