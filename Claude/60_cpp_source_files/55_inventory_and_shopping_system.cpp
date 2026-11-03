#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

struct Product {
    string name;
    double price;
    int quantity;
};

int main() {
    vector<Product> products = {
        {"Notebook", 120.0, 20},
        {"Pen", 40.0, 50},
        {"USB Drive", 900.0, 10}
    };
    double bill = 0;
    int choice, quantity;

    do {
        cout << "\nAvailable products:\n";
        for (int i = 0; i < static_cast<int>(products.size()); ++i)
            cout << i + 1 << ". " << products[i].name << " - Rs. "
                 << products[i].price << " (stock: " << products[i].quantity << ")\n";
        cout << "0. Checkout\nSelect product: ";
        cin >> choice;

        if (choice == 0) break;
        if (choice < 1 || choice > static_cast<int>(products.size())) {
            cout << "Invalid selection.\n";
            continue;
        }
        cout << "Quantity: ";
        cin >> quantity;
        Product &p = products[choice - 1];
        if (quantity <= 0) cout << "Quantity must be positive.\n";
        else if (quantity > p.quantity) cout << "Insufficient stock.\n";
        else {
            bill += p.price * quantity;
            p.quantity -= quantity;
            cout << "Added to bill.\n";
        }
    } while (true);

    cout << fixed << setprecision(2) << "Final bill = Rs. " << bill << '\n';
    return 0;
}
