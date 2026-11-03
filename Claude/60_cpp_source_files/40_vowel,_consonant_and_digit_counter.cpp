#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int countVowels(const string& text) {
    int count = 0;
    for (unsigned char ch : text) {
        char c = static_cast<char>(tolower(ch));
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') ++count;
    }
    return count;
}

int countConsonants(const string& text) {
    int count = 0;
    for (unsigned char ch : text)
        if (isalpha(ch) && string("aeiouAEIOU").find(static_cast<char>(ch)) == string::npos)
            ++count;
    return count;
}

int countDigits(const string& text) {
    int count = 0;
    for (unsigned char ch : text) if (isdigit(ch)) ++count;
    return count;
}

int main() {
    string text;
    cout << "Enter a line of text: ";
    getline(cin, text);
    cout << "Vowels = " << countVowels(text) << '\n';
    cout << "Consonants = " << countConsonants(text) << '\n';
    cout << "Digits = " << countDigits(text) << '\n';
    return 0;
}
