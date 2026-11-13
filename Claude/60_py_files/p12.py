"""Problem 12: Simple calculator with match/switch (Python 3.10+)"""


def p12():
    def calculate(a, op, b):
        match op:
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b
            case "/":
                return "Error: division by zero" if b == 0 else a / b
            case _:
                return "Error: unknown operator"

    for a, op, b in [(8, "+", 2), (8, "-", 2), (8, "*", 2), (8, "/", 2),
                     (8, "/", 0), (8, "%", 2)]:
        print(f"{a} {op} {b} = {calculate(a, op, b)}")


if __name__ == "__main__":
    p12()
