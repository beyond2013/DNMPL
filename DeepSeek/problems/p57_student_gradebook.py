"""Problem 57: Menu-driven student grade book."""
def main():
    students = []
    while True:
        print("\n1. Add  2. List  3. Average  4. Exit")
        ch = input("Choice: ")
        if ch == '1':
            name  = input("Name: ")
            marks = float(input("Marks: "))
            students.append({"name": name, "marks": marks})
        elif ch == '2':
            for s in students:
                print(f"{s['name']}: {s['marks']}")
        elif ch == '3' and students:
            avg = sum(s['marks'] for s in students) / len(students)
            print(f"Class Average = {avg:.2f}")
        elif ch == '4':
            break

if __name__ == "__main__":
    main()
