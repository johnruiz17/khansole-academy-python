"""
File: pythagorean.py
--------------------
This program calculates the length of the hypotenuse when the user provides the lengths of the other two sides.
"""

import math


def main():
    """
    The user is asked to provide two values which represent two sides of a right triangle,
    or a and b in the Pythagorean theorem.
    The program then takes the square root of the sum of the squares of these values and prints them to the terminal.
    The math.sqrt() function is used from the Python math library to compute the value of c.
    """
    print("Enter values to compute the Pythagorean theorem")

    a = float(input("a: "))
    b = float(input("b: "))
    c = math.sqrt((a**2) + (b**2))

    print("a:", a)
    print("b:", b)
    print("c", c)

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
