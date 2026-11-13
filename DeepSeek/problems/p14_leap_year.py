"""Problem 14: Leap year checker."""
y = int(input("Year: "))
is_leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
print(f"{y} is {'a leap year' if is_leap else 'not a leap year'}")
