"""Problem 60: Password validator."""
import string

def validate(pw):
    rules = [
        (len(pw) >= 8,                              "at least 8 characters"),
        (any(c.isupper() for c in pw),              "an uppercase letter"),
        (any(c.islower() for c in pw),              "a lowercase letter"),
        (any(c.isdigit() for c in pw),              "a digit"),
        (any(c in string.punctuation for c in pw),  "a special character"),
    ]
    errors = [msg for ok, msg in rules if not ok]
    return errors if errors else None

if __name__ == "__main__":
    pw = input("Password: ")
    err = validate(pw)
    print("Valid password!" if err is None else "Missing: " + ", ".join(err))
