"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""


def main():
    """
    This program uses a for loop to print numbers from 10 to 1 to the console and the print the string "Liftoff!"
    """
    value = 10

    for i in range(10):
        print(value)
        value -= 1
    print("Liftoff!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
