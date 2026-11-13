"""Problem 56: Recursive binary search"""


def p56():
    def bsearch(arr, target, low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            return bsearch(arr, target, mid + 1, high)
        return bsearch(arr, target, low, mid - 1)

    data = [2, 5, 8, 12, 16, 23, 38, 56]
    print("Index of 23:", bsearch(data, 23, 0, len(data) - 1))
    print("Index of 7 :", bsearch(data, 7, 0, len(data) - 1))


if __name__ == "__main__":
    p56()
