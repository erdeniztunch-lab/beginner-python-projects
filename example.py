# Generate a random number
# Loop
#   Ask the user to make a guess
#   if not a valid number
#   print an error
#   if number < guess
#       print too low
#   if number > guess
#       print too high
#   else
#       print well done

import random

random_number = random.randint(1, 5)

while True:
    try:
        guess = int(input("guess a number"))

        if random_number > guess:
            print("too high!")

        elif random_number > guess:
            print("too low'")
        else:
            print("you find it!")
            break
    except ValueError:
        print("invalid input!")
