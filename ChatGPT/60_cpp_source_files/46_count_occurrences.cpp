#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, target, count = 0;
    cout << "Number of values: ";
    cin >> n;
    if (n < 0) return 0;
    vector<int> values(n);
    for (int i = 0; i < n; ++i) cin >> values[i];
    cout << "Target value: ";
    cin >> target;
    for (int value : values) if (value == target) ++count;
    cout << "Occurrences = " << count << '\n';
    return 0;
}
