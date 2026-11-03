#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, passCount = 0;
    cout << "Number of students: ";
    cin >> n;
    if (n <= 0) {
        cout << "Enter at least one student.\n";
        return 0;
    }
    vector<double> marks(n);
    double total = 0, highest = -1, lowest = 101;
    for (int i = 0; i < n; ++i) {
        cout << "Marks for student " << i + 1 << " (0-100): ";
        cin >> marks[i];
        if (marks[i] < 0 || marks[i] > 100) {
            cout << "Invalid marks.\n";
            return 0;
        }
        total += marks[i];
        if (marks[i] > highest) highest = marks[i];
        if (marks[i] < lowest) lowest = marks[i];
        if (marks[i] >= 50) ++passCount;
    }
    cout << "Class average = " << total / n << '\n';
    cout << "Highest = " << highest << "\nLowest = " << lowest
         << "\nStudents passed (50 or above) = " << passCount << '\n';
    return 0;
}
