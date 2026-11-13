"""Problem 48: Caesar cipher"""


def p48():
    def shift_text(text, key):
        out = ""
        for ch in text:
            if ch.isupper():
                out += chr((ord(ch) - ord("A") + key) % 26 + ord("A"))
            elif ch.islower():
                out += chr((ord(ch) - ord("a") + key) % 26 + ord("a"))
            else:
                out += ch
        return out

    message, key = "Hello, World!", 3
    cipher = shift_text(message, key)
    print("Encrypted:", cipher)
    print("Decrypted:", shift_text(cipher, -key))


if __name__ == "__main__":
    p48()
