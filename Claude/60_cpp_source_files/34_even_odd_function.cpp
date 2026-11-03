#include <iostream>
using namespace std;

bool isEven(int n) { return n % 2 == 0; }

int main() {
    int count, value;
    cout << "How many integers? ";
    cin >> count;
    for (int i = 1; i <= count; ++i) {
        cout << "Enter integer " << i << ": ";
        cin >> value;
        cout << value << (isEven(value) ? " is even.\n" : " is odd.\n");
    }
    return 0;
}
