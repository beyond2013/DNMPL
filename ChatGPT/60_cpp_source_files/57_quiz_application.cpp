#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Question {
    string prompt;
    string options[4];
    char correct;
};

int main() {
    vector<Question> quiz = {
        {"Which operator gives the remainder?", {"A) /", "B) %", "C) *", "D) + "}, 'B'},
        {"Which type stores true or false?", {"A) int", "B) char", "C) bool", "D) string"}, 'C'},
        {"Which loop checks its condition before each iteration?", {"A) while", "B) do-while", "C) switch", "D) if"}, 'A'}
    };
    int score = 0;
    for (const Question &q : quiz) {
        cout << "\n" << q.prompt << '\n';
        for (const string &option : q.options) cout << option << '\n';
        char answer;
        cout << "Your answer (A-D): ";
        cin >> answer;
        if (toupper(static_cast<unsigned char>(answer)) == q.correct) {
            ++score;
            cout << "Correct!\n";
        } else {
            cout << "Incorrect. Correct answer: " << q.correct << '\n';
        }
    }
    double percentage = 100.0 * score / quiz.size();
    cout << "\nScore = " << score << "/" << quiz.size()
         << "\nPercentage = " << percentage << "%\n";
    return 0;
}
