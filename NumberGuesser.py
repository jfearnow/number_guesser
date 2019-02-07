import random
answer = random.randint(1,11)
guess = input('Guess a Number \n')
guess = int(guess)

def number_guessing_game(guess, answer):
    while guess == 0:
        guess = input('Guess a Number \n')
        guess = int(guess)
    if guess < answer:
        guess = input('Try Again number was too low \n')
        guess = int(guess)
        number_guessing_game(guess, answer)
    elif guess > answer:
        guess = input('Try again number was too high \n')
        guess = int(guess)
        number_guessing_game(guess, answer)
    else:
        print("You're Right")
        play_again_option = input('Enter 1 to play again, otherwise exit program \n')
        play_again_option = int(play_again_option)
        if play_again_option == 1:
            new_answer = random.randint(1,11)
            number_guessing_game(0, new_answer)
number_guessing_game(guess, answer)
