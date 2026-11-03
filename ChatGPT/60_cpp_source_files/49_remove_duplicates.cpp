#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cout << "Number of values: ";
    cin >> n;
    if (n < 0) return 0;
    vector<int> values(n), uniqueValues;
    for (int i = 0; i < n; ++i) cin >> values[i];

    for (int value : values) {
        bool alreadyPresent = false;
        for (int existing : uniqueValues)
            if (existing == value) alreadyPresent = true;
        if (!alreadyPresent) uniqueValues.push_back(value);
    }

    cout << "List without duplicates: ";
    for (int value : uniqueValues) cout << value << ' ';
    cout << '\n';
    return 0;
}
