#include <iostream>
using namespace std;

int main() {
    double balance, amount;
    cout << "Enter account balance and withdrawal amount: ";
    cin >> balance >> amount;

    if (balance < 0 || amount <= 0) cout << "Invalid balance or amount\n";
    else if (amount > balance) cout << "Insufficient balance\n";
    else if (static_cast<long long>(amount) % 500 != 0 || amount != static_cast<long long>(amount))
        cout << "Amount must be a whole-number multiple of Rs. 500\n";
    else {
        balance -= amount;
        cout << "Withdrawal successful. Remaining balance = Rs. " << balance << '\n';
    }
    return 0;
}
