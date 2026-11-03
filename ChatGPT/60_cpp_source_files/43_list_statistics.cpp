#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cout << "How many numbers? ";
    cin >> n;
    if (n <= 0) {
        cout << "Enter at least one number.\n";
        return 0;
    }
    vector<double> values(n);
    for (int i = 0; i < n; ++i) {
        cout << "Value " << i + 1 << ": ";
        cin >> values[i];
    }
    double sum = 0, minimum = values[0], maximum = values[0];
    for (double x : values) {
        sum += x;
        if (x < minimum) minimum = x;
        if (x > maximum) maximum = x;
    }
    cout << "Sum = " << sum << "\nCount = " << n
         << "\nAverage = " << sum / n << "\nMinimum = " << minimum
         << "\nMaximum = " << maximum << '\n';
    return 0;
}
