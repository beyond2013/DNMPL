#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int main() {
    int n;
    cout << "Number of values: ";
    cin >> n;
    if (n < 2) {
        cout << "At least two values are needed.\n";
        return 0;
    }
    int largest = INT_MIN, second = INT_MIN, value;
    bool hasLargest = false, hasSecond = false;
    for (int i = 0; i < n; ++i) {
        cin >> value;
        if (!hasLargest || value > largest) {
            if (hasLargest) {
                second = largest;
                hasSecond = true;
            }
            largest = value;
            hasLargest = true;
        } else if (value < largest && (!hasSecond || value > second)) {
            second = value;
            hasSecond = true;
        }
    }
    if (hasSecond) cout << "Second-largest distinct value = " << second << '\n';
    else cout << "No second-largest distinct value exists.\n";
    return 0;
}
