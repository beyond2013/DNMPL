#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter an integer: ";
    cin >> n;
    bool by3 = (n % 3 == 0);
    bool by5 = (n % 5 == 0);

    if (by3 && by5) cout << "Divisible by both 3 and 5\n";
    else if (by3) cout << "Divisible by 3 only\n";
    else if (by5) cout << "Divisible by 5 only\n";
    else cout << "Divisible by neither 3 nor 5\n";
    return 0;
}
