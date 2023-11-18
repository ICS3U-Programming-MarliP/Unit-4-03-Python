#!usr/bin/env python3
# Created By: Marli Peters
# Date: Nov. 18, 2023
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display
# all numbers from 0 to that number to the power of two.


def main():
    # get user number
    user_number_str = str(input("Enter a positive number: "))
    print("")

    try:
        # catch invalid integers
        user_number_int = int(user_number_str)
        # catch negative numbers
        if user_number_int < 0:
            print("Please enter a positive number.")
        else:
            # display results
            for counter in range(user_number_int + 1):
                user_number_int = int(user_number_str)
                power_of_two = counter**2
                print("{}^2 = {}".format(counter, power_of_two))
    except:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
