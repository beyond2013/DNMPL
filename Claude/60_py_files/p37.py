"""Problem 37: Linear search and binary search"""


def p37():
    def linear_search(arr, target):
        for i, x in enumerate(arr):
            if x == target:
                return i
        return -1

    def binary_search(arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    data = [3, 9, 14, 21, 28, 35, 42]          # sorted for binary search
    print("Linear search 28 ->", linear_search(data, 28))
    print("Binary search 28 ->", binary_search(data, 28))
    print("Binary search 5  ->", binary_search(data, 5))


if __name__ == "__main__":
    p37()
