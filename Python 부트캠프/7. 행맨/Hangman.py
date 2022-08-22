word_list = ["ardvark", "baboon", "camel"]

from pickle import FALSE
import random

chosse_word = random.choice(word_list)
print(f'Pssst, the solution is {chosse_word}')

guess_list = []
for letter in range(len(chosse_word)):
    guess_list.append('_')
print(guess_list)

guess = input("Guess a letter: ").lower()
    
for nPosition in range(len(chosse_word)):
    letter = chosse_word[nPosition]
    if letter == guess:
        guess_list[nPosition] = guess

print(guess_list)