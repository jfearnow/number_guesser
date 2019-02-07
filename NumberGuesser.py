import random
answer = random.randint(1,11)
guess = input('Guess a Number ')
guess = int(guess)

def number_guessing_game(guess, answer):
    # guess = input('Guess a Number ')
    # guess = int(guess)
    if guess < answer:
        guess = input('Try Again number was to low ')
        guess = int(guess)
        number_guessing_game(guess, answer)
    elif guess > answer:
        guess = input('Try again number was to high ')
        guess = int(guess)
        number_guessing_game(guess, answer)
    else:
        print('Youre Right')
number_guessing_game(guess, answer)




