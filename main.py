
import random
secret_number = random.randint(0,20)
print('Hi what is your name?')
name = input()
print('Okay, ' + name + ' would you like to play a game? I am thinking of a number between 0-20')

for guess_taken in range(0,6): #6 iterations
    print('Take a guess')
    guess = int(input())

    if guess < secret_number:
        print('Guess is too low')
    elif guess > secret_number:
        print('Guess too high')
    elif guess <= 0:
        print('Out of bounds')
    else:
        break

if guess == secret_number:
    print('Congratulations, You won and it took you ' + str(guess_taken) + ' guesses' )
else:
    print('You lose. Play Again!')
