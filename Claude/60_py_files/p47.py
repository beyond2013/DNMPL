"""Problem 47: Anagram check"""


def p47():
    def are_anagrams(a, b):
        a = a.replace(" ", "").lower()
        b = b.replace(" ", "").lower()
        if len(a) != len(b):
            return False
        counts = {}
        for ch in a:
            counts[ch] = counts.get(ch, 0) + 1
        for ch in b:
            if counts.get(ch, 0) == 0:
                return False
            counts[ch] -= 1
        return True

    for a, b in [("Listen", "Silent"), ("Hello", "World")]:
        print(f"{a} / {b} -> {are_anagrams(a, b)}")


if __name__ == "__main__":
    p47()
