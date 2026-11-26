"""Problem 39: Remove duplicates (keep first occurrence)"""


def p39():
    data = [4, 2, 4, 7, 2, 9, 7]
    unique = []
    for x in data:
        if x not in unique:
            unique.append(x)
    print(data, "->", unique)


if __name__ == "__main__":
    p39()
