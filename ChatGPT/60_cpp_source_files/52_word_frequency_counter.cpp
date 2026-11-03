#include <iostream>
#include <sstream>
#include <map>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string line, word;
    cout << "Enter a sentence: ";
    getline(cin, line);

    // Convert to lowercase and replace basic punctuation with spaces.
    for (char &ch : line) {
        unsigned char u = static_cast<unsigned char>(ch);
        if (ispunct(u)) ch = ' ';
        else ch = static_cast<char>(tolower(u));
    }

    map<string, int> frequency;
    stringstream input(line);
    while (input >> word) ++frequency[word];

    for (const auto &entry : frequency)
        cout << entry.first << ": " << entry.second << '\n';
    return 0;
}
