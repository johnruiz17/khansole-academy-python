"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    """
    This program asks the user for two numbers and then subtracts the second number from the first number.
    The result is then printed to the console.
    """

    print("This program subtracts one number from another.")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2

    print("The result is", result)



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
