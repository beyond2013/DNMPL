"""Problem 39: Diamond pattern."""
n = int(input("Half-size: "))
for i in range(1, n+1):
    print(" "*(n-i) + "* "*i)
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "* "*i)
