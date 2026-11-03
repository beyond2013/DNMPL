#include <iostream>
using namespace std;

int main() {
    int year;
    cout << "Enter a year: ";
    cin >> year;
    if (year <= 0) {
        cout << "Enter a positive year.\n";
    } else if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0)) {
        cout << "Leap year\n";
    } else {
        cout << "Not a leap year\n";
    }
    return 0;
}
