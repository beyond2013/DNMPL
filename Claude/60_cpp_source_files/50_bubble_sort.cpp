#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cout << "Number of values: ";
    cin >> n;
    if (n < 0) return 0;
    vector<int> values(n);
    for (int i = 0; i < n; ++i) cin >> values[i];

    for (int i = 0; i < n - 1; ++i) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; ++j) {
            if (values[j] > values[j + 1]) {
                int temp = values[j];
                values[j] = values[j + 1];
                values[j + 1] = temp;
                swapped = true;
            }
        }
        if (!swapped) break;
    }

    cout << "Sorted values: ";
    for (int value : values) cout << value << ' ';
    cout << '\n';
    return 0;
}
