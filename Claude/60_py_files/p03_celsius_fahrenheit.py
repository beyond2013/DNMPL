"""Problem 3: Celsius <-> Fahrenheit"""


def p03():
    def c_to_f(c):
        return c * 9 / 5 + 32

    def f_to_c(f):
        return (f - 32) * 5 / 9

    print(f"37 C  = {c_to_f(37):.1f} F")
    print(f"98.6 F = {f_to_c(98.6):.1f} C")


if __name__ == "__main__":
    p03()
