#include <iostream>
#include <random>
using namespace std;

int main() {
    random_device rd;
    mt19937 generator(rd());
    uniform_int_distribution<int> distribution(1, 100);
    int secret = distribution(generator), guess, attempts = 0;

    cout << "Guess the secret number from 1 to 100.\n";
    do {
        cout << "Your guess: ";
        cin >> guess;
        ++attempts;
        if (guess < secret) cout << "Too low.\n";
        else if (guess > secret) cout << "Too high.\n";
        else cout << "Correct! Attempts: " << attempts << '\n';
    } while (guess != secret);
    return 0;
}
