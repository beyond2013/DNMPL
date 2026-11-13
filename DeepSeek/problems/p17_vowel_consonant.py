"""Problem 17: Vowel or consonant."""
ch = input("Character: ").lower()
if not ch.isalpha(): print("Not a letter")
elif ch in "aeiou":  print("Vowel")
else:                print("Consonant")
