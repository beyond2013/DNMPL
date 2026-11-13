"""Problem 36: Floyd's triangle."""
n = int(input("Rows: "))
k = 1
for i in range(1, n+1):
    for _ in range(i):
        print(k, end=" ")
        k += 1
    print()
