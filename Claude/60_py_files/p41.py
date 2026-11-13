"""Problem 41: Rotate a list left/right by K"""


def p41():
    def rotate_left(arr, k):
        k %= len(arr)
        return arr[k:] + arr[:k]

    def rotate_right(arr, k):
        k %= len(arr)
        return arr[-k:] + arr[:-k] if k else arr[:]

    data = [1, 2, 3, 4, 5, 6]
    print("Left  by 2:", rotate_left(data, 2))
    print("Right by 2:", rotate_right(data, 2))


if __name__ == "__main__":
    p41()
