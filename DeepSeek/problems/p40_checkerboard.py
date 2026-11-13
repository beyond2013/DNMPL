"""Problem 40: Checkerboard pattern."""
n = int(input("Size: "))
for i in range(n):
    print(" ".join("*" if (i+j)%2==0 else "." for j in range(n)))
