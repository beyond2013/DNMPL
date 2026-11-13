# Programming Fundamentals: 60 Problems with Solutions

As a faculty member teaching diverse students (Pre-Engineering, ICS, and Diploma holders), I've designed these problems to progress from basic to intermediate. I'll use **Python** (readable syntax, ideal for beginners) and occasionally note C/C++ equivalents since diploma students will encounter them.

---

## Section A: Input/Output & Variables (Problems 1–10)

### Problem 1: Hello, Student
Print a greeting with the student's name.
```python
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to Programming Fundamentals.")
```

### Problem 2: Sum of Two Numbers
```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(f"Sum = {a + b}")
```

### Problem 3: Swap Two Variables (without third variable)
```python
a, b = 5, 10
a, b = b, a
print(f"After swap: a={a}, b={b}")
```

### Problem 4: Area & Perimeter of a Rectangle
```python
length = float(input("Length: "))
width = float(input("Width: "))
print(f"Area = {length * width}")
print(f"Perimeter = {2 * (length + width)}")
```

### Problem 5: Celsius to Fahrenheit
```python
c = float(input("Celsius: "))
f = (c * 9/5) + 32
print(f"{c}°C = {f}°F")
```

### Problem 6: Simple Interest Calculator
```python
p = float(input("Principal: "))
r = float(input("Rate (%): "))
t = float(input("Time (years): "))
si = (p * r * t) / 100
print(f"Simple Interest = {si:.2f}")
```

### Problem 7: Average of Three Numbers
```python
nums = [float(input(f"Number {i+1}: ")) for i in range(3)]
print(f"Average = {sum(nums)/3:.2f}")
```

### Problem 8: Total Marks & Percentage
```python
marks = [float(input(f"Subject {i+1}: ")) for i in range(5)]
total = sum(marks)
print(f"Total = {total}/500, Percentage = {total/5:.2f}%")
```

### Problem 9: BMI Calculator
```python
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))
bmi = weight / (height ** 2)
print(f"BMI = {bmi:.2f}")
```

### Problem 10: Time Conversion (seconds → h:m:s)
```python
total = int(input("Total seconds: "))
h, rem = divmod(total, 3600)
m, s = divmod(rem, 60)
print(f"{h}h {m}m {s}s")
```

---

## Section B: Conditionals (Problems 11–20)

### Problem 11: Even or Odd
```python
n = int(input("Number: "))
print("Even" if n % 2 == 0 else "Odd")
```

### Problem 12: Largest of Three
```python
a, b, c = map(int, input("Three numbers: ").split())
print(f"Largest = {max(a, b, c)}")
```

### Problem 13: Grade Calculator
```python
marks = float(input("Marks (0–100): "))
if marks >= 90: grade = 'A+'
elif marks >= 80: grade = 'A'
elif marks >= 70: grade = 'B'
elif marks >= 60: grade = 'C'
elif marks >= 50: grade = 'D'
else: grade = 'F'
print(f"Grade: {grade}")
```

### Problem 14: Leap Year Checker
```python
y = int(input("Year: "))
is_leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
print(f"{y} is {'a leap year' if is_leap else 'not a leap year'}")
```

### Problem 15: Quadratic Roots
```python
import math
a, b, c = map(float, input("a b c: ").split())
d = b*b - 4*a*c
if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Two real roots: {r1:.2f}, {r2:.2f}")
elif d == 0:
    print(f"One root: {-b/(2*a):.2f}")
else:
    print("Complex roots")
```

### Problem 16: Simple Calculator (using match/if-elif)
```python
a = float(input("A: ")); op = input("Op (+-*/): "); b = float(input("B: "))
if op == '+': print(a + b)
elif op == '-': print(a - b)
elif op == '*': print(a * b)
elif op == '/' and b != 0: print(a / b)
else: print("Invalid or divide by zero")
```

