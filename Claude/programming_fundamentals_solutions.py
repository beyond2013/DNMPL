"""
Solutions to 60 Programming Fundamentals Problems (Python 3.10+)

Usage:
    python programming_fundamentals_solutions.py          # run all 60 demos
    python programming_fundamentals_solutions.py 5 12 40  # run selected problems

Each problem is a function p01() ... p60() that demonstrates the solution
with sample data, so the whole file runs without typing input. To make any
problem interactive, replace the sample values with input() calls, e.g.
    a = float(input("Enter a number: "))
"""

import math
import os
import random
import sys
import tempfile
from dataclasses import dataclass

PROBLEMS = {}


def problem(number, title):
    """Decorator that registers a solution so it can be run by number."""
    def decorator(func):
        PROBLEMS[number] = (title, func)
        return func
    return decorator


# =====================================================================
# A. INPUT, OUTPUT, AND ARITHMETIC
# =====================================================================

@problem(1, "Print name, program, and city in a formatted block")
def p01():
    name, program, city = "Ayesha Khan", "BS Computer Science", "Lahore"
    print("+" + "-" * 34 + "+")
    print(f"| Name    : {name:<22} |")
    print(f"| Program : {program:<22} |")
    print(f"| City    : {city:<22} |")
    print("+" + "-" * 34 + "+")


@problem(2, "Sum, difference, product, quotient, remainder")
def p02():
    a, b = 17, 5
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    if b != 0:
        print(f"{a} / {b} = {a / b:.2f}  (integer quotient {a // b})")
        print(f"{a} % {b} = {a % b}")
    else:
        print("Cannot divide by zero")


@problem(3, "Celsius <-> Fahrenheit")
def p03():
    def c_to_f(c):
        return c * 9 / 5 + 32

    def f_to_c(f):
        return (f - 32) * 5 / 9

    print(f"37 C  = {c_to_f(37):.1f} F")
    print(f"98.6 F = {f_to_c(98.6):.1f} C")


@problem(4, "Area/perimeter of rectangle; area/circumference of circle")
def p04():
    length, width, radius = 8, 5, 3
    print(f"Rectangle: area = {length * width}, perimeter = {2 * (length + width)}")
    print(f"Circle: area = {math.pi * radius ** 2:.2f}, "
          f"circumference = {2 * math.pi * radius:.2f}")


@problem(5, "Ohm's law: current and power")
def p05():
    voltage, resistance = 12.0, 4.0        # volts, ohms
    current = voltage / resistance          # I = V / R
    power = voltage * current               # P = V * I
    print(f"V = {voltage} V, R = {resistance} ohm")
    print(f"Current I = {current} A, Power P = {power} W")


@problem(6, "Swap two variables (with and without a temporary)")
def p06():
    a, b = 10, 20
    print("Before:", a, b)
    temp = a            # method 1: temporary variable
    a = b
    b = temp
    print("With temp:", a, b)

    a, b = 10, 20       # reset to the original values
    a = a + b           # method 2: arithmetic, no temporary
    b = a - b
    a = a - b
    print("Without temp:", a, b)

    a, b = 10, 20
    a, b = b, a         # method 3: Python's tuple swap
    print("Pythonic:", a, b)


# =====================================================================
# B. CONDITIONALS
# =====================================================================

@problem(7, "Positive, negative, or zero")
def p07():
    for n in (5, -3, 0):
        if n > 0:
            print(n, "is positive")
        elif n < 0:
            print(n, "is negative")
        else:
            print(n, "is zero")


@problem(8, "Even or odd")
def p08():
    for n in (10, 7):
        print(n, "is", "even" if n % 2 == 0 else "odd")


@problem(9, "Largest of three numbers")
def p09():
    a, b, c = 14, 42, 27
    if a >= b and a >= c:
        largest = a
    elif b >= c:
        largest = b
    else:
        largest = c
    print(f"Largest of {a}, {b}, {c} is {largest}")


@problem(10, "Leap year")
def p10():
    def is_leap(y):
        return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

    for year in (1900, 2000, 2024, 2026):
        print(year, "is a leap year" if is_leap(year) else "is not a leap year")


@problem(11, "Percentage to grade")
def p11():
    def grade(p):
        if p < 0 or p > 100:
            return "Invalid"
        if p >= 80:
            return "A"
        if p >= 70:
            return "B"
        if p >= 60:
            return "C"
        if p >= 50:
            return "D"
        return "F"

    for p in (92, 74.5, 61, 50, 35, 120):
        print(f"{p}% -> {grade(p)}")


