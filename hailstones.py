"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""

SENTINEL = 1


def main():
    """
    Asks user for positive integer. If number is even, divide by 2, otherwise multiply by 3 and add 1.
    This process continues until the number becomes 1.
    Prints the number of steps required for the number to become 1.
    """

    steps = 0                                                    # the number of steps required for num to become 1

    while True:
        try:
            num = int(input("Enter a number (must be a positive integer): "))              # number entered by user
            if num > 0:
                break
            else:
                print("Value must be a positive integer. Please try again.")
        except ValueError:
            print("Value must be a positive integer. Please try again.")

    while num != SENTINEL:                                                          # while loop stops when num is 1
        if num % 2 == 0:                                                           # if num is even, divides it by 2
            old_num = num
            num /= 2
            print(str(int(old_num)), "is even, so I take half:", str(int(num)))
            steps += 1
        else:                                                                 # else, multiplies num by 3 and adds 1
            old_num = num
            num = (3 * num) + 1
            print(str(int(old_num)), "is odd, so I make 3n + 1:", str(int(num)))
            steps += 1
    print("The process took", str(steps), "steps to reach 1.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
