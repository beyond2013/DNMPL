"""Problem 27: Prime check."""
n = int(input("Number: "))
is_p = n > 1 and all(n % i for i in range(2, int(n**0.5)+1))
print("Prime" if is_p else "Not prime")
