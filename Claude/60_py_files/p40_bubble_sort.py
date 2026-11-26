"""Problem 40: Bubble sort"""


def p40():
    data = [64, 34, 25, 12, 22, 11, 90]
    n = len(data)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:          # already sorted: stop early
            break
    print("Sorted:", data)


if __name__ == "__main__":
    p40()
