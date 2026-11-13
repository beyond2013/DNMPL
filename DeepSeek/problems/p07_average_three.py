"""Problem 7: Average of three numbers."""
nums = [float(input(f"Number {i+1}: ")) for i in range(3)]
print(f"Average = {sum(nums)/3:.2f}")
