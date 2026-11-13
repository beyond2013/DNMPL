"""Problem 58: Read marks from a file; write a result report"""

import os
import tempfile


def p58():
    folder = tempfile.mkdtemp()
    in_path = os.path.join(folder, "marks.txt")
    out_path = os.path.join(folder, "report.txt")

    with open(in_path, "w") as f:               # create the sample input file
        f.write("Ali 78\nSara 91\nUsman 64\nHina 85\n")

    names, marks = [], []
    with open(in_path) as f:
        for line in f:
            parts = line.split()
            if len(parts) == 2:
                names.append(parts[0])
                marks.append(float(parts[1]))

    avg = sum(marks) / len(marks)
    hi, lo = max(marks), min(marks)
    with open(out_path, "w") as f:
        f.write(f"Average : {avg:.2f}\n")
        f.write(f"Highest : {hi} ({names[marks.index(hi)]})\n")
        f.write(f"Lowest  : {lo} ({names[marks.index(lo)]})\n")

    print(f"Report written to {out_path}:")
    with open(out_path) as f:
        print(f.read())


if __name__ == "__main__":
    p58()
