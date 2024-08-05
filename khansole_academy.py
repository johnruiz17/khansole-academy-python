"""
File: khansole_academy.py
-------------------------
This program asks the user to add two randomly generated numbers. Once the user gets three questions correct in a row,
the program congratulates them and then closes. Program lets user quit anytime by entering 0 and checks that
the user enters integers only using a try except block.
"""

import random


def main():
    """
    The main while loop in the program continues to run as long as the number of correct responses is less than 3.
    The try except block prevents the user from crashing the program when they enter a non-integer value and
    prompts them to re-enter their response.
    """

    # The correct variable stores the number of correct responses that the user has entered in a row.
    correct = 0

    # Program ends when user answers 3 questions correctly in a row.
    while correct < 3:
        # Two random numbers are generated and added together, each value is stored
        random_num1 = random_number()
        random_num2 = random_number()
        total = random_num1 + random_num2

        prompt = "What is " + str(random_num1) + "+ " + str(random_num2) + "? (Enter 0 to quit) "

        # If the user gets the question right, correct is incremented by 1, otherwise it is set to 0.
        try:
            user_answer = int(input(prompt))

            # The program ends if the user enters 0.
            if user_answer == 0:
                break
            elif user_answer == total:
                correct += 1
                print("Correct! You've gotten", correct, "in a row.")
                if correct == 3:
                    print("Congratulations! You mastered addition!")
            else:
                correct = 0
                print("Incorrect. The expected answer is", total)
        except ValueError:
            print("Sorry, please enter integers only.")


def random_number():
    """
    This function returns a random number from 0 to 100 using the random.randint function
    from the Python random library.
    """
    return random.randint(0, 100)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
