"""Problem 18: Triangle validity & type."""
a, b, c = map(float, input("Sides: ").split())
if a+b>c and b+c>a and a+c>b:
    if a==b==c:               print("Equilateral")
    elif a==b or b==c or a==c: print("Isosceles")
    else:                     print("Scalene")
else:
    print("Invalid triangle")
