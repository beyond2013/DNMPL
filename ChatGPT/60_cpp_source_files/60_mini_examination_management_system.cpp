#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

struct Student {
    string name;
    vector<double> marks;
    double total = 0;
    double percentage = 0;
    char grade = 'F';
    bool passed = false;
};

char gradeFor(double p) {
    if (p >= 80) return 'A';
    if (p >= 70) return 'B';
    if (p >= 60) return 'C';
    if (p >= 50) return 'D';
    return 'F';
}

int main() {
    int n, subjects;
    cout << "Number of students: ";
    cin >> n;
    cout << "Number of subjects: ";
    cin >> subjects;
    if (n <= 0 || subjects <= 0) {
        cout << "Both counts must be positive.\n";
        return 0;
    }

    vector<Student> students(n);
    for (int i = 0; i < n; ++i) {
        cout << "\nStudent " << i + 1 << " name: ";
        getline(cin >> ws, students[i].name);
        students[i].marks.resize(subjects);
        for (int j = 0; j < subjects; ++j) {
            cout << "Subject " << j + 1 << " marks (0-100): ";
            cin >> students[i].marks[j];
            if (students[i].marks[j] < 0 || students[i].marks[j] > 100) {
                cout << "Invalid marks.\n";
                return 0;
            }
            students[i].total += students[i].marks[j];
        }
        students[i].percentage = students[i].total / subjects;
        students[i].grade = gradeFor(students[i].percentage);
        students[i].passed = students[i].percentage >= 50;
    }

    sort(students.begin(), students.end(),
         [](const Student &a, const Student &b) { return a.total > b.total; });

    cout << "\nRanked class results:\n";
    cout << fixed << setprecision(2);
    for (int i = 0; i < n; ++i) {
        cout << i + 1 << ". " << students[i].name
             << " | Total: " << students[i].total << "/" << subjects * 100
             << " | Percentage: " << students[i].percentage << "%"
             << " | Grade: " << students[i].grade
             << " | " << (students[i].passed ? "Pass" : "Fail") << '\n';
    }
    return 0;
}
