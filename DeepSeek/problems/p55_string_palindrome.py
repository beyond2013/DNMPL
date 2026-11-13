"""Problem 55: Reverse a string and check palindrome."""
s = input("String: ")
print(f"Reversed: {s[::-1]}")
print("Palindrome" if s == s[::-1] else "Not palindrome")
