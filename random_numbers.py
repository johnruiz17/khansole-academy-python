"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random

# Constant for the number of random numbers that will be printed to the terminal.
NUM_RANDOM = 10

# Constant for the minimum value of each random number that will be printed to the terminal.
MIN_RANDOM = 0

# Constant for the maximum value of each random number that will be printed to the terminal.
MAX_RANDOM = 100

def main():
    """
    The program uses a for loop to print 10 random numbers ranging from 0 to 100 to the terminal.
    The random.randint() function is used to generate each random number that will be printed to the terminal.
    """

    for i in range(NUM_RANDOM):
        print(random.randint(MIN_RANDOM, MAX_RANDOM))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
