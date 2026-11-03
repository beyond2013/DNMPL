#include <iostream>
#include <string>
using namespace std;

int main() {
    string name, department, semester, city;
    cout << "Enter your name: ";
    getline(cin, name);
    cout << "Enter your department: ";
    getline(cin, department);
    cout << "Enter your semester: ";
    getline(cin, semester);
    cout << "Enter your city: ";
    getline(cin, city);

    cout << "\n--- Student Introduction ---\n";
    cout << "Name: " << name << "\nDepartment: " << department
         << "\nSemester: " << semester << "\nCity: " << city << '\n';
    return 0;
}
