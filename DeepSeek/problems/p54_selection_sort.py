"""Problem 54: Selection sort."""
def selection(arr):
    for i in range(len(arr)):
        m = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[m]: m = j
        arr[i], arr[m] = arr[m], arr[i]
    return arr

if __name__ == "__main__":
    print(selection([29, 10, 14, 37, 13]))
