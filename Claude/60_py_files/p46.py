"""Problem 46: Count words in a sentence"""


def p46():
    sentence = "  Python   is   easy   to   learn  "
    count, in_word = 0, False
    for ch in sentence:
        if ch != " " and not in_word:
            count += 1
            in_word = True
        elif ch == " ":
            in_word = False
    print(f"Words = {count}")


if __name__ == "__main__":
    p46()
