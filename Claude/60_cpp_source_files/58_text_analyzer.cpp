#include <iostream>
#include <sstream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string text;
    cout << "Enter a paragraph on one line: ";
    getline(cin, text);

    int vowels = 0, digits = 0, sentences = 0;
    for (unsigned char ch : text) {
        char c = static_cast<char>(tolower(ch));
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') ++vowels;
        if (isdigit(ch)) ++digits;
        if (ch == '.' || ch == '!' || ch == '?') ++sentences;
    }

    string word;
    int words = 0;
    stringstream input(text);
    while (input >> word) ++words;

    cout << "Characters (including spaces) = " << text.size() << '\n';
    cout << "Words = " << words << '\n';
    cout << "Sentence-ending punctuation marks = " << sentences << '\n';
    cout << "Vowels = " << vowels << '\n';
    cout << "Digits = " << digits << '\n';
    return 0;
}
