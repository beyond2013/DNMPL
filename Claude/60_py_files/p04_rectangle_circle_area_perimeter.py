"""Problem 4: Area/perimeter of rectangle; area/circumference of circle"""

import math


def p04():
    length, width, radius = 8, 5, 3
    print(f"Rectangle: area = {length * width}, perimeter = {2 * (length + width)}")
    print(f"Circle: area = {math.pi * radius ** 2:.2f}, "
          f"circumference = {2 * math.pi * radius:.2f}")


if __name__ == "__main__":
    p04()
