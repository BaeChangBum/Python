import random
from hanman_words import word_list
  
from hanman_art import logo
print(logo)
 
chosse_word = random.choice(word_list)
print(f'Pssst, the solution is {chosse_word}')

guess_list = []
for letter in range(len(chosse_word)):
    guess_list.append('_')
print(guess_list)
 
lives = 6
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
        
    for nPosition in range(len(chosse_word)):
        letter = chosse_word[nPosition]
        if letter == guess:
            guess_list[nPosition] = guess
    
    if guess not in chosse_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(guess_list)
    
    if "_" not in guess_list:
        end_of_game = True
        print("You Win")
        
    from hanman_art import stages 
    print(stages[lives])
