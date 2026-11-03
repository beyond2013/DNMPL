#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

struct Expense {
    string category;
    string description;
    double amount;
};

int main() {
    vector<Expense> expenses;
    int n;
    cout << "How many expenses will you enter? ";
    cin >> n;
    if (n < 0) return 0;

    for (int i = 0; i < n; ++i) {
        Expense e;
        cout << "Category (food/transport/books/utilities/other): ";
        cin >> e.category;
        cout << "Short description: ";
        getline(cin >> ws, e.description);
        cout << "Amount (Rs.): ";
        cin >> e.amount;
        if (e.amount < 0) {
            cout << "Amount cannot be negative.\n";
            return 0;
        }
        expenses.push_back(e);
    }

    double total = 0, largest = -1;
    int largestIndex = -1;
    for (int i = 0; i < static_cast<int>(expenses.size()); ++i) {
        total += expenses[i].amount;
        if (expenses[i].amount > largest) {
            largest = expenses[i].amount;
            largestIndex = i;
        }
    }

    cout << fixed << setprecision(2);
    cout << "\nTotal expenditure = Rs. " << total << '\n';
    cout << "Category totals:\n";
    vector<string> categories = {"food", "transport", "books", "utilities", "other"};
    for (const string &category : categories) {
        double subtotal = 0;
        for (const Expense &e : expenses)
            if (e.category == category) subtotal += e.amount;
        cout << category << ": Rs. " << subtotal << '\n';
    }
    if (largestIndex >= 0)
        cout << "Largest expense: " << expenses[largestIndex].description
             << " (Rs. " << largest << ")\n";
    return 0;
}
