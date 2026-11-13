"""Problem 16: Simple calculator with branching."""
a  = float(input("A: "))
op = input("Op (+-*/): ")
b  = float(input("B: "))
if   op == '+': print(a + b)
elif op == '-': print(a - b)
elif op == '*': print(a * b)
elif op == '/' and b != 0: print(a / b)
else: print("Invalid operation or divide by zero")
