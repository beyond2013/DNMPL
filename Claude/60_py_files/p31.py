"""Problem 31: Decimal <-> binary conversion"""


def to_binary(n):
    if n == 0:
        return "0"
    bits = ""
    while n > 0:
        bits = str(n % 2) + bits
        n //= 2
    return bits


def to_decimal(bits):
    value = 0
    for ch in bits:
        value = value * 2 + int(ch)
    return value


def p31():
    for n in (0, 10, 255):
        b = to_binary(n)
        print(f"{n} -> {b} -> {to_decimal(b)}")


if __name__ == "__main__":
    p31()
