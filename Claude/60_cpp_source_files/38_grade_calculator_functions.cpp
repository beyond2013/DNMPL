#include <iostream>
using namespace std;

double percentage(double obtained, double maximum) {
    return obtained / maximum * 100.0;
}

char gradeFor(double p) {
    if (p >= 80) return 'A';
    if (p >= 70) return 'B';
    if (p >= 60) return 'C';
    if (p >= 50) return 'D';
    return 'F';
}

int main() {
    double obtained, maximum;
    cout << "Enter obtained and maximum marks: ";
    cin >> obtained >> maximum;
    if (maximum <= 0 || obtained < 0 || obtained > maximum) {
        cout << "Invalid marks.\n";
        return 0;
    }
    double p = percentage(obtained, maximum);
    cout << "Percentage = " << p << "%\n";
    cout << "Grade = " << gradeFor(p) << '\n';
    return 0;
}