@problem(12, "Simple calculator with match/switch (Python 3.10+)")
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


@problem(13, "Triangle validity and type")
def p13():
    def classify(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return "Invalid (sides must be positive)"
        if a + b <= c or a + c <= b or b + c <= a:
            return "Not a triangle"
        if a == b == c:
            return "Equilateral"
        if a == b or b == c or a == c:
            return "Isosceles"
        return "Scalene"

    for sides in [(3, 3, 3), (5, 5, 8), (3, 4, 5), (1, 2, 3)]:
        print(sides, "->", classify(*sides))


@problem(14, "Slab-based electricity bill")
def p14():
    def bill(units):
        # first 100 units @10, next 100 @15, next 100 @20, rest @25
        slabs = [(100, 10), (100, 15), (100, 20)]
        total, remaining = 0, units
        for size, rate in slabs:
            used = min(remaining, size)
            total += used * rate
            remaining -= used
        total += remaining * 25
        return total

    for units in (80, 150, 250, 400):
        print(f"{units} units -> Rs {bill(units)}")


# =====================================================================
# C. LOOPS
# =====================================================================

@problem(15, "Print 1 to N")
def p15():
    n = 10
    for i in range(1, n + 1):
        print(i, end=" ")
    print()


@problem(16, "Multiplication table")
def p16():
    n = 7
    for i in range(1, 11):
        print(f"{n} x {i:2} = {n * i}")


@problem(17, "Sum of first N natural numbers")
def p17():
    n = 100
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f"Loop sum = {total}, formula n(n+1)/2 = {n * (n + 1) // 2}")


@problem(18, "Factorial")
def p18():
    n = 6
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    print(f"{n}! = {fact}")


@problem(19, "Count digits")
def p19():
    n = 987654
    count, temp = 0, abs(n)
    if temp == 0:
        count = 1
    while temp > 0:
        temp //= 10
        count += 1
    print(f"{n} has {count} digits")


@problem(20, "Reverse an integer and test palindrome")
def p20():
    for n in (12321, 12345):
        reversed_n, temp = 0, n
        while temp > 0:
            reversed_n = reversed_n * 10 + temp % 10
            temp //= 10
        verdict = "is" if reversed_n == n else "is not"
        print(f"{n} reversed = {reversed_n}; {verdict} a palindrome")


@problem(21, "Sum of digits")
def p21():
    n = 4829
    total, temp = 0, n
    while temp > 0:
        total += temp % 10
        temp //= 10
    print(f"Sum of digits of {n} = {total}")


@problem(22, "First N Fibonacci numbers")
def p22():
    n = 12
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


def is_prime(n):
    """Shared helper: trial division up to sqrt(n)."""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


@problem(23, "Prime check and primes up to N")
def p23():
    print("97 prime?", is_prime(97), "| 91 prime?", is_prime(91))
    n = 50
    print(f"Primes up to {n}:", [x for x in range(2, n + 1) if is_prime(x)])


@problem(24, "GCD and LCM (Euclid)")
def p24():
    a, b = 48, 18
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    gcd = x
    lcm = a * b // gcd
    print(f"GCD({a}, {b}) = {gcd}, LCM({a}, {b}) = {lcm}")


# =====================================================================
# D. NESTED LOOPS AND PATTERNS
# =====================================================================

@problem(25, "Right-angled triangle of stars")
def p25():
    n = 5
    for i in range(1, n + 1):
        print("*" * i)


@problem(26, "Pyramid of stars")
def p26():
    n = 5
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))


@problem(27, "Pascal's triangle")
def p27():
    rows = 6
    for i in range(rows):
        value = 1
        line = []
        for j in range(i + 1):
            line.append(str(value))
            value = value * (i - j) // (j + 1)   # C(i, j+1) from C(i, j)
        print(" ".join(line).center(rows * 4))


@problem(28, "Armstrong numbers between 1 and 1000")
def p28():
    result = []
    for n in range(1, 1001):
        digits = len(str(n))
        total, temp = 0, n
        while temp > 0:
            total += (temp % 10) ** digits
            temp //= 10
        if total == n:
            result.append(n)
    print(result)


# =====================================================================
# E. FUNCTIONS
# =====================================================================

@problem(29, "max, min, abs functions")
def p29():
    def my_max(a, b):
        return a if a >= b else b

    def my_min(a, b):
        return a if a <= b else b

    def my_abs(x):
        return -x if x < 0 else x

    print("max(7, 12) =", my_max(7, 12))
    print("min(7, 12) =", my_min(7, 12))
    print("abs(-9.5)  =", my_abs(-9.5))


