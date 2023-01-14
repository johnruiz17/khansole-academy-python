"""
File: compute_interest.py
-------------------------
This program computes the user's monthly bank account balance based on the interest rate that the user enters.
The program then prints the user's projected balance to the terminal for the time period that the user chose.
"""

GOODBYE_MESSAGE = "Thank you for using the Easy Interest app!"


def main():
    """
    Calculates and prints account balance after accrued interest for user-specified time range and interest rate.
    """
    print("Welcome to the Easy Interest app!")

    while True:
        try:
            # prompts user for initial balance and starting and ending years and months
            initial_balance = float(input("Initial balance: "))
            start_year = int(input("Start year: "))
            start_month = int(input("Start month: "))
            end_year = int(input("End year: "))
            end_month = int(input("End month: "))

            # prevents end date < start date, and prevents values less than or equal to 0
            if (end_year + (end_month / 12)) < (start_year + (start_month / 12)):
                print("Starting date needs to be before the ending date.")
            elif initial_balance <= 0 or start_year <= 0 or start_month <= 0 or end_year <= 0 or end_month <= 0:
                print("All values entered must be greater than 0.")
            else:
                break
        except ValueError:
            print("Sorry, please enter integers for months and years and the interest rate in decimal form.")

    # current values will start with initial values and user will be prompted for interest rate
    current_year = start_year
    current_month = start_month
    current_balance = initial_balance
    interest_rate = get_interest_rate()

    if interest_rate == 0:
        print(GOODBYE_MESSAGE)
    else:
        while True:
            # if the current date matches the end date, gives user the choice to end program or continue
            if current_year == end_year and current_month == end_month:
                display_balance(current_year, current_month, current_balance)
                interest_rate = get_interest_rate()
                if interest_rate == 0:
                    print(GOODBYE_MESSAGE)
                    break
            # otherwise the current balance is displayed, and the values for the current balance and month are updated
            else:
                display_balance(current_year, current_month, current_balance)
                current_month += 1
                current_balance = current_balance + (current_balance * interest_rate)

                # adjusts current month and year in January
                if current_month == 13:
                    current_year += 1
                    current_month = 1


def get_interest_rate():
    """
    Prompts user to enter an interest rate and converts the string to a float.
    """
    return float(input("Interest rate (0 to quit) "))


def display_balance(year, month, balance):
    """
    Prints the current balance for the current year and month.
    The values for the current year, month, and balance are passed in as arguments.
    """
    print("Year " + str(year) + ", month " + str(month) + " balance: " + str(balance))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
