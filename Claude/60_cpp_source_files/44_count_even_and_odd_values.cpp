#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, evenCount = 0, oddCount = 0, value;
    cout << "How many integers? ";
    cin >> n;
    if (n < 0) {
        cout << "Count cannot be negative.\n";
        return 0;
    }
    for (int i = 0; i < n; ++i) {
        cin >> value;
        if (value % 2 == 0) ++evenCount;
        else ++oddCount;
    }
    cout << "Even values = " << evenCount << "\nOdd values = " << oddCount << '\n';
    return 0;
}
