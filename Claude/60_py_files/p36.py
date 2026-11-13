"""Problem 36: Sum, average, max, min of a list"""


def p36():
    data = [12, 45, 7, 33, 21]
    total, largest, smallest = 0, data[0], data[0]
    for x in data:
        total += x
        largest = max(largest, x)
        smallest = min(smallest, x)
    print(f"Sum={total}, Average={total / len(data):.2f}, Max={largest}, Min={smallest}")


if __name__ == "__main__":
    p36()
