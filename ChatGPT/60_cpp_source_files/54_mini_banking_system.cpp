#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double balance;
    cout << "Enter opening balance: ";
    cin >> balance;
    if (balance < 0) {
        cout << "Balance cannot be negative.\n";
        return 0;
    }

    int choice;
    do {
        cout << "\n1. Deposit  2. Withdraw  3. Check balance  0. Exit\nChoice: ";
        cin >> choice;
        if (choice == 1) {
            double amount;
            cout << "Deposit amount: ";
            cin >> amount;
            if (amount <= 0) cout << "Amount must be positive.\n";
            else balance += amount;
        } else if (choice == 2) {
            double amount;
            cout << "Withdrawal amount: ";
            cin >> amount;
            if (amount <= 0) cout << "Amount must be positive.\n";
            else if (amount > balance) cout << "Insufficient funds.\n";
            else balance -= amount;
        } else if (choice == 3) {
            cout << fixed << setprecision(2) << "Balance = Rs. " << balance << '\n';
        } else if (choice != 0) cout << "Invalid choice.\n";
    } while (choice != 0);

    cout << "Final balance = Rs. " << fixed << setprecision(2) << balance << '\n';
    return 0;
}
