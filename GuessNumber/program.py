import random

print('----------------------------------')
print('       Guess the number')
print('----------------------------------')
print()

the_number = random.randint(0, 100)

guess_text = input('Guess a number between 0 and 100... ')
guess = int(guess_text)
print(type(guess), type(guess_text))
while guess != the_number:
    if guess < the_number:
        print('Too low!')
    elif guess > the_number:
        print('Too high!')
    else:
        print('Just right')
    guess_text = input('Guess a number between 0 and 100... ')
    guess = int(guess_text)

print(the_number)