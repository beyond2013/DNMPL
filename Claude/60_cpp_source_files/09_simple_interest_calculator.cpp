#include <iostream>
using namespace std;

int main() {
    double principal, rate, years;
    cout << "Enter principal, annual rate (%) and time (years): ";
    cin >> principal >> rate >> years;
    double interest = principal * rate * years / 100.0;
    cout << "Simple interest = " << interest << '\n';
    cout << "Total amount = " << principal + interest << '\n';
    return 0;
}