### Problem 17: Vowel or Consonant
```python
ch = input("Character: ").lower()
print("Vowel" if ch in "aeiou" else "Consonant" if ch.isalpha() else "Not a letter")
```

### Problem 18: Triangle Validity & Type
```python
a, b, c = map(float, input("Sides: ").split())
if a+b>c and b+c>a and a+c>b:
    if a==b==c: print("Equilateral")
    elif a==b or b==c or a==c: print("Isosceles")
    else: print("Scalene")
else: print("Invalid triangle")
```

### Problem 19: Electricity Bill (slab-based) — *familiar to diploma students*
```python
units = float(input("Units: "))
if units <= 100: bill = units * 5
elif units <= 200: bill = 100*5 + (units-100)*7
else: bill = 100*5 + 100*7 + (units-200)*10
print(f"Bill = Rs. {bill:.2f}")
```

### Problem 20: Number Sign & Magnitude Category
```python
n = float(input("Number: "))
if n == 0: print("Zero")
elif n > 0: print("Positive " + ("small" if n < 10 else "large"))
else: print("Negative " + ("small" if -n < 10 else "large"))
```

---

## Section C: Loops (Problems 21–32)

### Problem 21: Print 1 to N
```python
n = int(input("N: "))
for i in range(1, n+1): print(i, end=" ")
```

### Problem 22: Sum of First N Natural Numbers
```python
n = int(input("N: "))
print(f"Sum = {n*(n+1)//2}")
```

### Problem 23: Factorial
```python
n = int(input("N: "))
f = 1
for i in range(2, n+1): f *= i
print(f"{n}! = {f}")
```

### Problem 24: Fibonacci Series
```python
n = int(input("Terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" "); a, b = b, a+b
```

### Problem 25: Reverse a Number
```python
n = int(input("Number: "))
rev = 0
while n > 0:
    rev = rev*10 + n%10; n //= 10
print(f"Reversed = {rev}")
```

### Problem 26: Palindrome Number
```python
n = int(input("Number: "))
s = str(n)
print("Palindrome" if s == s[::-1] else "Not palindrome")
```

### Problem 27: Prime Check
```python
n = int(input("Number: "))
is_p = n > 1 and all(n % i for i in range(2, int(n**0.5)+1))
print("Prime" if is_p else "Not prime")
```

### Problem 28: Primes up to N (Sieve)
```python
n = int(input("N: "))
sieve = [True]*(n+1); sieve[0:2] = [False, False]
for i in range(2, int(n**0.5)+1):
    if sieve[i]:
        for j in range(i*i, n+1, i): sieve[j] = False
print([i for i in range(n+1) if sieve[i]])
```

### Problem 29: Sum of Digits
```python
n = int(input("Number: "))
print(f"Sum of digits = {sum(int(d) for d in str(abs(n)))}")
```

### Problem 30: GCD & LCM (Euclidean algorithm)
```python
a, b = map(int, input("Two numbers: ").split())
x, y = a, b
while y: x, y = y, x % y
print(f"GCD = {x}, LCM = {a*b//x}")
```

### Problem 31: Multiplication Table
```python
n = int(input("Number: "))
for i in range(1, 11): print(f"{n} x {i} = {n*i}")
```

### Problem 32: Armstrong Number (3-digit)
```python
n = int(input("3-digit number: "))
s = sum(int(d)**3 for d in str(n))
print("Armstrong" if s == n else "Not Armstrong")
```

---

## Section D: Nested Loops & Patterns (Problems 33–40)

### Problem 33: Right Triangle Star Pattern
```python
n = int(input("Rows: "))
for i in range(1, n+1): print("* " * i)
```

### Problem 34: Inverted Triangle
```python
n = int(input("Rows: "))
for i in range(n, 0, -1): print("* " * i)
```

### Problem 35: Pyramid Pattern
```python
n = int(input("Rows: "))
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)
```

### Problem 36: Floyd's Triangle
```python
n = int(input("Rows: ")); k = 1
for i in range(1, n+1):
    for _ in range(i): print(k, end=" "); k += 1
    print()
```

