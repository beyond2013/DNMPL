"""Problem 57: Student structure: store and display N students"""

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    roll_no: int
    marks: float


def p57():
    students = [
        Student("Ali", 101, 78.5),
        Student("Sara", 102, 91.0),
        Student("Usman", 103, 64.25),
    ]
    print(f"{'Roll':<6}{'Name':<10}{'Marks':>6}")
    for s in students:
        print(f"{s.roll_no:<6}{s.name:<10}{s.marks:>6.1f}")
    top = max(students, key=lambda s: s.marks)
    print(f"Topper: {top.name} with {top.marks}")


if __name__ == "__main__":
    p57()
