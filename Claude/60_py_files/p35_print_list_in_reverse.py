"""Problem 35: Print N numbers in reverse"""


def p35():
    data = [4, 8, 15, 16, 23, 42]
    for i in range(len(data) - 1, -1, -1):
        print(data[i], end=" ")
    print()


if __name__ == "__main__":
    p35()