### Problem 37: Pascal's Triangle
```python
n = int(input("Rows: "))
row = [1]
for i in range(n):
    print(" " * (n-i), *row)
    row = [1] + [row[j]+row[j+1] for j in range(len(row)-1)] + [1]
```

### Problem 38: Number Pattern (1 / 12 / 123...)
```python
n = int(input("Rows: "))
for i in range(1, n+1):
    print("".join(str(j) for j in range(1, i+1)))
```

### Problem 39: Diamond Pattern
```python
n = int(input("Half-size: "))
for i in range(1, n+1): print(" "*(n-i) + "* "*i)
for i in range(n-1, 0, -1): print(" "*(n-i) + "* "*i)
```

### Problem 40: Checkerboard (alternating)
```python
n = int(input("Size: "))
for i in range(n):
    print(" ".join("*" if (i+j)%2==0 else "." for j in range(n)))
```

---

## Section E: Functions & Recursion (Problems 41–48)

### Problem 41: Function — is_prime
```python
def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))
print(is_prime(17))
```

### Problem 42: Function — Calculator with Separate Functions
```python
def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b if b else None
print(add(3,4), sub(3,4), mul(3,4), div(3,4))
```

### Problem 43: Recursive Factorial
```python
def fact(n): return 1 if n <= 1 else n * fact(n-1)
print(fact(6))
```

### Problem 44: Recursive Fibonacci
```python
def fib(n): return n if n < 2 else fib(n-1) + fib(n-2)
print([fib(i) for i in range(10)])
```

### Problem 45: Recursive Sum of Digits
```python
def digit_sum(n): return 0 if n == 0 else n % 10 + digit_sum(n // 10)
print(digit_sum(1234))
```

### Problem 46: Recursive Power (x^n)
```python
def power(x, n): return 1 if n == 0 else x * power(x, n-1)
print(power(2, 10))
```

### Problem 47: Function — Count Vowels
```python
def count_vowels(s): return sum(1 for c in s.lower() if c in "aeiou")
print(count_vowels("Programming Fundamentals"))
```

### Problem 48: Tower of Hanoi
```python
def hanoi(n, src, aux, dst):
    if n == 1: print(f"Move disk 1: {src} -> {dst}"); return
    hanoi(n-1, src, dst, aux)
    print(f"Move disk {n}: {src} -> {dst}")
    hanoi(n-1, aux, src, dst)
hanoi(3, 'A', 'B', 'C')
```

---

## Section F: Arrays / Lists & Strings (Problems 49–56)

### Problem 49: Max & Min in an Array
```python
arr = list(map(int, input("Numbers: ").split()))
print(f"Max = {max(arr)}, Min = {min(arr)}")
```

### Problem 50: Reverse an Array (in-place)
```python
arr = [1,2,3,4,5]
arr.reverse()
print(arr)
```

### Problem 51: Linear Search
```python
arr = [10, 20, 30, 40, 50]
key = int(input("Search: "))
idx = arr.index(key) if key in arr else -1
print(f"Found at {idx}" if idx != -1 else "Not found")
```

### Problem 52: Binary Search
```python
def bsearch(arr, key):
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] == key: return mid
        elif arr[mid] < key: lo = mid+1
        else: hi = mid-1
    return -1
print(bsearch([10,20,30,40,50], 30))
```

### Problem 53: Bubble Sort
```python
def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bubble([64, 34, 25, 12, 22, 11, 90]))
```

### Problem 54: Selection Sort
```python
def selection(arr):
    for i in range(len(arr)):
        m = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[m]: m = j
        arr[i], arr[m] = arr[m], arr[i]
    return arr
print(selection([29, 10, 14, 37, 13]))
```

### Problem 55: String Reverse & Palindrome Check
```python
s = input("String: ")
print(f"Reversed: {s[::-1]}")
print("Palindrome" if s == s[::-1] else "Not palindrome")
```

