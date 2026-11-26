"""Problem 44: Reverse a string and check palindrome"""


def p44():
    for s in ("Level", "Python"):
        rev = ""
        for ch in s:
            rev = ch + rev
        verdict = "is" if rev.lower() == s.lower() else "is not"
        print(f"{s} reversed = {rev}; {verdict} a palindrome")


if __name__ == "__main__":
    p44()
