"""Problem 20: Number sign and magnitude category."""
n = float(input("Number: "))
if n == 0:  print("Zero")
elif n > 0: print("Positive " + ("small" if n < 10 else "large"))
else:       print("Negative " + ("small" if -n < 10 else "large"))