@problem(30, "isPrime and twin primes")
def p30():
    twins = [(p, p + 2) for p in range(2, 100) if is_prime(p) and is_prime(p + 2)]
    print("Twin primes below 100:", twins)


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


@problem(31, "Decimal <-> binary conversion")
def p31():
    for n in (0, 10, 255):
        b = to_binary(n)
        print(f"{n} -> {b} -> {to_decimal(b)}")


@problem(32, "power(base, exp) without ** operator")
def p32():
    def power(base, exp):
        result = 1
        for _ in range(abs(exp)):
            result *= base
        return result if exp >= 0 else 1 / result

    print("2^10 =", power(2, 10))
    print("5^0  =", power(5, 0))
    print("2^-3 =", power(2, -3))


@problem(33, "Simple and compound interest")
def p33():
    def simple(p, r, t):
        return p * r * t / 100

    def compound(p, r, t, n=1):
        return p * (1 + r / (100 * n)) ** (n * t) - p

    p, r, t = 10000, 8, 3
    print(f"Simple interest   : {simple(p, r, t):.2f}")
    print(f"Compound (yearly) : {compound(p, r, t):.2f}")
    print(f"Compound (monthly): {compound(p, r, t, 12):.2f}")


@problem(34, "Pass-by-value vs pass-by-reference behaviour")
def p34():
    # Python passes object references. Immutable objects (int, str, tuple)
    # behave like pass-by-value; mutable objects (list, dict) can be changed.
    def try_swap_ints(a, b):
        a, b = b, a            # only changes local names

    def swap_in_list(lst):
        lst[0], lst[1] = lst[1], lst[0]   # mutates the caller's list

    def swap_returning(a, b):
        return b, a

    x, y = 1, 2
    try_swap_ints(x, y)
    print("After try_swap_ints:", x, y, "(unchanged)")

    pair = [1, 2]
    swap_in_list(pair)
    print("After swap_in_list :", pair, "(changed)")

    x, y = swap_returning(x, y)
    print("After swap_returning:", x, y, "(idiomatic Python)")


# =====================================================================
# F. ARRAYS / LISTS
# =====================================================================

@problem(35, "Print N numbers in reverse")
def p35():
    data = [4, 8, 15, 16, 23, 42]
    for i in range(len(data) - 1, -1, -1):
        print(data[i], end=" ")
    print()


@problem(36, "Sum, average, max, min of a list")
def p36():
    data = [12, 45, 7, 33, 21]
    total, largest, smallest = 0, data[0], data[0]
    for x in data:
        total += x
        largest = max(largest, x)
        smallest = min(smallest, x)
    print(f"Sum={total}, Average={total / len(data):.2f}, Max={largest}, Min={smallest}")


