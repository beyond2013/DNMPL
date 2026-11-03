#include <iostream>
using namespace std;

double add(double a, double b) { return a + b; }
double subtract(double a, double b) { return a - b; }
double multiply(double a, double b) { return a * b; }
double divide(double a, double b) { return a / b; }

int main() {
    int choice;
    double a, b;
    do {
        cout << "\n1. Add  2. Subtract  3. Multiply  4. Divide  0. Exit\nChoice: ";
        cin >> choice;
        if (choice >= 1 && choice <= 4) {
            cout << "Enter two numbers: ";
            cin >> a >> b;
            switch (choice) {
                case 1: cout << add(a, b) << '\n'; break;
                case 2: cout << subtract(a, b) << '\n'; break;
                case 3: cout << multiply(a, b) << '\n'; break;
                case 4:
                    if (b == 0) cout << "Cannot divide by zero.\n";
                    else cout << divide(a, b) << '\n';
                    break;
            }
        } else if (choice != 0) {
            cout << "Invalid choice.\n";
        }
    } while (choice != 0);
    return 0;
}
