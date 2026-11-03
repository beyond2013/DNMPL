#include <iostream>
using namespace std;

int main() {
    double marks;
    cout << "Enter marks (0 to 100): ";
    cin >> marks;
    if (marks < 0 || marks > 100) cout << "Invalid marks\n";
    else if (marks >= 80) cout << "Grade: A\n";
    else if (marks >= 70) cout << "Grade: B\n";
    else if (marks >= 60) cout << "Grade: C\n";
    else if (marks >= 50) cout << "Grade: D\n";
    else cout << "Grade: F\n";
    return 0;
}
