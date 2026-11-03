#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cout << "Number of values: ";
    cin >> n;
    if (n < 0) return 0;
    vector<int> values(n), reversed;
    for (int i = 0; i < n; ++i) cin >> values[i];
    for (int i = n - 1; i >= 0; --i) reversed.push_back(values[i]);

    cout << "Reversed list: ";
    for (int value : reversed) cout << value << ' ';
    cout << '\n';
    return 0;
}
