"""Problem 8: Total marks and percentage (5 subjects)."""
marks = [float(input(f"Subject {i+1}: ")) for i in range(5)]
total = sum(marks)
print(f"Total = {total}/500, Percentage = {total/5:.2f}%")
