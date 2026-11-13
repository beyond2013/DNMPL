"""Problem 34: Inverted triangle star pattern."""
n = int(input("Rows: "))
for i in range(n, 0, -1):
    print("* " * i)
