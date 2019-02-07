# import random module
import random

# Assign a random interger (1-10) to the variable 'answer'
answer = random.randint(1,10)
guess = 0

# Number Guessing Game Function
def number_guessing_game(guess, answer):
    while guess == 0:
        guess = int(input('Guess a Number \n'))
    if guess < answer:
        guess = int(input('Try Again number was too low \n'))
        number_guessing_game(guess, answer)
    elif guess > answer:
        guess = int(input('Try again number was too high \n'))
        number_guessing_game(guess, answer)
    else:
        print("You're Right")
        play_again_option = int(input('Enter 1 to play again, otherwise exit program \n'))
        if play_again_option == 1:
            new_answer = random.randint(1,10)
            number_guessing_game(0, new_answer)

# Call numbers_guessing_game function
number_guessing_game(guess, answer)

# TODO: Add error handling for when user does not enter a number