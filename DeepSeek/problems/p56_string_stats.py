"""Problem 56: Count words, vowels, consonants in a string."""
text = input("Text: ")
words      = len(text.split())
vowels     = sum(1 for c in text.lower() if c in "aeiou")
consonants = sum(1 for c in text.lower() if c.isalpha() and c not in "aeiou")
print(f"Words={words}, Vowels={vowels}, Consonants={consonants}")
