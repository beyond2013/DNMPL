#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, target;
    cout << "Number of values: ";
    cin >> n;
    if (n < 0) return 0;
    vector<int> values(n);
    for (int i = 0; i < n; ++i) cin >> values[i];
    cout << "Value to search for: ";
    cin >> target;

    int foundIndex = -1;
    for (int i = 0; i < n; ++i) {
        if (values[i] == target) {
            foundIndex = i;
            break;
        }
    }
    if (foundIndex == -1) cout << "Value not found.\n";
    else cout << "Value found at zero-based index " << foundIndex << '\n';
    return 0;
}
