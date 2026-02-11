# Rock, Paper, Scissors (DRY) -- Algorithm
# Define constants and reusable choice mappings
# Get a valid user choice
# Generate computer choice randomly
# Show both choices
# Determine and print the winner
# Ask to continue
# If user says no, stop the game

import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = {ROCK: '🪨', PAPER: '📝', SCISSORS: '✂️'}
choices = tuple(emojis.keys())


# This function is responsible only for getting a valid user choice.
def get_user_choice():
    while True:
        user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")


# This function prints both choices to keep display logic in one place.
def display_choices(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")


# This function contains winner rules, so game rules stay separate from input/output.
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
            (user_choice == PAPER and computer_choice == ROCK)):
        print("You win!")
    else:
        print("You lose!")


# This function coordinates one full game cycle and controls replay.
def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input("Continue (y/n): ").lower()
        if should_continue == 'n':
            break


# We call one main function to start the program from a single entry point.
play_game()

# Program summary:
# Constants remove repeated literals and make rule checks clearer.
# Functions separate responsibilities, so repeated logic stays in one place.
# This follows the DRY principle and makes future edits safer.
