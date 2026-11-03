#include <iostream>
using namespace std;

double totalMarks(double marks[], int size) {
    double total = 0;
    for (int i = 0; i < size; ++i) total += marks[i];
    return total;
}

double percentage(double total, double maximum) {
    return total / maximum * 100.0;
}

char gradeFor(double p) {
    if (p >= 80) return 'A';
    if (p >= 70) return 'B';
    if (p >= 60) return 'C';
    if (p >= 50) return 'D';
    return 'F';
}

int main() {
    const int SUBJECTS = 5;
    double marks[SUBJECTS];
    cout << "Enter marks in five subjects (each out of 100):\n";
    for (int i = 0; i < SUBJECTS; ++i) {
        cin >> marks[i];
        if (marks[i] < 0 || marks[i] > 100) {
            cout << "Invalid mark entered.\n";
            return 0;
        }
    }
    double total = totalMarks(marks, SUBJECTS);
    double p = percentage(total, SUBJECTS * 100.0);
    cout << "Total = " << total << '\n';
    cout << "Percentage = " << p << "%\n";
    cout << "Grade = " << gradeFor(p) << '\n';
    cout << "Result = " << (p >= 50 ? "Pass\n" : "Fail\n");
    return 0;
}
