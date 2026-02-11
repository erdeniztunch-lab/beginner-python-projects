# Rock, Paper, Scissors (Modularized) -- Algorithm
# Define valid choices and display symbols
# Get a valid user choice
# Generate computer choice randomly
# Show both choices
# Determine and print the winner
# Ask to continue
# If user says no, stop the game

import random

emojis = {'r': '🪨', 'p': '📝', 's': '✂️'}
choices = ('r', 'p', 's')


# This function is responsible only for getting a valid user choice.
def get_user_chpice():
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
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
            (user_choice == 'p' and computer_choice == 'r')):
        print("You win!")
    else:
        print("You lose!")


# This function coordinates one full game cycle and controls replay.
def play_game():
    while True:
        user_choice = get_user_chpice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input("Continue (y/n): ").lower()
        if should_continue == 'n':
            break


# We call one main function to start the program from a single entry point.
play_game()

# Program summary:
# The game is split into small functions so each part has one clear job.
# This structure makes the code easier to read, test, and update.
# A main game loop is kept in play_game() to manage repeated rounds.
