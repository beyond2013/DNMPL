"""Problem 1: Print name, program, and city in a formatted block"""


def p01():
    name, program, city = "Ayesha Khan", "BS Computer Science", "Lahore"
    print("+" + "-" * 34 + "+")
    print(f"| Name    : {name:<22} |")
    print(f"| Program : {program:<22} |")
    print(f"| City    : {city:<22} |")
    print("+" + "-" * 34 + "+")


if __name__ == "__main__":
    p01()
