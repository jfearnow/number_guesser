import random
answer = random.randint(1,11)
guess = input('Guess a Number ')
guess = int(guess)

def number_guessing_game(guess, answer):
    if guess < answer:
        guess = input('Try Again number was to low \n')
        guess = int(guess)
        number_guessing_game(guess, answer)
    elif guess > answer:
        guess = input('Try again number was to high \n')
        guess = int(guess)
        number_guessing_game(guess, answer)
    else:
        print('Youre Right')
        play_again_option = input('Enter 1 to play again, otherwise exit program \n')
        play_again_option = int(play_again_option)
        if play_again_option == 1:
            new_answer = random.randint(2,11)
            number_guessing_game(guess, new_answer)
number_guessing_game(guess, answer)




