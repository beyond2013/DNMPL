#include <iostream>
using namespace std;

int main() {
    double marks, total = 0;
    const int SUBJECTS = 5;
    cout << "Enter marks for " << SUBJECTS << " subjects (each out of 100):\n";
    for (int i = 1; i <= SUBJECTS; ++i) {
        cout << "Subject " << i << ": ";
        cin >> marks;
        total += marks;
    }
    cout << "Total = " << total << " / " << SUBJECTS * 100 << '\n';
    cout << "Percentage = " << total / (SUBJECTS * 100.0) * 100 << "%\n";
    cout << "Average marks = " << total / SUBJECTS << '\n';
    return 0;
}