### Problem 56: Count Words, Vowels, Consonants
```python
text = input("Text: ")
words = len(text.split())
vowels = sum(1 for c in text.lower() if c in "aeiou")
consonants = sum(1 for c in text.lower() if c.isalpha() and c not in "aeiou")
print(f"Words={words}, Vowels={vowels}, Consonants={consonants}")
```

---

## Section G: Capstone / Applied (Problems 57–60)

### Problem 57: Student Grade Book (Menu-driven with list of dicts)
```python
students = []
while True:
    print("\n1. Add  2. List  3. Average  4. Exit")
    ch = input("Choice: ")
    if ch == '1':
        name = input("Name: "); marks = float(input("Marks: "))
        students.append({"name": name, "marks": marks})
    elif ch == '2':
        for s in students: print(f"{s['name']}: {s['marks']}")
    elif ch == '3' and students:
        print(f"Class Average = {sum(s['marks'] for s in students)/len(students):.2f}")
    elif ch == '4': break
```

### Problem 58: Matrix Addition & Multiplication
```python
def mat_add(A, B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mat_mul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
A = [[1,2],[3,4]]; B = [[5,6],[7,8]]
print("Add:", mat_add(A,B)); print("Mul:", mat_mul(A,B))
```

### Problem 59: Phone Directory (Search & Delete)
```python
directory = {}
while True:
    print("\n1. Add  2. Search  3. Delete  4. List  5. Exit")
    ch = input("Choice: ")
    if ch == '1': directory[input("Name: ")] = input("Phone: ")
    elif ch == '2':
        name = input("Search: ")
        print(directory.get(name, "Not found"))
    elif ch == '3': directory.pop(input("Delete: "), None)
    elif ch == '4':
        for k, v in directory.items(): print(f"{k}: {v}")
    elif ch == '5': break
```

### Problem 60: Password Validator
```python
import string
def validate(pw):
    rules = [
        (len(pw) >= 8, "at least 8 characters"),
        (any(c.isupper() for c in pw), "an uppercase letter"),
        (any(c.islower() for c in pw), "a lowercase letter"),
        (any(c.isdigit() for c in pw), "a digit"),
        (any(c in string.punctuation for c in pw), "a special character"),
    ]
    errors = [msg for ok, msg in rules if not ok]
    return errors if errors else None

pw = input("Password: ")
err = validate(pw)
print("Valid password!" if err is None else "Missing: " + ", ".join(err))
```

---

## Teaching Notes (for diverse cohorts)

| Group | Suggested focus |
|-------|----------------|
| **Pre-Engineering** | Strong in math → emphasize #15, #27, #30, #44–48 (recursion, algorithms) |
| **ICS** | Familiar with flowcharts → jump quickly to #20–25, then strings (#55–56) |
| **Diploma (Electrical/Electronic)** | Connect to #16, #19 (bill), #20, #38 patterns (bit-level thinking), and #58 matrices (circuit analysis) |

**Pedagogical progression I recommend:**
1. **Weeks 1–3:** Problems 1–10 (I/O, arithmetic) — pair with C if diploma students need it.
2. **Weeks 4–5:** Problems 11–20 (branching).
3. **Weeks 6–8:** Problems 21–32 (loops) — critical milestone.
4. **Weeks 9–10:** Problems 33–40 (nested loops — the hardest beginner concept).
5. **Weeks 11–12:** Problems 41–48 (functions & recursion — introduce after loops).
6. **Weeks 13–14:** Problems 49–56 (arrays & strings).
7. **Weeks 15–16:** Problems 57–60 (capstone, integration).

**Note for C/C++ instructors:** Problems 1–32 translate directly. For #49–56, teach arrays with fixed size + `printf`/`scanf` instead of Python lists. For #57, use `struct` arrays.

Would you like me to produce a **C++ version** of any subset, or **unit tests** for auto-grading?
