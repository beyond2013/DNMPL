"""Problem 51: Linear search."""
arr = [10, 20, 30, 40, 50]
key = int(input("Search: "))
idx = arr.index(key) if key in arr else -1
print(f"Found at {idx}" if idx != -1 else "Not found")
