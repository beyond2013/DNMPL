#include <iostream>
using namespace std;

int main() {
    int n;
    long long sum = 0;
    cout << "Enter N: ";
    cin >> n;
    for (int i = 2; i <= n; i += 2) sum += i;
    cout << "Sum of even numbers from 1 to " << n << " = " << sum << '\n';
    return 0;
}
