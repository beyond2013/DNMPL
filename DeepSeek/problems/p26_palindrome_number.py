"""Problem 26: Palindrome number check."""
n = int(input("Number: "))
s = str(n)
print("Palindrome" if s == s[::-1] else "Not palindrome")
