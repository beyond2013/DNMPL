#include <iostream>
using namespace std;

int main() {
    double percentage, testScore;
    cout << "Enter previous-exam percentage and entry-test score (%): ";
    cin >> percentage >> testScore;
    // Illustrative thresholds; replace with the actual admission policy.
    if (percentage < 0 || percentage > 100 || testScore < 0 || testScore > 100) {
        cout << "Invalid score(s)\n";
    } else if (percentage >= 50 && testScore >= 50) {
        cout << "Meets the illustrative eligibility criteria\n";
    } else {
        cout << "Does not meet the illustrative eligibility criteria\n";
    }
    return 0;
}
