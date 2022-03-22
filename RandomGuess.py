from random import *
print('Welcome to the guessing game!')
randNb = randint(1, 10) # randomize bounds
print('Guess the random number generated between 1 and 10!')
guess = '0'
while (int(guess) != randNb):
    guess = input()
    if (int(guess) < randNb):
        print('Too low')
    elif (int(guess) > randNb):
        print('Too high')
    else:
        break
print('Just right!, the answer is ' + str(randNb))
