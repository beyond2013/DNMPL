#include <iostream>
using namespace std;

int main() {
    long long totalSeconds;
    cout << "Enter total seconds: ";
    cin >> totalSeconds;
    if (totalSeconds < 0) {
        cout << "Please enter a nonnegative number of seconds.\n";
        return 0;
    }
    long long hours = totalSeconds / 3600;
    long long minutes = (totalSeconds % 3600) / 60;
    long long seconds = totalSeconds % 60;
    cout << hours << " hour(s), " << minutes << " minute(s), "
         << seconds << " second(s)\n";
    return 0;
}
