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

number_guesses = int(input('Pick a number:'))




def get_guess():
    guess = input('Guess a letter boi')
    return guess



def main():
    for k in range(len(secretarray)):
        print(str(secretarray[k]), end='')
    print()
    while True:
        guess = get_guess()
        check_word(guess, secretword, number_guesses)
        for k in range (len(secretarray)):
            print(str(secretarray[k]), end='')
        print()




def check_word(guess, secretword, number_guesses):
    if guess in secretword:
        print('Good Guess!')
        for k in range (len(secretword)):
            if guess == secretword[k]:
                secretarray[k] = guess
    else:
        number_guesses = number_guesses - 1
        print(number_guesses)
        print('Sorry! There are no',guess,'s in the secret word')







while number_guesses > 0:
    main()




