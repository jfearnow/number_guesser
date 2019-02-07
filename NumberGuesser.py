answer = 10
guess = input('Guess a Number ')
guess = int(guess)
while True:
    if guess < answer:
        guess = input('Try Again number was to low ')
        guess = int(guess)
    elif guess == answer:
        print('Youre Right')
        break
    elif guess > answer:
          guess = input('Try again number was to high ')
          guess = int(guess)

