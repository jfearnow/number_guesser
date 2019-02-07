import random
answer = random.randint(1,11)
guess = 0

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
            new_answer = random.randint(1,11)
            number_guessing_game(0, new_answer)
number_guessing_game(guess, answer)
