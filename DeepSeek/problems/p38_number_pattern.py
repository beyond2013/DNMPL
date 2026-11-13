"""Problem 38: Number pattern (1 / 12 / 123 ...)."""
n = int(input("Rows: "))
for i in range(1, n+1):
    print("".join(str(j) for j in range(1, i+1)))
