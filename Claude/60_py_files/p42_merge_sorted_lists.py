"""Problem 42: Merge two sorted lists"""


def p42():
    a, b = [1, 4, 9, 15], [2, 3, 10, 20, 25]
    merged, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    print(merged)


if __name__ == "__main__":
    p42()
