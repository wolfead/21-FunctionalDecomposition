"""
Hangman.

Authors: Alex and Kirk.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.
import random

with open('words.txt') as f:
    f.readline()
    string = f.read()
    words = string.split()
r = random.randrange(len(words))
secretword = words[r]
secretarray = []
for k in range(len(secretword)):
    secretarray = secretarray + ['_ ']
number_guesses = int(input('Pick a number!'))
print('You have', number_guesses,' guesses to ', end='')
print('figure out the secret word!')

def get_guess():
    print()
    guess = input('Guess a letter!')
    return guess

def check_word(guess, secretword, number_guesses):
    if guess in secretword:
        print()
        print('Good Guess!')
        for k in range(len(secretword)):
            if guess == secretword[k]:
                secretarray[k] = guess
        print()
    elif number_guesses == 1:
        print()
        print('Sorry! There is no', guess, 'in the secret word')
        print()
        return 1
    else:
        print()
        print('Sorry! There is no', guess, 'in the secret word')
        print()
        print('You now have',number_guesses-1,'guesses to figure out the secret!')
        return 1

def check_if_win(secretarray, secretword):
    for k in range(len(secretword)):
        if secretword[k] != secretarray[k]:
            return False
    return True

while True:
    for k in range(len(secretarray)):
        print(str(secretarray[k]), end='')
    print()
    guess = get_guess()
    if check_word(guess, secretword, number_guesses) == 1:
        number_guesses = number_guesses - 1
    if check_if_win(secretarray,secretword):
        print()
        print('----------------------------------------')
        print()
        print('----------------------------------------')
        print()
        print('You Win!')
        print()
        print('You solved the word:', secretword)
        print('with', number_guesses,'guesses left!')
        print()
        print('----------------------------------------')
        print()
        print('----------------------------------------')
        x = input('Do you want to play again?  y/n')
        if x == 'n':
            print()
            print('Goodbye! Thanks for playing hangman!')
            break
        if x == 'y':
            with open('words.txt') as f:
                f.readline()
                string = f.read()
                words = string.split()
            r = random.randrange(len(words))
            secretword = words[r]
            secretarray = []
            for k in range(len(secretword)):
                secretarray = secretarray + ['_ ']
            print()
            number_guesses = int(input('Pick a number'))
            print('You have', number_guesses, ' guesses to figure out the secret word!')

    if number_guesses == 0:
        print()
        print('----------------------------------------')
        print()
        print('----------------------------------------')
        print()
        print('Game Over')
        print()
        print('The secret word was', secretword, '!')
        print()
        print('----------------------------------------')
        print()
        print('----------------------------------------')
        y = input('Do you want to play again?  y/n')
        if y == 'n':
            print()
            print('Goodbye! Thanks for playing hangman!')
            break
        if y == 'y':
            with open('words.txt') as f:
                f.readline()
                string = f.read()
                words = string.split()
            r = random.randrange(len(words))
            secretword = words[r]
            secretarray = []
            for k in range(len(secretword)):
                secretarray = secretarray + ['_ ']
            print()
            number_guesses = int(input('Pick a number!'))
            print('You have', number_guesses, ' guesses to figure out the secret word!')