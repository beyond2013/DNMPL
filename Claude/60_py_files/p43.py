"""Problem 43: Count vowels, consonants, digits, spaces"""


def p43():
    text = "Programming in Python 3 is fun!"
    vowels = consonants = digits = spaces = 0
    for ch in text.lower():
        if ch in "aeiou":
            vowels += 1
        elif ch.isalpha():
            consonants += 1
        elif ch.isdigit():
            digits += 1
        elif ch == " ":
            spaces += 1
    print(f"Vowels={vowels}, Consonants={consonants}, Digits={digits}, Spaces={spaces}")


if __name__ == "__main__":
    p43()
