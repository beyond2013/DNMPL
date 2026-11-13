"""Problem 13: Grade calculator (0-100)."""
marks = float(input("Marks (0-100): "))
if marks >= 90:   grade = 'A+'
elif marks >= 80: grade = 'A'
elif marks >= 70: grade = 'B'
elif marks >= 60: grade = 'C'
elif marks >= 50: grade = 'D'
else:             grade = 'F'
print(f"Grade: {grade}")
