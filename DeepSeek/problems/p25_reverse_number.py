"""Problem 25: Reverse a number."""
n = int(input("Number: "))
rev = 0
while n > 0:
    rev = rev*10 + n%10
    n //= 10
print(f"Reversed = {rev}")
