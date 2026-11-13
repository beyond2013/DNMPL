"""Problem 52: Binary search on sorted array."""
def bsearch(arr, key):
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if   arr[mid] == key: return mid
        elif arr[mid] <  key: lo = mid+1
        else:                 hi = mid-1
    return -1

if __name__ == "__main__":
    print(bsearch([10,20,30,40,50], 30))