@problem(37, "Linear search and binary search")
def p37():
    def linear_search(arr, target):
        for i, x in enumerate(arr):
            if x == target:
                return i
        return -1

    def binary_search(arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    data = [3, 9, 14, 21, 28, 35, 42]          # sorted for binary search
    print("Linear search 28 ->", linear_search(data, 28))
    print("Binary search 28 ->", binary_search(data, 28))
    print("Binary search 5  ->", binary_search(data, 5))


@problem(38, "Count even and odd elements")
def p38():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even = sum(1 for x in data if x % 2 == 0)
    print(f"Even = {even}, Odd = {len(data) - even}")


@problem(39, "Remove duplicates (keep first occurrence)")
def p39():
    data = [4, 2, 4, 7, 2, 9, 7]
    unique = []
    for x in data:
        if x not in unique:
            unique.append(x)
    print(data, "->", unique)


@problem(40, "Bubble sort")
def p40():
    data = [64, 34, 25, 12, 22, 11, 90]
    n = len(data)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:          # already sorted: stop early
            break
    print("Sorted:", data)


@problem(41, "Rotate a list left/right by K")
def p41():
    def rotate_left(arr, k):
        k %= len(arr)
        return arr[k:] + arr[:k]

    def rotate_right(arr, k):
        k %= len(arr)
        return arr[-k:] + arr[:-k] if k else arr[:]

    data = [1, 2, 3, 4, 5, 6]
    print("Left  by 2:", rotate_left(data, 2))
    print("Right by 2:", rotate_right(data, 2))


@problem(42, "Merge two sorted lists")
def p42():
    a, b = [1, 4, 9, 15], [2, 3, 10, 20, 25]
    merged, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    print(merged)


# =====================================================================
# G. STRINGS
# =====================================================================

@problem(43, "Count vowels, consonants, digits, spaces")
def p43():
    text = "Programming in Python 3 is fun!"
    vowels = consonants = digits = spaces = 0
    for ch in text.lower():
        if ch in "aeiou":
            vowels += 1
        elif ch.isalpha():
            consonants += 1
        elif ch.isdigit():
            digits += 1
        elif ch == " ":
            spaces += 1
    print(f"Vowels={vowels}, Consonants={consonants}, Digits={digits}, Spaces={spaces}")


@problem(44, "Reverse a string and check palindrome")
def p44():
    for s in ("Level", "Python"):
        rev = ""
        for ch in s:
            rev = ch + rev
        verdict = "is" if rev.lower() == s.lower() else "is not"
        print(f"{s} reversed = {rev}; {verdict} a palindrome")


@problem(45, "Upper/lower case without library functions")
def p45():
    def to_upper(s):
        out = ""
        for ch in s:
            out += chr(ord(ch) - 32) if "a" <= ch <= "z" else ch
        return out

    def to_lower(s):
        out = ""
        for ch in s:
            out += chr(ord(ch) + 32) if "A" <= ch <= "Z" else ch
        return out

    s = "Hello, World 123"
    print(to_upper(s), "|", to_lower(s))


@problem(46, "Count words in a sentence")
def p46():
    sentence = "  Python   is   easy   to   learn  "
    count, in_word = 0, False
    for ch in sentence:
        if ch != " " and not in_word:
            count += 1
            in_word = True
        elif ch == " ":
            in_word = False
    print(f"Words = {count}")


@problem(47, "Anagram check")
def p47():
    def are_anagrams(a, b):
        a = a.replace(" ", "").lower()
        b = b.replace(" ", "").lower()
        if len(a) != len(b):
            return False
        counts = {}
        for ch in a:
            counts[ch] = counts.get(ch, 0) + 1
        for ch in b:
            if counts.get(ch, 0) == 0:
                return False
            counts[ch] -= 1
        return True

    for a, b in [("Listen", "Silent"), ("Hello", "World")]:
        print(f"{a} / {b} -> {are_anagrams(a, b)}")


@problem(48, "Caesar cipher")
def p48():
    def shift_text(text, key):
        out = ""
        for ch in text:
            if ch.isupper():
                out += chr((ord(ch) - ord("A") + key) % 26 + ord("A"))
            elif ch.islower():
                out += chr((ord(ch) - ord("a") + key) % 26 + ord("a"))
            else:
                out += ch
        return out

    message, key = "Hello, World!", 3
    cipher = shift_text(message, key)
    print("Encrypted:", cipher)
    print("Decrypted:", shift_text(cipher, -key))


# =====================================================================
# H. TWO-DIMENSIONAL ARRAYS
# =====================================================================

def show(matrix):
    for row in matrix:
        print("  ".join(f"{x:3}" for x in row))


@problem(49, "Print a matrix and its transpose")
def p49():
    m = [[1, 2, 3], [4, 5, 6]]
    print("Matrix:")
    show(m)
    t = [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]
    print("Transpose:")
    show(t)


@problem(50, "Matrix addition and multiplication")
def p50():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    n = len(a)
    add = [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]
    mul = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mul[i][j] += a[i][k] * b[k][j]
    print("A + B:")
    show(add)
    print("A x B:")
    show(mul)


@problem(51, "Row sums, column sums, diagonal sums")
def p51():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n = len(m)
    print("Row sums   :", [sum(row) for row in m])
    print("Column sums:", [sum(m[i][j] for i in range(n)) for j in range(n)])
    print("Main diagonal:", sum(m[i][i] for i in range(n)))
    print("Anti diagonal:", sum(m[i][n - 1 - i] for i in range(n)))


@problem(52, "Symmetric matrix check")
def p52():
    def is_symmetric(m):
        n = len(m)
        return all(m[i][j] == m[j][i] for i in range(n) for j in range(n))

    print(is_symmetric([[1, 2, 3], [2, 4, 5], [3, 5, 6]]))   # True
    print(is_symmetric([[1, 2], [3, 4]]))                    # False


# =====================================================================
# I. RECURSION
# =====================================================================

def fact_rec(n):
    return 1 if n <= 1 else n * fact_rec(n - 1)


def fib_rec(n):
    return n if n < 2 else fib_rec(n - 1) + fib_rec(n - 2)


@problem(53, "Factorial and Fibonacci: recursive vs iterative")
def p53():
    def fact_iter(n):
        r = 1
        for i in range(2, n + 1):
            r *= i
        return r

    def fib_iter(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    print("6!   recursive:", fact_rec(6), "| iterative:", fact_iter(6))
    print("fib(10) recursive:", fib_rec(10), "| iterative:", fib_iter(10))
    print("Note: recursive Fibonacci repeats work and is exponentially slow.")


@problem(54, "Sum of digits (recursive)")
def p54():
    def digit_sum(n):
        return n if n < 10 else n % 10 + digit_sum(n // 10)

    print("Digit sum of 4829 =", digit_sum(4829))


@problem(55, "Tower of Hanoi")
def p55():
    moves = []

    def hanoi(n, source, target, spare):
        if n == 0:
            return
        hanoi(n - 1, source, spare, target)
        moves.append(f"Move disk {n} from {source} to {target}")
        hanoi(n - 1, spare, target, source)

    hanoi(3, "A", "C", "B")
    print("\n".join(moves))
    print(f"Total moves = {len(moves)} (2^3 - 1)")


@problem(56, "Recursive binary search")
def p56():
    def bsearch(arr, target, low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            return bsearch(arr, target, mid + 1, high)
        return bsearch(arr, target, low, mid - 1)

    data = [2, 5, 8, 12, 16, 23, 38, 56]
    print("Index of 23:", bsearch(data, 23, 0, len(data) - 1))
    print("Index of 7 :", bsearch(data, 7, 0, len(data) - 1))


# =====================================================================
# J. STRUCTURES, FILES, AND MINI-PROJECTS
# =====================================================================

@dataclass
class Student:
    name: str
    roll_no: int
    marks: float


@problem(57, "Student structure: store and display N students")
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


@problem(58, "Read marks from a file; write a result report")
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


class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit must be positive."
        self.balance += amount
        return f"Deposited {amount:.2f}."

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal must be positive."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrew {amount:.2f}."


def bank_menu():
    """Interactive menu version: call this from the console to try it."""
    acct = BankAccount("User")
    while True:
        print("\n1) Deposit  2) Withdraw  3) Balance  4) Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            print(acct.deposit(float(input("Amount: "))))
        elif choice == "2":
            print(acct.withdraw(float(input("Amount: "))))
        elif choice == "3":
            print(f"Balance: {acct.balance:.2f}")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


@problem(59, "Menu-driven bank account simulator (scripted demo)")
def p59():
    # The demo plays a scripted session. Run bank_menu() for the real thing.
    acct = BankAccount("Demo", 1000)
    for action, amount in [("deposit", 500), ("withdraw", 200),
                           ("withdraw", 5000), ("deposit", -10)]:
        print(getattr(acct, action)(amount))
    print(f"Final balance: {acct.balance:.2f}")


def guessing_game(secret, scripted_guesses=None, max_attempts=7):
    """Play with input() if scripted_guesses is None, else use the list."""
    attempts = 0
    guesses = iter(scripted_guesses) if scripted_guesses is not None else None
    while attempts < max_attempts:
        raw = next(guesses, None) if guesses else input("Your guess (1-100): ")
        if raw is None:
            break
        guess = int(raw)
        attempts += 1
        if guess == secret:
            print(f"Correct! You needed {attempts} attempt(s).")
            return True
        print(f"{guess}: too {'low' if guess < secret else 'high'}.")
    print(f"Out of attempts. The number was {secret}.")
    return False


@problem(60, "Number-guessing game (scripted demo)")
def p60():
    secret = random.randint(1, 100)
    print("(Demo: binary-search strategy against a random secret)")
    low, high, guesses = 1, 100, []
    # Precompute a binary-search sequence of guesses for the demo
    while low <= high:
        mid = (low + high) // 2
        guesses.append(mid)
        if mid == secret:
            break
        low, high = (mid + 1, high) if mid < secret else (low, mid - 1)
    guessing_game(secret, guesses)
    # For a real game:  guessing_game(random.randint(1, 100))


# =====================================================================
# RUNNER
# =====================================================================

def main():
    wanted = [int(a) for a in sys.argv[1:]] or sorted(PROBLEMS)
    for number in wanted:
        if number not in PROBLEMS:
            print(f"No problem numbered {number}")
            continue
        title, func = PROBLEMS[number]
        print(f"\n=== Problem {number}: {title} ===")
        func()


if __name__ == "__main__":
    main()
