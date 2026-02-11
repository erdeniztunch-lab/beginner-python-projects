# Dice Rolling Game
# Ask the user if they want to roll the dice
# If the user enters "y":
#   - Generate two random numbers between 1 and 6
#   - Print the result
# If the user enters "n":
#   - Print a thank you message
#   - Exit the program
# Otherwise:
#   - Print an invalid input message

import random  # Used to generate random numbers

# Keep asking until the user provides a valid input
while True:
    user_input = input("Do you want to roll the dice? (y/n): ").lower()

    if user_input == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"You rolled {dice1} and {dice2}")

    elif user_input == "n":
        print("Thank you!")
        break

    else:
        print("Invalid input. Please enter 'y' or 'n'.")

# Program summary:
# This game loops until the user chooses to stop.
# It uses random numbers to simulate two dice and prints each roll.
# A loop is used because the number of rounds is controlled by the user.
