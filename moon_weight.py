"""
File: moon_weight.py
--------------------
This program converts the user's weight on Earth to their weight on the moon.
"""

# Conversion factor for Earth weight to Moon weight.
MOON_CONVERSION_FACTOR = 0.165

def main():
    """
    This program asks the user to enter their weight and converts that value to their weight on the moon.
    The value for moon_weight is printed to the terminal.
    If the user enters a negative number or zero, a corresponding message is printed to the terminal.
    """
    earth_weight = float(input("Enter your weight: "))
    moon_weight = earth_weight * MOON_CONVERSION_FACTOR

    if moon_weight < 0:
        print("Sorry, you can't have a negative weight")
    elif moon_weight == 0:
        print("Sorry, enter a number that is greater than 0")
    else:
        print("Your weight on the moon is", moon_weight)

# This provided line is required at the end of a Python file
# to call the main() function.


if __name__ == '__main__':
    main()
