#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double price1, price2, price3, discountPercent;
    int quantity1, quantity2, quantity3;

    cout << "Enter price and quantity for product 1: ";
    cin >> price1 >> quantity1;
    cout << "Enter price and quantity for product 2: ";
    cin >> price2 >> quantity2;
    cout << "Enter price and quantity for product 3: ";
    cin >> price3 >> quantity3;
    cout << "Enter discount percentage: ";
    cin >> discountPercent;

    double subtotal = price1 * quantity1 + price2 * quantity2 + price3 * quantity3;
    double discount = subtotal * discountPercent / 100.0;
    cout << fixed << setprecision(2);
    cout << "Subtotal = Rs. " << subtotal << '\n';
    cout << "Discount = Rs. " << discount << '\n';
    cout << "Final bill = Rs. " << subtotal - discount << '\n';
    return 0;
}
