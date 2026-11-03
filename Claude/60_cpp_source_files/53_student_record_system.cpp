#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

struct Student {
    string name;
    double marks;
};

int main() {
    vector<Student> students;
    int choice;
    do {
        cout << "\n1. Add student  2. Display records  3. Highest mark  0. Exit\nChoice: ";
        cin >> choice;
        if (choice == 1) {
            Student s;
            cout << "Enter student name: ";
            getline(cin >> ws, s.name);
            cout << "Enter percentage (0-100): ";
            cin >> s.marks;
            if (s.marks < 0 || s.marks > 100) cout << "Invalid percentage.\n";
            else students.push_back(s);
        } else if (choice == 2) {
            if (students.empty()) cout << "No records available.\n";
            for (const Student &s : students)
                cout << s.name << " - " << s.marks << "%\n";
        } else if (choice == 3) {
            if (students.empty()) cout << "No records available.\n";
            else {
                Student best = students[0];
                for (const Student &s : students)
                    if (s.marks > best.marks) best = s;
                cout << "Highest scorer: " << best.name << " (" << best.marks << "%)\n";
            }
        } else if (choice != 0) cout << "Invalid choice.\n";
    } while (choice != 0);
    return 0;
}
