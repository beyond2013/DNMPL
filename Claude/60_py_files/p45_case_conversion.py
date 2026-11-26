"""Problem 45: Upper/lower case without library functions"""


def p45():
    def to_upper(s):
        out = ""
        for ch in s:
            out += chr(ord(ch) - 32) if "a" <= ch <= "z" else ch
        return out

    def to_lower(s):
        out = ""
        for ch in s:
            out += chr(ord(ch) + 32) if "A" <= ch <= "Z" else ch
        return out

    s = "Hello, World 123"
    print(to_upper(s), "|", to_lower(s))


if __name__ == "__main__":
    p45()
