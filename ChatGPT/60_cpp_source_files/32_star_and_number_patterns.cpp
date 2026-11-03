#include <iostream>
using namespace std;

int main() {
    int rows;
    cout << "Enter number of rows: ";
    cin >> rows;
    if (rows < 1 || rows > 50) {
        cout << "Enter a value from 1 to 50.\n";
        return 0;
    }

    cout << "Star pattern:\n";
    for (int i = 1; i <= rows; ++i) {
        for (int j = 1; j <= i; ++j) cout << "* ";
        cout << '\n';
    }

    cout << "Number pattern:\n";
    for (int i = 1; i <= rows; ++i) {
        for (int j = 1; j <= i; ++j) cout << j << ' ';
        cout << '\n';
    }
    return 0;
}
